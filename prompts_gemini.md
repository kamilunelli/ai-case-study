# Prompts — Gemini

Ferramenta: Antigravity ou app do Gemini. Para cada problema: abra uma conversa/sessão limpa (no Claude Code: `/clear`), copie o bloco inteiro e cole. Depois submeta no LeetCode e anote em `aceitas.csv`.

Os enunciados foram reescritos em português a partir do LeetCode, mantendo regras, exemplos e restrições. Os dois arquivos de prompts são idênticos, exceto pelo caminho onde a solução é salva.


---

## p01 — 1. Two Sum (Fácil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p01.py

Dado um array de inteiros `nums` e um inteiro `target`, retorne os índices de dois números do array cuja soma seja igual a `target`. Existe exatamente uma solução, e o mesmo elemento não pode ser usado duas vezes. Os índices podem ser retornados em qualquer ordem.

Exemplos:
- nums = [2,7,11,15], target = 9 → [0,1]
- nums = [3,2,4], target = 6 → [1,2]
- nums = [3,3], target = 6 → [0,1]

Restrições: 2 <= len(nums) <= 10^4; -10^9 <= nums[i], target <= 10^9; existe exatamente uma resposta válida.

Código inicial:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
```

---

## p02 — 13. Roman to Integer (Fácil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p02.py

Converta um número romano (string `s`) para inteiro. Os símbolos valem: I=1, V=5, X=10, L=50, C=100, D=500, M=1000. Normalmente os símbolos aparecem do maior para o menor e são somados, mas existem seis casos de subtração: IV=4, IX=9, XL=40, XC=90, CD=400, CM=900.

Exemplos:
- s = "III" → 3
- s = "LVIII" → 58
- s = "MCMXCIV" → 1994

Restrições: 1 <= len(s) <= 15; s contém apenas I, V, X, L, C, D, M; s é um número romano válido entre 1 e 3999.

Código inicial:
class Solution:
    def romanToInt(self, s: str) -> int:
        
```

---

## p03 — 14. Longest Common Prefix (Fácil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p03.py

Dada uma lista de strings `strs`, retorne o maior prefixo comum a todas elas. Se não houver prefixo comum, retorne a string vazia "".

Exemplos:
- strs = ["flower","flow","flight"] → "fl"
- strs = ["dog","racecar","car"] → ""

Restrições: 1 <= len(strs) <= 200; 0 <= len(strs[i]) <= 200; strs[i] contém apenas letras minúsculas do inglês.

Código inicial:
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
```

---

## p04 — 20. Valid Parentheses (Fácil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p04.py

Dada uma string `s` contendo apenas os caracteres '(', ')', '{', '}', '[' e ']', determine se ela é válida. Ela é válida se: todo símbolo de abertura é fechado pelo mesmo tipo; os fechamentos ocorrem na ordem correta; e todo símbolo de fechamento tem uma abertura correspondente.

Exemplos:
- s = "()" → true
- s = "()[]{}" → true
- s = "(]" → false
- s = "([])" → true

Restrições: 1 <= len(s) <= 10^4; s contém apenas '()[]{}'.

Código inicial:
class Solution:
    def isValid(self, s: str) -> bool:
        
```

---

## p05 — 21. Merge Two Sorted Lists (Fácil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p05.py

Você recebe as cabeças de duas listas ligadas, `list1` e `list2`, ambas ordenadas em ordem crescente. Junte-as em uma única lista ordenada, formada pelo encadeamento dos nós das duas listas, e retorne a cabeça da lista resultante.

Exemplos:
- list1 = [1,2,4], list2 = [1,3,4] → [1,1,2,3,4,4]
- list1 = [], list2 = [] → []
- list1 = [], list2 = [0] → [0]

Restrições: cada lista tem de 0 a 50 nós; -100 <= Node.val <= 100; ambas estão em ordem crescente.

Código inicial:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
```

---

## p06 — 70. Climbing Stairs (Fácil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p06.py

Você está subindo uma escada com `n` degraus. A cada passo, pode subir 1 ou 2 degraus. De quantas maneiras distintas é possível chegar ao topo?

Exemplos:
- n = 2 → 2 (1+1, 2)
- n = 3 → 3 (1+1+1, 1+2, 2+1)

Restrições: 1 <= n <= 45.

Código inicial:
class Solution:
    def climbStairs(self, n: int) -> int:
        
```

---

## p07 — 121. Best Time to Buy and Sell Stock (Fácil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p07.py

Dado um array `prices`, em que prices[i] é o preço de uma ação no dia i, escolha um único dia para comprar e um dia posterior para vender, maximizando o lucro. Retorne o lucro máximo possível; se não for possível ter lucro, retorne 0.

