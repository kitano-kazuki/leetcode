class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        estate_with_stock = [None] * len(prices)
        estate_without_stock = [None] * len(prices)

        estate_with_stock[0] = -prices[0]
        estate_without_stock[0] = 0

        for i in range(1, len(prices)):
            estate_with_stock[i] = max(
                estate_with_stock[i - 1],
                estate_without_stock[i - 1] - prices[i]
            )
            estate_without_stock[i] = max(
                estate_with_stock[i - 1] + prices[i],
                estate_without_stock[i - 1]
            )
        
        return estate_without_stock[-1]
