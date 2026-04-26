class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0

        # amount以下の金額それぞれで必要な最小コイン枚数を計算
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
        
        # float("inf")は特殊な値なので, ==の比較が正しく動作する
        # IEEE754 - https://tmytokai.github.io/open-ed/activity/fpoint/text03/page02.html
        if min_num_coins[amount] == float("inf"):
            return -1
        return min_num_coins[amount]