Exemplos:
- prices = [7,1,5,3,6,4] → 5 (compra a 1, vende a 6)
- prices = [7,6,4,3,1] → 0

Restrições: 1 <= len(prices) <= 10^5; 0 <= prices[i] <= 10^4.

Código inicial:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
```

---

## p08 — 125. Valid Palindrome (Fácil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p08.py

Uma frase é palíndromo se, depois de converter todas as letras maiúsculas em minúsculas e remover todos os caracteres não alfanuméricos, ela é lida igual de trás para frente. Letras e números são alfanuméricos. Dada uma string `s`, retorne true se for palíndromo e false caso contrário.

Exemplos:
- s = "A man, a plan, a canal: Panama" → true
- s = "race a car" → false
- s = " " → true (vira string vazia, que é palíndromo)

Restrições: 1 <= len(s) <= 2 * 10^5; s contém apenas caracteres ASCII imprimíveis.

Código inicial:
class Solution:
    def isPalindrome(self, s: str) -> bool:
        
```

---

## p09 — 242. Valid Anagram (Fácil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p09.py

Dadas duas strings `s` e `t`, retorne true se `t` for um anagrama de `s` (mesmas letras, com as mesmas quantidades, em qualquer ordem) e false caso contrário.

Exemplos:
- s = "anagram", t = "nagaram" → true
- s = "rat", t = "car" → false

Restrições: 1 <= len(s), len(t) <= 5 * 10^4; s e t contêm apenas letras minúsculas do inglês.

Código inicial:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
```

---

## p10 — 704. Binary Search (Fácil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p10.py

Dado um array de inteiros `nums` ordenado em ordem crescente e um inteiro `target`, retorne o índice de `target` em `nums`, ou -1 se ele não existir. O algoritmo deve ter complexidade O(log n).

Exemplos:
- nums = [-1,0,3,5,9,12], target = 9 → 4
- nums = [-1,0,3,5,9,12], target = 2 → -1

Restrições: 1 <= len(nums) <= 10^4; -10^4 < nums[i], target < 10^4; todos os elementos de nums são distintos; nums está em ordem crescente.

Código inicial:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
```

---

## p11 — 3. Longest Substring Without Repeating Characters (Média)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p11.py

Dada uma string `s`, retorne o comprimento da maior substring (trecho contínuo) sem caracteres repetidos.

Exemplos:
- s = "abcabcbb" → 3 ("abc")
- s = "bbbbb" → 1 ("b")
- s = "pwwkew" → 3 ("wke"; "pwke" não vale porque não é contínuo)

Restrições: 0 <= len(s) <= 5 * 10^4; s contém letras do inglês, dígitos, símbolos e espaços.

Código inicial:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
```

---

## p12 — 5. Longest Palindromic Substring (Média)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p12.py

Dada uma string `s`, retorne a maior substring de `s` que seja palíndromo.

Exemplos:
- s = "babad" → "bab" ("aba" também é uma resposta aceita)
- s = "cbbd" → "bb"

Restrições: 1 <= len(s) <= 1000; s contém apenas dígitos e letras do inglês.

Código inicial:
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
```

---

## p13 — 11. Container With Most Water (Média)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p13.py

Você recebe um array `height` de tamanho n. Existem n linhas verticais: a linha i vai do ponto (i, 0) até (i, height[i]). Escolha duas linhas que, junto com o eixo x, formem um recipiente que armazene a maior quantidade de água possível. Retorne essa quantidade máxima. O recipiente não pode ser inclinado.

Exemplos:
- height = [1,8,6,2,5,4,8,3,7] → 49
- height = [1,1] → 1

Restrições: 2 <= n <= 10^5; 0 <= height[i] <= 10^4.

Código inicial:
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
```

---

## p14 — 15. 3Sum (Média)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p14.py

Dado um array de inteiros `nums`, retorne todas as triplas [nums[i], nums[j], nums[k]] com i, j e k distintos e nums[i] + nums[j] + nums[k] == 0. A resposta não pode conter triplas repetidas. A ordem das triplas e dos elementos não importa.

Exemplos:
- nums = [-1,0,1,2,-1,-4] → [[-1,-1,2],[-1,0,1]]
- nums = [0,1,1] → []
- nums = [0,0,0] → [[0,0,0]]

Restrições: 3 <= len(nums) <= 3000; -10^5 <= nums[i] <= 10^5.

Código inicial:
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
```

---

## p15 — 22. Generate Parentheses (Média)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p15.py

Dado `n` pares de parênteses, gere todas as combinações de parênteses bem formados (balanceados). A ordem da lista não importa.

Exemplos:
- n = 3 → ["((()))","(()())","(())()","()(())","()()()"]
- n = 1 → ["()"]

Restrições: 1 <= n <= 8.

