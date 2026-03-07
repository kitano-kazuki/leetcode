from collections import deque
import copy
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_copy = copy.deepcopy(grid)
        m = len(grid_copy)
        n = len(grid_copy[0])
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        def visit_adjacents(init_r: int, init_c: int) -> None:
            to_visit = deque()
            to_visit.append((init_r, init_c))
            while to_visit:
                r, c = to_visit.popleft()
                if r < 0 or r >= m or c < 0 or c >= n:
                    continue
                if grid_copy[r][c] == "0":
                    continue
                grid_copy[r][c] = "1"
                for dr, dc in dirs:
                    to_visit.append((r + dr, c + dc))
            return

        count = 0
        for r in range(m):
            for c in range(n):
                if grid_copy[r][c] == "1":
                    count += 1
                    visit_adjacents(r, c)

        return count
