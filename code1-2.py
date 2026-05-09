class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n *= -1

        def my_pow_helper(x: float, n: int) -> float:
            if n == 1:
                return x

            if n % 2 == 0:
                return my_pow_helper(x * x, n // 2)
            else:
                return my_pow_helper(x * x, n // 2) * x

        return my_pow_helper(x, n)
    
