from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        node = root
        frontier = [(node, 1)]
        maximum_depth = 0
        while frontier:
            node, depth = frontier.pop()
            if node is None:
                continue
            maximum_depth = max(maximum_depth, depth)
            frontier.append((node.left, depth + 1))
            frontier.append((node.right, depth + 1))
        
        return maximum_depth