Código inicial:
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
```

---

## p16 — 33. Search in Rotated Sorted Array (Média)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p16.py

Um array de inteiros distintos, originalmente em ordem crescente, pode ter sido rotacionado em um ponto desconhecido (por exemplo, [0,1,2,4,5,6,7] pode virar [4,5,6,7,0,1,2]). Dado esse array `nums` e um inteiro `target`, retorne o índice de `target`, ou -1 se ele não existir. O algoritmo deve ter complexidade O(log n).

Exemplos:
- nums = [4,5,6,7,0,1,2], target = 0 → 4
- nums = [4,5,6,7,0,1,2], target = 3 → -1
- nums = [1], target = 0 → -1

Restrições: 1 <= len(nums) <= 5000; -10^4 <= nums[i], target <= 10^4; todos os valores são distintos; nums é um array crescente possivelmente rotacionado.

Código inicial:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
```

---

## p17 — 49. Group Anagrams (Média)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p17.py

Dada uma lista de strings `strs`, agrupe as strings que são anagramas entre si. A ordem dos grupos e das strings dentro de cada grupo não importa.

Exemplos:
- strs = ["eat","tea","tan","ate","nat","bat"] → [["bat"],["nat","tan"],["ate","eat","tea"]]
- strs = [""] → [[""]]
- strs = ["a"] → [["a"]]

Restrições: 1 <= len(strs) <= 10^4; 0 <= len(strs[i]) <= 100; strs[i] contém apenas letras minúsculas do inglês.

Código inicial:
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
```

---

## p18 — 56. Merge Intervals (Média)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p18.py

Dado um array `intervals`, em que intervals[i] = [inicio_i, fim_i], junte todos os intervalos que se sobrepõem e retorne um array de intervalos sem sobreposição que cubra todos os intervalos da entrada. Intervalos que apenas se tocam (ex.: [1,4] e [4,5]) também devem ser unidos.

Exemplos:
- intervals = [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]
- intervals = [[1,4],[4,5]] → [[1,5]]

Restrições: 1 <= len(intervals) <= 10^4; intervals[i] tem 2 elementos; 0 <= inicio_i <= fim_i <= 10^4.

Código inicial:
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
```

---

## p19 — 200. Number of Islands (Média)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p19.py

Dada uma grade `grid` de m x n, em que '1' representa terra e '0' representa água, retorne o número de ilhas. Uma ilha é formada por terras conectadas na horizontal ou na vertical e é cercada por água. Considere que todas as bordas da grade são cercadas por água. Os valores da grade são strings ('1' e '0').

Exemplos:
- grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]] → 1
- grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]] → 3

Restrições: 1 <= m, n <= 300; grid[i][j] é '0' ou '1'.

Código inicial:
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
```

---

## p20 — 322. Coin Change (Média)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p20.py

Dado um array `coins` com valores de moedas e um inteiro `amount` com um valor total, retorne o menor número de moedas necessário para formar esse valor. Se não for possível, retorne -1. Há quantidade ilimitada de cada moeda.

Exemplos:
- coins = [1,2,5], amount = 11 → 3 (5 + 5 + 1)
- coins = [2], amount = 3 → -1
- coins = [1], amount = 0 → 0

Restrições: 1 <= len(coins) <= 12; 1 <= coins[i] <= 2^31 - 1; 0 <= amount <= 10^4.

Código inicial:
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
```

---

## p21 — 4. Median of Two Sorted Arrays (Difícil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p21.py

Dados dois arrays ordenados `nums1` e `nums2`, de tamanhos m e n, retorne a mediana dos dois arrays combinados. A complexidade de tempo deve ser O(log(m + n)).

Exemplos:
- nums1 = [1,3], nums2 = [2] → 2.00000
- nums1 = [1,2], nums2 = [3,4] → 2.50000

Restrições: 0 <= m, n <= 1000; 1 <= m + n <= 2000; -10^6 <= nums1[i], nums2[i] <= 10^6.

Código inicial:
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
```

---

## p22 — 10. Regular Expression Matching (Difícil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p22.py

Dada uma string `s` e um padrão `p`, implemente a correspondência de expressões regulares com suporte a '.' e '*': '.' corresponde a qualquer caractere único; '*' corresponde a zero ou mais ocorrências do elemento anterior. A correspondência deve cobrir a string inteira, não apenas uma parte.

Exemplos:
- s = "aa", p = "a" → false
- s = "aa", p = "a*" → true
- s = "ab", p = ".*" → true

Restrições: 1 <= len(s) <= 20; 1 <= len(p) <= 20; s contém apenas letras minúsculas; p contém apenas letras minúsculas, '.' e '*'; todo '*' é precedido por um caractere válido.

Código inicial:
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        
```

---

## p23 — 23. Merge k Sorted Lists (Difícil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p23.py

