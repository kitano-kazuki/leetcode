from typing import List

class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def create_adjacent_matrix():
            adjacent_matrix = [[False] * n for _ in range(n)]
            for edge in edges:
                node1 = edge[0]
                node2 = edge[1]
                adjacent_matrix[node1][node2] = True
                adjacent_matrix[node2][node1] = True
            return adjacent_matrix
        
        def visit_all_connected_nodes(cur_node, adj_matrix, visited):
            if visited[cur_node]:
                return
            visited[cur_node] = True
            for next_node in range(n):
                if cur_node == next_node:
                    continue
                if not adj_matrix[cur_node][next_node]:
                    continue
                visit_all_connected_nodes(next_node, adj_matrix, visited)
            return

        visited = [False] * n
        adj_matrix = create_adjacent_matrix()
        num_components = 0
        for i in range(n):
            if visited[i]:
                continue
            num_components += 1
            visit_all_connected_nodes(i, adj_matrix, visited)
        return num_components