# solved: 5:10

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        patterns = [[0] * (n + 1) for _ in range(m + 1)]
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if row == 1 and col == 1:
                    patterns[row][col] = 1
                    continue
                patterns[row][col] = patterns[row - 1][col] + patterns[row][col - 1]
        return patterns[m][n]