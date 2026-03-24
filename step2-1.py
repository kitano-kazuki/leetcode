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
        level_zigzag_ordered_values = []
        is_right_to_left = False
        frontier = deque([(root)])
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
            if is_right_to_left:
                values_at_this_level = values_at_this_level[::-1]
            level_zigzag_ordered_values.append(values_at_this_level)
            frontier = next_frontier
            is_right_to_left = not is_right_to_left
        return level_zigzag_ordered_values
        