from typing import List
import copy

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_copy = copy.deepcopy(grid)
        m = len(grid_copy)
        n = len(grid_copy[0])
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        def visit_adjacents(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if grid_copy[r][c] == "0":
                return
            grid_copy[r][c] = "0"
            for dr, dc in dirs:
                next_r = r + dr
                next_c = c + dc
                visit_adjacents(next_r, next_c)
        
        count = 0
        for r in range(m):
            for c in range(n):
                if grid_copy[r][c] == "1":
                    count += 1
                    visit_adjacents(r, c)
        
        return count
                
            
        

