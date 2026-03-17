# 1st 2:16

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
        min_depth = float("inf")
        while frontier:
            node, distance = frontier.pop()
            if node.left is None and node.right is None:
                min_depth = min(min_depth, distance)
                continue
            if node.left is not None:
                frontier.append((node.left, distance + 1))
            if node.right is not None:
                frontier.append((node.right, distance + 1))
        return min_depth