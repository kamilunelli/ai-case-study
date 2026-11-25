from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for a in range(coin, amount + 1):
                candidate = dp[a - coin] + 1
                if candidate < dp[a]:
                    dp[a] = candidate

        return dp[amount] if dp[amount] <= amount else -1