Você recebe um array `lists` com k listas ligadas, cada uma ordenada em ordem crescente. Junte todas em uma única lista ligada ordenada e retorne sua cabeça.

Exemplos:
- lists = [[1,4,5],[1,3,4],[2,6]] → [1,1,2,3,4,4,5,6]
- lists = [] → []
- lists = [[]] → []

Restrições: 0 <= k <= 10^4; cada lista tem de 0 a 500 nós; -10^4 <= valor <= 10^4; cada lista está em ordem crescente; o total de nós não passa de 10^4.

Código inicial:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
```

---

## p24 — 32. Longest Valid Parentheses (Difícil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p24.py

Dada uma string `s` contendo apenas '(' e ')', retorne o comprimento da maior substring de parênteses válidos (bem formados).

Exemplos:
- s = "(()" → 2 ("()")
- s = ")()())" → 4 ("()()")
- s = "" → 0

Restrições: 0 <= len(s) <= 3 * 10^4; s[i] é '(' ou ')'.

Código inicial:
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
```

---

## p25 — 41. First Missing Positive (Difícil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p25.py

Dado um array de inteiros não ordenado `nums`, retorne o menor inteiro positivo que não está presente em `nums`. O algoritmo deve rodar em tempo O(n) e usar espaço extra O(1).

Exemplos:
- nums = [1,2,0] → 3
- nums = [3,4,-1,1] → 2
- nums = [7,8,9,11,12] → 1

Restrições: 1 <= len(nums) <= 10^5; -2^31 <= nums[i] <= 2^31 - 1.

Código inicial:
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
```

---

## p26 — 42. Trapping Rain Water (Difícil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p26.py

Dados n inteiros não negativos representando um mapa de elevação, em que cada barra tem largura 1, calcule quanta água da chuva fica acumulada entre as barras.

Exemplos:
- height = [0,1,0,2,1,0,1,3,2,1,2,1] → 6
- height = [4,2,0,3,2,5] → 9

Restrições: 1 <= n <= 2 * 10^4; 0 <= height[i] <= 10^5.

Código inicial:
class Solution:
    def trap(self, height: List[int]) -> int:
        
```

---

## p27 — 51. N-Queens (Difícil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p27.py

O problema das n rainhas consiste em posicionar n rainhas em um tabuleiro de xadrez n x n de forma que nenhuma rainha ataque outra (nenhuma pode estar na mesma linha, coluna ou diagonal). Dado `n`, retorne todas as soluções distintas, em qualquer ordem. Cada solução é uma lista de strings representando o tabuleiro, em que 'Q' é uma rainha e '.' é uma casa vazia.

Exemplos:
- n = 4 → [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
- n = 1 → [["Q"]]

Restrições: 1 <= n <= 9.

Código inicial:
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
```

---

## p28 — 76. Minimum Window Substring (Difícil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p28.py

Dadas duas strings `s` (tamanho m) e `t` (tamanho n), retorne a menor substring de `s` que contenha todos os caracteres de `t`, incluindo repetições. Se não existir, retorne "". Os casos de teste garantem que a resposta, quando existe, é única.

Exemplos:
- s = "ADOBECODEBANC", t = "ABC" → "BANC"
- s = "a", t = "a" → "a"
- s = "a", t = "aa" → ""

Restrições: 1 <= m, n <= 10^5; s e t contêm letras maiúsculas e minúsculas do inglês. Desafio: resolver em O(m + n).

Código inicial:
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
```

---

## p29 — 84. Largest Rectangle in Histogram (Difícil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p29.py

Dado um array `heights` com as alturas das barras de um histograma, em que cada barra tem largura 1, retorne a área do maior retângulo que cabe no histograma.

Exemplos:
- heights = [2,1,5,6,2,3] → 10
- heights = [2,4] → 4

Restrições: 1 <= len(heights) <= 10^5; 0 <= heights[i] <= 10^4.

Código inicial:
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
```

---

## p30 — 239. Sliding Window Maximum (Difícil)

```text
Resolva o problema a seguir em Python 3.
Use exatamente a assinatura fornecida.
Responda apenas com o código, sem explicações.
Não execute nem teste o código e não pesquise na internet. Apenas salve a solução em solucoes/gemini/p30.py

Dado um array de inteiros `nums` e uma janela deslizante de tamanho `k` que se move da esquerda para a direita, uma posição por vez, retorne um array com o valor máximo de cada posição da janela. Só é possível ver os k números dentro da janela.

Exemplos:
- nums = [1,3,-1,-3,5,3,6,7], k = 3 → [3,3,5,5,6,7]
- nums = [1], k = 1 → [1]

Restrições: 1 <= len(nums) <= 10^5; -10^4 <= nums[i] <= 10^4; 1 <= k <= len(nums).

Código inicial:
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
```
