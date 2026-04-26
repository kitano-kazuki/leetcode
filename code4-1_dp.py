class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0

        min_num_coins = [0] + [float("inf")] * amount
        for target in range(amount + 1):
            if min_num_coins[target] == float("inf"):
                continue
            for coin in coins:
                if target + coin > amount:
                    continue
                min_num_coins[target + coin] = min(
                    min_num_coins[target + coin],
                    min_num_coins[target] + 1
                )
            
        if min_num_coins[amount] == float("inf"):
            return -1
        return min_num_coins[amount]
                