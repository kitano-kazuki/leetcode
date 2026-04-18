from itertools import islice


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            raise ValueError("given array is empty")

        max_profit = 0
        min_price = prices[0]
        for price in islice(prices, 1, len(prices)):
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit