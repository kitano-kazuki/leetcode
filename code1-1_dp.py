class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount < 0:
            return -1

        if amount == 0:
            return 0

        min_coins = [0] + [None] * (amount)
        for target in range(amount + 1):
            if min_coins[target] is None:
                continue
            for coin in coins:
                if target + coin > amount:
                    continue
                if min_coins[target + coin] is None or min_coins[target] + 1 < min_coins[target + coin]:
                    min_coins[target + coin] = min_coins[target] + 1
        
        if min_coins[amount] is None:
            return -1
        return min_coins[amount]
