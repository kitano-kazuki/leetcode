from typing import List
import copy

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_copy = copy.deepcopy(grid)
        m = len(grid_copy)
        n = len(grid_copy[0])
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        def rewrite_1_to_0_and_recur_adjacents(r: int, c: int) -> None:
            grid_copy[r][c] = "0"
            for dr, dc in dirs:
                next_r = r + dr
                next_c = c + dc
                if next_r < 0 or next_r >= m or next_c < 0 or next_c >= n:
                    continue
                if grid_copy[next_r][next_c] == "0":
                    continue
                rewrite_1_to_0_and_recur_adjacents(next_r, next_c)
        
        count = 0
        for r in range(m):
            for c in range(n):
                if grid_copy[r][c] == "1":
                    count += 1
                    rewrite_1_to_0_and_recur_adjacents(r, c)
        
        return count
                