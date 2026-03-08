from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        WATER = 0
        LAND = 1
        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

        def get_area_of_island(row, col):
            assert not visited[row][col]
            to_visit = [(row, col)]
            area_size = 0
            while to_visit:
                r, c = to_visit.pop()
                if visited[r][c]:
                    continue
                visited[r][c] = True
                area_size += 1
                dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dr, dc in dirs:
                    next_r = r + dr
                    next_c = c + dc
                    if next_r < 0 or num_rows <= next_r:
                        continue
                    if next_c < 0 or num_cols <= next_c:
                        continue
                    if grid[next_r][next_c] == WATER:
                        continue
                    if visited[next_r][next_c]:
                        continue
                    to_visit.append((next_r, next_c))
            return area_size
                
        maximum_area = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == WATER:
                    continue
                if visited[r][c]:
                    continue
                area = get_area_of_island(r, c)
                maximum_area = max(area, maximum_area)
        return maximum_area