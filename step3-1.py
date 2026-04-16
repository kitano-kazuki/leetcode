# 1st: 4:00
# 2nd: 2:01
# 3rd: 1:29

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        unique_paths = [0] * n
        for _ in range(m):
            unique_paths_next = [0] * n
            unique_paths_next[0] = 1
            for column in range(1, n):
                unique_paths_next[column] = unique_paths[column] + unique_paths_next[column - 1]
            unique_paths = unique_paths_next
        return unique_paths[-1]
                