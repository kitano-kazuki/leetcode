# solved: 14:56
import enum


class Solution:

    class _GradientState(enum.Enum):
        SLOPE = 0
        VALLEY = 1
        EDGE = 2
        
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        def _calculate_gradient_state(array: list[int], index: int) -> Solution._GradientState:
            left_height = array[index - 1] if index - 1 >= 0 else float("inf")
            right_height = array[index + 1] if index + 1 < len(array) else float("-inf")
            if left_height < array[index] < right_height or left_height > array[index] > right_height:
                return Solution._GradientState.SLOPE
            if left_height >= array[index] and array[index] < right_height:
                return Solution._GradientState.VALLEY
            if left_height < array[index] and array[index] >= right_height:
                return Solution._GradientState.EDGE
            assert True, "unreachable"

        profit = 0
        for i in range(len(prices)):
            gradient_state = _calculate_gradient_state(prices, i)
            if gradient_state == Solution._GradientState.SLOPE:
                continue
            if gradient_state == Solution._GradientState.VALLEY:
                profit -= prices[i]
                continue
            if gradient_state == Solution._GradientState.EDGE:
                profit += prices[i]
                continue
        
        return profit
            