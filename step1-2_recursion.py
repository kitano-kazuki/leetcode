# solved: 7:57

from functools import cache


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        @cache
        def unique_paths_with_obstacles_helper(destination_row: int, destination_column: int) -> int:
            if destination_row < 0 or destination_column < 0:
                return 0

            OBSTACLE = 1
            if obstacleGrid[destination_row][destination_column] == OBSTACLE:
                return 0

            if destination_row == 0 and destination_column == 0:
                return 1

            return unique_paths_with_obstacles_helper(destination_row - 1, destination_column) + unique_paths_with_obstacles_helper(destination_row, destination_column - 1)

        return unique_paths_with_obstacles_helper(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)