# 1st: 1:30
from typing import Optional
from copy import deepcopy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return deepcopy(root2)
        if root2 is None:
            return deepcopy(root1)
        
        merged_node = TreeNode(root1.val + root2.val)
        merged_node.left = self.mergeTrees(root1.left, root2.left)
        merged_node.right = self.mergeTrees(root1.right, root2.right)
        return merged_node