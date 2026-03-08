from typing import List
import copy

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        num_rows = len(grid)
        num_cols = len(grid[0])

        WATER = 0
        LAND = 1

        def calc_area_size_from_unvisited(row, col, visited):
            if row < 0 or num_rows <= row or col < 0 or num_cols <= col:
                return 0
            if grid[row][col] == WATER:
                return 0
            visited[row][col] = True
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            areas = 1
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
                areas += calc_area_size_from_unvisited(next_row, next_col, visited)
            return areas

        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]
        
        max_areas = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == WATER:
                    continue
                if not visited[r][c]:
                    area = calc_area_size_from_unvisited(r, c, visited)
                    max_areas = max(area, max_areas)

        return max_areas
                