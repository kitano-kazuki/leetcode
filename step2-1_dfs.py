from typing import List
from collections import defaultdict

class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        node_to_neighbors = defaultdict(set)
        for edge in edges:
            node_to_neighbors[edge[0]].add(edge[1])
            node_to_neighbors[edge[1]].add(edge[0])

        visited = [False] * n

        def visit_connected_nodes(init_node):
            frontier = [init_node]
            while frontier:
                node = frontier.pop()
                if visited[node]:
                    continue
                visited[node] = True
                for neighbor_node in node_to_neighbors[node]:
                    if not visited[neighbor_node]:
                        frontier.append(neighbor_node)
            return

        num_components = 0
        for i in range(n):
            if visited[i]:
                continue
            num_components += 1
            visit_connected_nodes(i)
        return num_components