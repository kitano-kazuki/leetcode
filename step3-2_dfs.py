# 1st: 3:27
# 2nd: 1:13
# 3rd: 1:17


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
        node_to_visit = [(root, targetSum)]
        while node_to_visit:
            node, target_sum_at_this_node = node_to_visit.pop()
            is_leaf = node.left is None and node.right is None
            if is_leaf and node.val == target_sum_at_this_node:
                return True
            if node.left is not None:
                node_to_visit.append((node.left, target_sum_at_this_node - node.val))
            if node.right is not None:
                node_to_visit.append((node.right, target_sum_at_this_node - node.val))
        return False