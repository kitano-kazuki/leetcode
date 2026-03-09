from typing import List
from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        node_to_neighbors = defaultdict(set)
        for edge in edges:
            node_to_neighbors[edge[0]].add(edge[1])
            node_to_neighbors[edge[1]].add(edge[0])
        
        visited = [False] * n

        def visit_connected(init_node):
            if visited[init_node]:
                return
            frontier = [init_node]
            while frontier:
                node = frontier.pop()
                if visited[node]:
                    continue
                visited[node] = True
                for neighbor_node in node_to_neighbors[node]:
                    if visited[neighbor_node]:
                        continue
                    frontier.append(neighbor_node)
        
        num_components = 0
        for node in range(n):
            if visited[node]:
                continue
            num_components += 1
            visit_connected(node)

        return num_components
