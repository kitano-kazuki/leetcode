# 1st: 1:29
# 2nd: 1:32
# 3rd: 1:16

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        node_and_valid_bounds = [(root, float("-inf"), float("inf"))]
        while node_and_valid_bounds:
            node, lower_bound_exclusive, upper_bound_exclusive = node_and_valid_bounds.pop()
            if not (lower_bound_exclusive < node.val < upper_bound_exclusive):
                return False
            if node.left is not None:
                node_and_valid_bounds.append((node.left, lower_bound_exclusive, node.val))
            if node.right is not None:
                node_and_valid_bounds.append((node.right, node.val, upper_bound_exclusive))
        return True