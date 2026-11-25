from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res: List[List[str]] = []
        cols = set()
        diag1 = set()
        diag2 = set()
        queens: List[int] = []

        def backtrack(row: int) -> None:
            if row == n:
                res.append(["." * col + "Q" + "." * (n - col - 1) for col in queens])
                return

            for col in range(n):
                d1 = row - col
                d2 = row + col
                if col in cols or d1 in diag1 or d2 in diag2:
                    continue

                cols.add(col)
                diag1.add(d1)
                diag2.add(d2)
                queens.append(col)

                backtrack(row + 1)

                queens.pop()
                cols.remove(col)
                diag1.remove(d1)
                diag2.remove(d2)

        backtrack(0)
        return res