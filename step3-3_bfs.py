# 1st: 1:54
# 2nd: 1:39
# 3rd: 1:26


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False
        frontier = [(root, targetSum)]
        while frontier:
            next_level_frontier = []
            while frontier:
                node, target_sum_at_this_node = frontier.pop()
                is_leaf = node.left is None and node.right is None
                if is_leaf and node.val == target_sum_at_this_node:
                    return True
                if node.left is not None:
                    next_level_frontier.append((node.left, target_sum_at_this_node - node.val))
                if node.right is not None:
                    next_level_frontier.append((node.right, target_sum_at_this_node - node.val))
            frontier = next_level_frontier
        return False