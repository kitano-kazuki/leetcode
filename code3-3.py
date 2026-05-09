class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        abs_n = abs(n)

        # nの各bitごとにx^(2^k)を乗算
        # n = 5(0b101) -> x^(2^0 * 1 + 2^1 * 0 + 2^2 * 1) = x^(2^0) * x^(2^2)
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
                