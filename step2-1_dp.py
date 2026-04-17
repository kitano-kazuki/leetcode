
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        num_rows = len(obstacleGrid)
        num_columns = len(obstacleGrid[0])
        OBSTACLE = 1

        if obstacleGrid[0][0] == OBSTACLE:
            return 0

        previous_unique_paths = [0] * num_columns
        previous_unique_paths[0] = 1
        for row in range(num_rows):
            unique_paths = [0] * num_columns
            for column in range(num_columns):
                if obstacleGrid[row][column] == OBSTACLE:
                    unique_paths[column] = 0
                else:
                    unique_paths[column] = previous_unique_paths[column] + (unique_paths[column - 1] if column > 0 else 0)
            previous_unique_paths = unique_paths

        return previous_unique_paths[-1]