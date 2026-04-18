class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # max_price[i]: maximum price of prices[i:]
        max_price = [None] * len(prices)
        for i in range(len(prices) - 1, -1, -1):
            if i == len(prices) - 1:
                max_price[i] = prices[i]
            else:
                max_price[i] = max(prices[i], max_price[i + 1])

        max_profit = 0
        for i in range(len(prices) - 1):
            if max_price[i + 1] <= prices[i]:
                continue
            max_profit = max(max_profit, max_price[i + 1] - prices[i])
        
        return max_profit
