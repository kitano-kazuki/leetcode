class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        abs_n = abs(n)

        selection_bit = 0b1
        powed_x = x
        result = 1
        while selection_bit <= abs_n:
            if selection_bit & abs_n > 0:
                result *= powed_x
            powed_x = powed_x * powed_x
            selection_bit = selection_bit << 1
        
        if n < 0:
            result = 1. / result
        
        return result
