# 1st: 2:46
# 2nd: 計測忘れ
# 3rd: 2:01
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        frontier = deque([root])
        is_left_to_right = True
        level_order_values = []
        while frontier:
            next_frontier = deque()
            values_at_this_level = []
            while frontier:
                node = frontier.popleft()
                values_at_this_level.append(node.val)
                if node.left is not None:
                    next_frontier.append(node.left)
                if node.right is not None:
                    next_frontier.append(node.right)
            if not is_left_to_right:
                values_at_this_level = list(reversed(values_at_this_level))
            level_order_values.append(values_at_this_level)
            is_left_to_right = not is_left_to_right
            frontier = next_frontier
        return level_order_values
