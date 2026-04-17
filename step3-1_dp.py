# 1st: 3:30
# 2nd: 2:28
# 3rd: 2:06

OBSTACLE = 1

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        num_rows = len(obstacleGrid)
        num_columns = len(obstacleGrid[0])

        if obstacleGrid[0][0] == OBSTACLE or obstacleGrid[num_rows - 1][num_columns - 1] == OBSTACLE:
            return 0

        previous_unique_paths = [1] + [0] * (num_columns - 1)
        for r in range(num_rows):
            unique_paths = [None] * num_columns
            for c in range(num_columns):
                if obstacleGrid[r][c] == OBSTACLE:
                    unique_paths[c] = 0
                    continue
                unique_paths[c] = previous_unique_paths[c] + (unique_paths[c - 1] if c > 0 else 0)
            previous_unique_paths = unique_paths
        
        return previous_unique_paths[-1]
            