from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        node_chunks_by_level = []
        frontier = deque([(root)])
        while frontier:
            next_level_frontier = deque([])
            nodes_at_this_level = []
            while frontier:
                node = frontier.popleft()
                nodes_at_this_level.append(node.val)
                if node.left is not None:
                    next_level_frontier.append(node.left)
                if node.right is not None:
                    next_level_frontier.append(node.right)
            frontier = next_level_frontier
            node_chunks_by_level.append(nodes_at_this_level)
        return node_chunks_by_level
