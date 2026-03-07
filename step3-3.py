from typing import List

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size
    
    def find(self, idx):
        if self.parent[idx] == idx:
            return idx
        parent_idx = self.find(self.parent[idx])
        self.parent[idx] = parent_idx
        return parent_idx
    
    def union(self, idx1, idx2):
        parent_idx1 = self.find(idx1)
        parent_idx2 = self.find(idx2)
        if parent_idx1 == parent_idx2:
            return
        
        if self.rank[parent_idx1] < self.rank[parent_idx2]:
            self.parent[parent_idx1] = parent_idx2
            return
        elif self.rank[parent_idx2] < self.rank[parent_idx1]:
            self.parent[parent_idx2] = parent_idx1
            return
        else:
            self.parent[parent_idx2] = parent_idx1
            self.rank[parent_idx1] += 1
            return

    def is_root(self, idx):
        return self.parent[idx] == idx

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        WATER = "0"
        LAND = "1"

        uf = UnionFind(num_rows * num_cols)

        flatten_row_col = lambda row, col : row * num_cols + col

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == WATER:
                    continue
                if r + 1 < num_rows and grid[r + 1][c] == LAND:
                    uf.union(flatten_row_col(r, c), flatten_row_col(r + 1, c))
                if c + 1 < num_cols and grid[r][c + 1] == LAND:
                    uf.union(flatten_row_col(r, c), flatten_row_col(r, c + 1))
        
        num_islands = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == WATER:
                    continue
                if uf.is_root(flatten_row_col(r, c)):
                    num_islands += 1
        
        return num_islands