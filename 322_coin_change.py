from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        pattern = [-1] * ( amount + 1)
        pattern[0] = 0


        for i in range(1, amount + 1):
            for coin in coins:
                target = i - coin
                if target >= 0 and pattern[target] != -1:
                    num = pattern[target] + 1
                    if pattern[i] == -1 or num < pattern[i]:
                        pattern[i] = num
        return pattern[amount]


COINS = [1, 3, 5]
AMOUNT = 11
solution = Solution()
RESULT = solution.coinChange(COINS, AMOUNT)
print(RESULT)
