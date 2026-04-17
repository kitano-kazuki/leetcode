# solved: 10:22
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        SPACE = 0
        OBSTACLE = 1

        if obstacleGrid[0][0] == OBSTACLE:
            return 0

        previous_unique_paths = [0] * n
        previous_unique_paths[0] = 1
        for row in range(m):
            unique_paths = [0] * n
            for column in range(n):
                if obstacleGrid[row][column] == OBSTACLE:
                    unique_paths[column] = 0
                else:
                    unique_paths[column] = previous_unique_paths[column] + (unique_paths[column - 1] if column > 0 else 0)
            previous_unique_paths = unique_paths

        return previous_unique_paths[-1]