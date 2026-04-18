from enum import Enum
from functools import cache

class State(Enum):
    EMPTY = 0
    HOLD = 1


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        @cache
        def max_profit_with_state(day: int, state: State) -> int:
            if day == len(prices):
                return 0
                
            if state == State.EMPTY:
                return max(
                    max_profit_with_state(day + 1, State.EMPTY),
                    -prices[day] + max_profit_with_state(day + 1, State.HOLD)
                )
            if state == State.HOLD:
                return max(
                    max_profit_with_state(day + 1, State.HOLD),
                    prices[day]
                )
        
        return max_profit_with_state(0, State.EMPTY)