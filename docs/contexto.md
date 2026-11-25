# Contexto do projeto (lido apenas fora da coleta)

Trabalho da disciplina **Engenharia de Software Experimental** (Bacharelado em Engenharia de Software,
UDESC Alto Vale, Prof. Dr. Paulo Roberto Farah). Dupla. Idioma de tudo: **português**.

Entrega: artigo no template **SBC** (LaTeX, compilado em https://latex.sistemas.udesc.br) +
apresentação de até 15 min (27/11/2026 ou 04/12/2026). O enunciado exige: questão de pesquisa, hipótese,
coleta em contexto real, **estatística descritiva, teste de hipótese e effect size**, ameaças à validade,
limitações e aspectos éticos. **Plágio ou fraude (dados não verdadeiros) zeram a nota.**

## O estudo

- **Estratégia:** experimento *in vitro*, delineamento **pareado** (cada problema recebe os dois tratamentos).
- **QP:** Há diferença na complexidade ciclomática das soluções geradas pelo Claude e pelo Gemini
  para os mesmos problemas de programação?
- **H0:** mediana das diferenças pareadas de CC total (Claude − Gemini) = 0.
  **H1:** mediana das diferenças ≠ 0. Hipóteses análogas para SLOC (análise secundária).
- **Variável independente:** IA (2 níveis). **Dependentes:** CC total (módulo + funções/métodos, via radon
  `ComplexityVisitor.total_complexity`) e SLOC (radon raw). **Controle:** aceita ou não no LeetCode.
- **Amostra:** 30 problemas gratuitos do LeetCode, 10 fáceis / 10 médios / 10 difíceis (`problemas.csv`).
  Seleção por conveniência, sugerida por IA (Claude), já declarada como ameaça.
- **Análise:** descritiva + boxplots; Shapiro-Wilk nas diferenças; **Wilcoxon signed-rank** bicaudal
  (α = 0,05), robustez com `zero_method="pratt"`; effect size **rank-bisserial pareado** (Kerby, 2014) e
  **delta de Cliff** (limiares de Romano et al., 2006). Repetir só com pares em que ambas foram aceitas.

## Modelos e ferramentas (registrar exatamente assim)

- **Claude:** Claude Code no VS Code, modelo **Sonnet 4.6**.
- **Gemini:** app gemini.google.com, "Análise mais profunda" (**4 Neon**), **Nível de Raciocínio Alto**,
  plano Google AI Pro. O modelo "Programação e tarefas complexas (4 Carbon)" estava bloqueado no plano.
- Justificativa da escolha: nível intermediário de cada família (Sonnet entre Haiku e Opus; Neon entre
  Hydrogen e Carbon). Equivalência aproximada, declarada como limitação.

## Protocolo de coleta

1. Prompts prontos em `prompts_claude.md` e `prompts_gemini.md` (textos idênticos, exceto o caminho de
   salvamento). Enunciados reescritos em português a partir do LeetCode, com regras, exemplos e restrições.
2. Uma conversa nova por problema (`/clear` no Claude Code; "Nova conversa" no Gemini).
3. Primeira resposta, sem regenerar nem pedir correção. O Claude Code é instruído a não executar nem testar.
   No Gemini, copia-se só o código da resposta, sem alteração, para `solucoes/gemini/pXX.py`.
4. Submissão no LeetCode; registro em `aceitas.csv` (`problema,ia,aceita` com 1/0) e em
   `registro_coleta.csv` (`problema,ia,data,modelo,observacoes`). Falhou = anota 0, sem correção.
5. O `CLAUDE.md` é mantido curto e neutro (sem mencionar métricas ou hipóteses) para não influenciar as
   soluções geradas pelo Claude Code; este contexto fica em `docs/` e não é lido na coleta.

## Estrutura do repositório

```
CLAUDE.md, README.md, docs/contexto.md
prompts_claude.md, prompts_gemini.md
problemas.csv, aceitas.csv, registro_coleta.csv
solucoes/claude/  solucoes/gemini/
analise.py            # python analise.py --a claude --b gemini  (rodar na raiz)
artigo/artigo.tex, artigo/referencias.bib   # + sbc-template.sty e sbc.bst do template SBC
resultados/           # mover para cá: resultados.txt, metricas.csv, tabela_descritiva.tex, boxplots
```

## Regras (fora da coleta)

- **Nunca alterar, corrigir ou reformatar arquivos em `solucoes/`.** Pode apenas ler e validar (checar se
  os 60 arquivos existem e se o radon consegue analisá-los). Se um arquivo tiver texto que não é código,
  **avisar** em vez de editar.
- **Nunca inventar dados ou resultados.** Todo número do artigo vem de `resultados/`, gerado pelo
  `analise.py` sobre os dados reais. Sem resultados, deixar `[PREENCHER]`.
- Não alterar `aceitas.csv` nem `registro_coleta.csv` sem pedido explícito.
- Não adicionar referências não verificadas; marcar `% VERIFICAR` quando incerto.
- Conflito de interesse declarado (o Claude ajuda no trabalho e é um dos modelos comparados): redação
  neutra; se o resultado não favorecer o Claude, ele é reportado como está.
- Se não rejeitar H0: "não houve evidência de diferença", nunca "são iguais".

## Ameaças à validade (manter no artigo)

- **Interna:** não determinismo (uma execução por problema); influência do prompt; seleção dos problemas
  sugerida por um dos modelos comparados; **ferramentas diferentes** (Claude Code, um agente com acesso ao
  repositório, vs. app web do Gemini), mitigado com instrução de não executar/testar e `CLAUDE.md` neutro.
- **Construção:** CC e SLOC medem só estrutura; SLOC depende de estilo; soluções incorretas distorcem as
  métricas; enunciados reescritos podem diferir levemente dos originais.
- **Externa:** só Python e problemas de programação competitiva; versões dos modelos na data da coleta;
  provável contaminação (problemas populares nos dados de treinamento); modelo de programação do Gemini
  bloqueado no plano.
- **Conclusão:** n = 30 (poder limitado); empates descartados no Wilcoxon; duas métricas testadas (SLOC é
  secundária).

## Status

- [x] Tema, desenho, hipóteses, script de análise, esqueleto do artigo, lista de problemas, prompts
- [x] Modelos definidos (Sonnet 4.6 via Claude Code; Gemini 4 Neon, raciocínio Alto, via app)
- [ ] Coleta das 60 soluções + submissões no LeetCode
- [ ] Rodar `analise.py`, mover saídas para `resultados/`
- [ ] Atualizar a seção de coleta do `artigo.tex` (enunciados reescritos; ferramentas usadas)
- [ ] Preencher Resultados, Discussão, Resumo/Abstract, Conclusão; adicionar 2–3 trabalhos relacionados
- [ ] Slides (15 min)
