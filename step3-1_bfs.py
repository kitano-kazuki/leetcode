# 1st: 2:05
# 2nd: 1:40

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
        frontier = deque([root])
        level_ordered_values = []
        while frontier:
            next_frontier = deque([])
            values_at_this_level = []
            while frontier:
                node = frontier.popleft()
                values_at_this_level.append(node.val)
                if node.left is not None:
                    next_frontier.append(node.left)
                if node.right is not None:
                    next_frontier.append(node.right)
            level_ordered_values.append(values_at_this_level)
            frontier = next_frontier
        return level_ordered_values