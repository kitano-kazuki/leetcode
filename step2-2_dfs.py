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
        
        frontier = [(root, 1)]
        minimum_depth = float("inf")
        while frontier:
            node, depth = frontier.pop()
            if node.left is None and node.right is None:
                minimum_depth = min(minimum_depth, depth)
                continue
            if node.left is not None:
                frontier.append((node.left, depth + 1))
            if node.right is not None:
                frontier.append((node.right, depth + 1))
        return minimum_depth