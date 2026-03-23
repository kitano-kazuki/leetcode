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
        is_leaf = root.left is None and root.right is None
        if is_leaf and root.val == targetSum:
            return True
        next_targetSum = targetSum - root.val
        return self.hasPathSum(root.left, next_targetSum) or self.hasPathSum(root.right, next_targetSum)