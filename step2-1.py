class Solution:
    def myPow(self, x: float, n: int) -> float:

        def mypow_helper(x: float, n: int) -> float:
            if n == 0:
                return 1
            if n == 1:
                return x

            half_powed = mypow_helper(x, n // 2)
            if n % 2 == 0:
                return half_powed * half_powed
            else:
                return half_powed * half_powed * x
        
        is_negative = x < 0 and n % 2 == 1
        reverse = n < 0

        powed_value = mypow_helper(abs(x), abs(n))

        if reverse:
            powed_value = 1 / powed_value

        if is_negative:
            powed_value = -1 * powed_value
        
        return powed_value
