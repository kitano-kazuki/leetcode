from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        frontier = deque()
        frontier.append(root)
        depth = 0
        while frontier:
            num_cur_frontiers = len(frontier)
            depth += 1
            for _ in range(num_cur_frontiers):
                node = frontier.popleft()
                if node is None:
                    continue
                frontier.append(node.left)
                frontier.append(node.right)
        
        return depth