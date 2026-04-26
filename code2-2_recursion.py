import functools


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        @functools.cache
        def calc_minimum_num_coins(amount: int) -> int:
            if amount < 0:
                return -1
            if amount == 0:
                return 0

            # 「(総額 - コインの額)を作るのに必要な最小枚数」+ 1 の最小値を計算
            minimum_num_coins = float("inf")
            for coin in coins:
                num_coins = calc_minimum_num_coins(amount - coin)
                if num_coins == -1:
                    continue
                minimum_num_coins = min(minimum_num_coins, num_coins + 1)
            
            # float("inf")は特殊な値なので, ==の比較が正しく動作する
            # IEEE754 - https://tmytokai.github.io/open-ed/activity/fpoint/text03/page02.html
            if minimum_num_coins == float("inf"):
                return -1
            return minimum_num_coins

        return calc_minimum_num_coins(amount)
