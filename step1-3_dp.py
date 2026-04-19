class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        EMPTY_STOCK_STATE = 0
        HOLDING_STOCK_STATE = 1
        maximum_profit_from_today = [[None, None] for _ in range(len(prices))]
        maximum_profit_from_today[-1][EMPTY_STOCK_STATE] = 0
        maximum_profit_from_today[-1][HOLDING_STOCK_STATE] = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            maximum_profit_from_today[i][EMPTY_STOCK_STATE] = max(
                maximum_profit_from_today[i + 1][EMPTY_STOCK_STATE], 
                -prices[i] + maximum_profit_from_today[i + 1][HOLDING_STOCK_STATE]
            )
            maximum_profit_from_today[i][HOLDING_STOCK_STATE] = max(
                prices[i]  + maximum_profit_from_today[i + 1][EMPTY_STOCK_STATE],
                maximum_profit_from_today[i + 1][HOLDING_STOCK_STATE]
            )

        return maximum_profit_from_today[0][EMPTY_STOCK_STATE]
            