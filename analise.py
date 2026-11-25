"""
Análise do experimento: complexidade ciclomática (CC) e LOC de código gerado por duas IAs.

Instalação:
    pip install radon scipy pandas numpy matplotlib

Estrutura esperada das pastas (mesmo nome de arquivo = mesmo problema):
    solucoes/
        ia_a/p01.py ... p30.py
        ia_b/p01.py ... p30.py

Opcional: aceitas.csv com colunas  problema,ia,aceita   (ex.: p01,ia_a,1)
    -> registra se a solução foi aceita pelo juiz (LeetCode).
       Se existir, a análise é repetida só com os pares em que as duas foram aceitas.

Uso:
    python analise.py --a ia_a --b ia_b
Saídas: metricas.csv, resultados.txt, tabela_descritiva.tex, boxplot_cc.pdf, boxplot_loc.pdf
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
from radon.visitors import ComplexityVisitor
from radon.raw import analyze
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def _closures(f):
    """Funções internas (definidas dentro de outra função), em qualquer nível."""
    for c in f.closures:
        yield c
        yield from _closures(c)


def _todas_funcoes(v):
    def metodos(cls):
        for m in cls.methods:
            yield m
        for ic in cls.inner_classes:
            yield from metodos(ic)
    principais = list(v.functions) + [m for c in v.classes for m in metodos(c)]
    internas = [c for f in principais for c in _closures(f)]
    return principais, internas


def extrair_metricas(arquivo: Path) -> dict:
    codigo = arquivo.read_text(encoding="utf-8")
    v = ComplexityVisitor.from_code(codigo)
    principais, internas = _todas_funcoes(v)
    blocos = [f.complexity for f in principais + internas]
    return {
        # CC total = nível do módulo + todas as funções/métodos + funções internas
        # (o total_complexity do radon não soma funções internas, ex.: dfs dentro de um método)
        "cc_total": v.total_complexity + sum(f.complexity for f in internas),
        "cc_max": max(blocos + [v.complexity]),
        "n_funcoes_internas": len(internas),
        "sloc": analyze(codigo).sloc,  # linhas de código sem comentários/brancos
    }


def coletar(base: Path, ia_a: str, ia_b: str) -> pd.DataFrame:
    linhas = []
    for ia in (ia_a, ia_b):
        for arq in sorted((base / ia).glob("*.py")):
            linhas.append({"problema": arq.stem, "ia": ia, **extrair_metricas(arq)})
    df = pd.DataFrame(linhas)
    faltando = set(df[df.ia == ia_a].problema) ^ set(df[df.ia == ia_b].problema)
    if faltando:
        raise SystemExit(f"Problemas sem par nas duas IAs: {sorted(faltando)}")
    return df


def rank_biserial_pareado(dif: np.ndarray) -> float:
    """Correlação rank-bisserial para amostras pareadas (Kerby, 2014)."""
    d = dif[dif != 0]
    if len(d) == 0:
        return 0.0
    r = stats.rankdata(np.abs(d))
    w_pos, w_neg = r[d > 0].sum(), r[d < 0].sum()
    return (w_pos - w_neg) / (w_pos + w_neg)


def cliffs_delta(x: np.ndarray, y: np.ndarray) -> float:
    maiores = sum((xi > y).sum() for xi in x)
    menores = sum((xi < y).sum() for xi in x)
    return (maiores - menores) / (len(x) * len(y))


def magnitude_cliff(d: float) -> str:  # limiares de Romano et al. (2006)
    d = abs(d)
    return "desprezível" if d < 0.147 else "pequeno" if d < 0.33 else "médio" if d < 0.474 else "grande"


def analisar(df: pd.DataFrame, ia_a: str, ia_b: str, metrica: str, titulo: str) -> str:
    wide = df.pivot(index="problema", columns="ia", values=metrica)
    a, b = wide[ia_a].to_numpy(float), wide[ia_b].to_numpy(float)
    dif = a - b
    out = [f"\n=== {titulo} | métrica: {metrica} | n = {len(a)} pares ==="]
    for nome, x in ((ia_a, a), (ia_b, b)):
        q1, q3 = np.percentile(x, [25, 75])
        out.append(f"{nome}: média={x.mean():.2f} dp={x.std(ddof=1):.2f} mediana={np.median(x):.2f} "
                   f"Q1={q1:.2f} Q3={q3:.2f} min={x.min():.0f} max={x.max():.0f}")
    out.append(f"Pares empatados (diferença zero): {(dif == 0).sum()}")

    if np.all(dif == 0):
        out.append("Todas as diferenças são zero: teste não aplicável.")
        return "\n".join(out)

    if np.ptp(dif) == 0:
        out.append("Shapiro-Wilk: diferenças constantes, teste de normalidade não aplicável.")
    else:
        sw = stats.shapiro(dif)
        out.append(f"Shapiro-Wilk nas diferenças: W={sw.statistic:.3f}, p={sw.pvalue:.4f} "
                   f"({'não normal' if sw.pvalue < 0.05 else 'normalidade não rejeitada'})")

    w = stats.wilcoxon(a, b, zero_method="wilcox", alternative="two-sided")
    out.append(f"Wilcoxon signed-rank (bicaudal): W={w.statistic:.1f}, p={w.pvalue:.4f} -> "
               f"{'rejeita H0' if w.pvalue < 0.05 else 'não rejeita H0'} (alfa = 0,05)")
    wp = stats.wilcoxon(a, b, zero_method="pratt")
    out.append(f"  (verificação de robustez, zero_method='pratt': p={wp.pvalue:.4f})")

    t = stats.ttest_rel(a, b)
    dz = dif.mean() / dif.std(ddof=1) if dif.std(ddof=1) > 0 else float("nan")
    out.append(f"t pareado (referência): t={t.statistic:.3f}, p={t.pvalue:.4f}, Cohen's d_z={dz:.3f}")

    rrb = rank_biserial_pareado(dif)
    cd = cliffs_delta(a, b)
    out.append(f"Effect size: rank-bisserial pareado r={rrb:.3f} | Cliff's delta={cd:.3f} ({magnitude_cliff(cd)})")
    out.append(f"(valores positivos = {ia_a} tende a ter {metrica} maior que {ia_b})")
    return "\n".join(out)


def tabela_latex(df: pd.DataFrame, ia_a: str, ia_b: str) -> str:
    linhas = [r"\begin{table}[ht]", r"\centering",
              r"\caption{Estatística descritiva das métricas por IA}", r"\label{tab:descritiva}",
              r"\begin{tabular}{llrrrrr}", r"\hline",
              r"Métrica & IA & Média & DP & Mediana & Mín. & Máx. \\ \hline"]
    for met, rot in (("cc_total", "CC total"), ("sloc", "SLOC")):
        for ia in (ia_a, ia_b):
            x = df[df.ia == ia][met]
            linhas.append(f"{rot} & {ia.replace('_', r'\_')} & {x.mean():.2f} & {x.std():.2f} & "
                          f"{x.median():.1f} & {x.min()} & {x.max()} \\\\")
    linhas += [r"\hline", r"\end{tabular}", r"\end{table}"]
    return "\n".join(linhas)


def boxplot(df, ia_a, ia_b, metrica, rotulo, arquivo):
    plt.figure(figsize=(4.5, 3.5))
    dados = [df[df.ia == ia_a][metrica], df[df.ia == ia_b][metrica]]
    try:
        plt.boxplot(dados, tick_labels=[ia_a, ia_b])  # matplotlib >= 3.9
    except TypeError:
        plt.boxplot(dados, labels=[ia_a, ia_b])       # versões antigas
    plt.ylabel(rotulo)
    plt.tight_layout()
    plt.savefig(arquivo)
    plt.close()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base", default="solucoes")
    p.add_argument("--a", default="ia_a")
    p.add_argument("--b", default="ia_b")
    args = p.parse_args()

    df = coletar(Path(args.base), args.a, args.b)
    df.to_csv("metricas.csv", index=False)

    relatorio = []
    for met in ("cc_total", "sloc", "cc_max"):
        relatorio.append(analisar(df, args.a, args.b, met, "Todos os pares"))

    if Path("aceitas.csv").exists():
        ac = pd.read_csv("aceitas.csv")
        relatorio.append("\nTaxa de aceitação: " +
                         ", ".join(f"{ia}={g.aceita.mean():.0%}" for ia, g in ac.groupby("ia")))
        ok = ac.groupby("problema").aceita.min()
        ok = ok[ok == 1].index
        sub = df[df.problema.isin(ok)]
        if sub.empty:
            raise SystemExit("Nenhum par aceito encontrado: confira se os nomes em aceitas.csv "
                             "são iguais aos nomes dos arquivos (ex.: p01 e p01.py).")
        for met in ("cc_total", "sloc"):
            relatorio.append(analisar(sub, args.a, args.b, met, "Só pares com as duas soluções aceitas"))

    texto = "\n".join(relatorio)
    Path("resultados.txt").write_text(texto, encoding="utf-8")
    Path("tabela_descritiva.tex").write_text(tabela_latex(df, args.a, args.b), encoding="utf-8")
    boxplot(df, args.a, args.b, "cc_total", "Complexidade ciclomática total", "boxplot_cc.pdf")
    boxplot(df, args.a, args.b, "sloc", "SLOC", "boxplot_loc.pdf")
    print(texto)


if __name__ == "__main__":
    main()
