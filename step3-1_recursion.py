# 1st 2:10

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

        def minDepth_helper(node: TreeNode) -> int:
            if node.left is None and node.right is None:
                return 1
            if node.left is None:
                return minDepth_helper(node.right) + 1
            if node.right is None:
                return minDepth_helper(node.left) + 1
            return min(minDepth_helper(node.left), minDepth_helper(node.right)) + 1

        return minDepth_helper(root)
        