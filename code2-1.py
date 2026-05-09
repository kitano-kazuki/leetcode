class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n <= 0:
            raise ValueError("n must be > 0")
        
        # k > n行目のシンボル数
        if k > 2 ** (n - 1):
            raise ValueError("k must be less than the number of symbols in the row")

        is_reverse = False
        row = n
        col = k
        while row > 1:
            if col % 2 == 0:
                is_reverse = not is_reverse
            row = row - 1
            col = (col + 1) // 2
        
        if is_reverse:
            return 1
        else:
            return 0
        