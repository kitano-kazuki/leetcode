# solved: 6:47

class Solution:
    def num_ways(self, n: int, k: int) -> int:
        if n == 1:
            return k

        patterns_same_color = [0] * n
        patterns_different_color = [0] * n

        patterns_same_color[0] = 0
        patterns_different_color[0] = k
        for i in range(1, n):
            patterns_same_color[i] = patterns_different_color[i - 1]
            patterns_different_color[i] = patterns_same_color[i - 1] * (k - 1) + patterns_different_color[i - 1] * (k - 1)
        
        return patterns_same_color[n - 1] + patterns_different_color[n - 1]
