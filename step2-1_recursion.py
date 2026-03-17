from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def helper_minDepth(node: TreeNode) -> int:
            if node.left is None and node.right is None:
                return 1
            if node.left is None:
                return helper_minDepth(node.right) + 1
            if node.right is None:
                return helper_minDepth(node.left) + 1
            return min(helper_minDepth(node.left), helper_minDepth(node.right)) + 1
        
        return helper_minDepth(root)