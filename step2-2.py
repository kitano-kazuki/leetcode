from collections import deque
import copy
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_copy = copy.deepcopy(grid)
        m = len(grid_copy)
        n = len(grid_copy[0])
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        def rewrite_island_to_sea(init_r: int, init_c: int) -> None:
            grid_copy[init_r][init_c] = "0"
            to_visit = deque()
            to_visit.append((init_r, init_c))
            while to_visit:
                r, c = to_visit.popleft()
                for dr, dc in dirs:
                    next_r = r + dr
                    next_c = c + dc
                    if next_r < 0 or next_r >= m or next_c < 0 or next_c >= n:
                        continue
                    if grid_copy[next_r][next_c] == "0":
                        continue
                    grid_copy[next_r][next_c] = "0"
                    to_visit.append((next_r, next_c))
            return

        count = 0
        for r in range(m):
            for c in range(n):
                if grid_copy[r][c] == "1":
                    count += 1
                    rewrite_island_to_sea(r, c)

        return count
