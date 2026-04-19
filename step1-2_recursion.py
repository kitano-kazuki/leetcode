# solved: 2:53
import functools


class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        @functools.cache
        def max_profit_with_state(day: int, has_stock: bool) -> int:
            if day == len(prices) - 1:
                return prices[day] if has_stock else 0

            if has_stock:
                return max(
                    prices[day] + max_profit_with_state(day + 1, False),
                    max_profit_with_state(day + 1, True)
                )
            
            return max(
                -prices[day] + max_profit_with_state(day + 1, True),
                max_profit_with_state(day + 1, False)
            )

        return max_profit_with_state(0, False)