from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.ranks = [1] * size
    
    def find(self, idx):
        if self.parents[idx] == idx:
            return idx
        parent = self.find(self.parents[idx])
        self.parents[idx] = parent
        return parent
    
    def union(self, idx1, idx2):
        parent1 = self.find(idx1)
        parent2 = self.find(idx2)
        if self.ranks[parent1] < self.ranks[parent2]:
            self.parents[parent1] = parent2
        elif self.ranks[parent1] > self.ranks[parent2]:
            self.parents[parent2] = parent1
        else:
            self.parents[parent2] = parent1
            self.ranks[parent1] += 1
        return

    def is_root(self, idx):
        if self.find(idx) == idx:
            return True
        return False


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        calc_flatten_idx = lambda row, col : row * num_cols + col
        num_elements = num_rows * num_cols
        uf = UnionFind(num_elements)
        for r in range(num_rows):
            for c in range(num_cols):
                if r + 1 < num_rows:
                    if grid[r][c] == "1" and grid[r + 1][c] == "1":
                        uf.union(calc_flatten_idx(r, c), calc_flatten_idx(r + 1, c))
                if c + 1 < num_cols:
                    if grid[r][c] == "1" and grid[r][c + 1] == "1":
                        uf.union(calc_flatten_idx(r, c), calc_flatten_idx(r, c + 1))
        num_islands = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1" and uf.is_root(calc_flatten_idx(r, c)):
                    num_islands += 1
        return num_islands