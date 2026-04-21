class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        profit = 0
        for i in range(len(prices)):
            yesterday_price = prices[i - 1] if i - 1 >= 0 else float("inf")
            today_price = prices[i]
            tomorrow_price = prices[i + 1] if i + 1 < len(prices) else float("-inf")
            if yesterday_price <= today_price and today_price <= tomorrow_price:
                continue
            if yesterday_price <= today_price and today_price > tomorrow_price:
                profit += today_price
                continue
            if yesterday_price > today_price and today_price <= tomorrow_price:
                profit -= today_price
                continue

        return profit