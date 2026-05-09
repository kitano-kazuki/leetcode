
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n *= -1

        multiplier = 1
        while n > 1:
            if n % 2 == 1:
                multiplier *= x
            x = x * x
            n = n // 2

        x *= multiplier

        return x

