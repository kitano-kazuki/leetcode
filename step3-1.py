from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        WATER = 0
        LAND = 1
        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

        def get_area_of_island(row, col):
            assert 0 <= row and row < num_rows
            assert 0 <= col and col < num_cols
            assert grid[row][col] == LAND
            assert not visited[row][col]

            area_size = 1
            visited[row][col] = True
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in dirs:
                next_row = row + dr
                next_col = col + dc
                if next_row < 0 or num_rows <= next_row:
                    continue
                if next_col < 0 or num_cols <= next_col:
                    continue
                if grid[next_row][next_col] == WATER:
                    continue
                if visited[next_row][next_col]:
                    continue
                area_size += get_area_of_island(next_row, next_col)
            return area_size

        max_area = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == WATER:
                    continue
                if visited[r][c]:
                    continue
                area = get_area_of_island(r, c)
                max_area = max(area, max_area)
        return max_area