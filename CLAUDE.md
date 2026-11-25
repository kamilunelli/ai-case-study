# Contexto do projeto (leia antes de qualquer tarefa)

Trabalho da disciplina **Engenharia de Software Experimental** (Bacharelado em Engenharia de Software,
UDESC Alto Vale, Prof. Dr. Paulo Roberto Farah). Dupla de alunas/alunos. Idioma de tudo: **português**.

Entrega: artigo no template **SBC** (LaTeX, compilado em https://latex.sistemas.udesc.br) +
apresentação de até 15 min (dias 27/11/2026 e 04/12/2026). O enunciado exige: questão de pesquisa,
hipótese, coleta em contexto real, **estatística descritiva, teste de hipótese e effect size**,
ameaças à validade, limitações e aspectos éticos. **Plágio ou fraude (dados não verdadeiros) zeram a nota.**

## O estudo

- **Estratégia:** experimento *in vitro*, delineamento **pareado** (cada problema recebe os dois tratamentos).
- **QP:** Há diferença na complexidade ciclomática das soluções geradas pelo Claude e pelo Gemini
  para os mesmos problemas de programação?
- **H0:** mediana das diferenças pareadas de CC total (Claude − Gemini) = 0.
  **H1:** mediana das diferenças ≠ 0. Hipóteses análogas para SLOC (análise secundária).
- **Variável independente:** IA (2 níveis). **Dependentes:** CC total (módulo + funções/métodos, via
  radon `ComplexityVisitor.total_complexity`) e SLOC (radon raw). **Controle:** aceita ou não no LeetCode.
- **Amostra:** 30 problemas gratuitos do LeetCode, 10 fáceis / 10 médios / 10 difíceis
  (lista em `problemas.csv`). Seleção por conveniência, sugerida por IA (Claude) — já declarado como ameaça.
- **Análise:** descritiva + boxplots; Shapiro-Wilk nas diferenças; **Wilcoxon signed-rank** bicaudal
  (α = 0,05), robustez com `zero_method="pratt"`; effect size **rank-bisserial pareado** (Kerby, 2014)
  e **delta de Cliff** (limiares de Romano et al., 2006). Repetir só com pares em que ambas foram aceitas.

## Modelos (registrar exatamente assim)

- **Gemini:** app gemini.google.com, opção "Análise mais profunda (4 Neon)" (marcada como "Novo"),
  nível de raciocínio **Alto**, plano **Google AI Pro**. O modelo "Programação e tarefas complexas
  (4 Carbon)" estava **bloqueado** no plano — declarar como ameaça.
- **Claude:** app claude.ai (plano pago), modelo de nível comparável com raciocínio estendido ativado.
  **[PREENCHER modelo exato escolhido antes da coleta]**.
- Ambos via **chat** (mesmo tipo de interface). Não usar agentes (Antigravity, Claude Code) para gerar
  as soluções, porque eles podem executar e corrigir o código, o que confundiria a comparação.

## Protocolo de coleta

1. Uma conversa nova por problema; busca na web e memória desligadas, se existirem.
2. Mesmo prompt nas duas IAs:
   ```
   Resolva o problema a seguir em Python 3.
   Use exatamente a assinatura fornecida.
   Responda apenas com o código, sem explicações.

   [ENUNCIADO COMPLETO, COM EXEMPLOS E RESTRIÇÕES]

   Código inicial:
   [TRECHO DO EDITOR DO LEETCODE EM PYTHON 3]
   ```
3. Guardar a **primeira resposta**, sem regenerar nem pedir correção. Se vier texto junto, copiar só o
   código, **sem alterar nada**.
4. Salvar em `solucoes/claude/pXX.py` e `solucoes/gemini/pXX.py` (pXX conforme `problemas.csv`).
5. Submeter no LeetCode; registrar em `aceitas.csv` (`problema,ia,aceita` com 1/0).
6. Registrar data, modelo e observações em `registro_coleta.csv`. Coletas das duas IAs nos mesmos dias.

## Estrutura do repositório

```
README.md, protocolo.md, CLAUDE.md
problemas.csv, aceitas.csv, registro_coleta.csv
solucoes/claude/  solucoes/gemini/
analise.py            # python analise.py --a claude --b gemini  (rodar na raiz)
artigo/artigo.tex, artigo/referencias.bib   # + sbc-template.sty e sbc.bst do template SBC
resultados/           # mover para cá: resultados.txt, metricas.csv, tabela_descritiva.tex, boxplots
```

## REGRAS PARA O CLAUDE CODE (obrigatórias)

- **Nunca criar, gerar, corrigir, reformatar ou "melhorar" arquivos em `solucoes/`.** Eles são os dados
  brutos do experimento. Pode apenas ler e validar (ex.: checar se todos os 60 arquivos existem e se o
  radon consegue analisá-los). Se um arquivo tiver texto que não é código, **avisar** em vez de editar.
- **Nunca inventar dados ou resultados.** Todo número do artigo deve vir de `resultados/` gerado pelo
  `analise.py` sobre os dados reais. Se os resultados ainda não existem, deixar `[PREENCHER]`.
- Não alterar `aceitas.csv` nem `registro_coleta.csv` sem pedido explícito.
- Não adicionar referências que não foram verificadas; marcar como `% VERIFICAR` quando incerto.
- Não colocar enunciados completos do LeetCode no repositório (só número e link).
- Se o resultado não favorecer o Claude, ele é reportado como está. Há conflito de interesse
  declarado (o Claude ajuda no trabalho e é um dos modelos comparados); ser neutro na redação.
- Ao interpretar: se não rejeitar H0, escrever "não houve evidência de diferença", nunca "são iguais".

## Ameaças à validade já identificadas (manter no artigo)

Interna: não determinismo dos modelos (uma execução por problema); influência do prompt; seleção dos
problemas sugerida por um dos modelos comparados. Construção: CC e SLOC medem só estrutura; SLOC depende de
estilo; soluções incorretas distorcem métricas. Externa: só Python, só problemas de programação competitiva,
versões dos modelos na data da coleta, provável contaminação (problemas populares nos dados de treinamento),
modelo de programação do Gemini bloqueado no plano. Conclusão: n = 30 (poder limitado), empates descartados
no Wilcoxon, duas métricas testadas (SLOC é secundária).

## Status

- [x] Tema, desenho, hipóteses, script de análise, esqueleto do artigo, lista de problemas
- [ ] Definir e registrar o modelo exato do Claude
- [ ] Coleta das 60 soluções + submissões no LeetCode
- [ ] Rodar `analise.py`, mover saídas para `resultados/`
- [ ] Preencher Resultados, Discussão, Resumo/Abstract, Conclusão; adicionar 2–3 trabalhos relacionados lidos pela dupla
- [ ] Slides (15 min)
