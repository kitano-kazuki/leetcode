class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # NOTE:
        # * Each column has the same value
        # * i-th row has 2^(i - 1) elements
        # * the first 2^(i - 2) element is the reverse of the rest
        # * track the k-th element in the final row

        reverse = False
        half_length = 2 ** (n - 2)
        while k != 1:
            if k > half_length:
                k = k - half_length
                reverse = not reverse
            half_length = half_length / 2

        if reverse:
            return 1

        return 0
