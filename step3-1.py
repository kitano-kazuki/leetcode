from typing import List
import copy

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_copy = copy.deepcopy(grid)
        num_rows = len(grid)
        num_cols = len(grid[0])

        LAND = "1"
        WATER = "0"

        def rewrite_land_to_water_and_recur_adjacent(row: int, col: int) -> None:
            if row < 0 or num_rows <= row or col < 0 or num_cols <= col:
                return
            if grid_copy[row][col] == WATER:
                return

            grid_copy[row][col] = WATER
            dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]
            for dr, dc in dirs:
                adj_row = row + dr
                adj_col = col + dc
                if adj_row < 0 or num_rows <= adj_row or adj_col < 0 or num_cols <= adj_col:
                    continue
                if grid_copy[adj_row][adj_col] == WATER:
                    continue
                rewrite_land_to_water_and_recur_adjacent(adj_row, adj_col)

        num_islands = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid_copy[r][c] == WATER:
                    continue
                num_islands += 1
                rewrite_land_to_water_and_recur_adjacent(r, c)

        return num_islands
                
