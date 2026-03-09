from typing import List

class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.rank = [0] * size
    
    def find(self, idx):
        if self.parents[idx] != idx:
            self.parents[idx] = self.find(self.parents[idx])
        return self.parents[idx]
    
    def union(self, idx1, idx2):
        parent1 = self.find(idx1)
        parent2 = self.find(idx2)
        if parent1 == parent2:
            return
        if self.rank[parent1] < self.rank[parent2]:
            self.parents[parent1] = parent2
            return
        if self.rank[parent2] < self.rank[parent1]:
            self.parents[parent2] = parent1
            return
        self.parents[parent2] = parent1
        self.rank[parent1] += 1
        return
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for edge in  edges:
            uf.union(edge[0], edge[1])
        
        seen_parent = set()
        num_components = 0
        for node in range(n):
            parent = uf.find(node)
            if parent in seen_parent:
                continue
            seen_parent.add(parent)
            num_components += 1
        return num_components
