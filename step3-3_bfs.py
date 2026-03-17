# 1st 2:44
# 2nd 1:23
# 3rd 1:32

from typing import Optional
from collections import deque


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

        frontier = deque([root])
        current_depth = 1
        while True:
            next_frontier = deque()
            while frontier:
                node = frontier.popleft()
                if node.left is None and node.right is None:
                    return current_depth
                if node.left is not None:
                    next_frontier.append(node.left)
                if node.right is not None:
                    next_frontier.append(node.right)
            frontier = next_frontier
            current_depth += 1
