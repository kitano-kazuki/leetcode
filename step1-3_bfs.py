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
        
        depth = 0
        frontier = deque()
        frontier.append(root)
        while frontier:
            num_cur_frontier = len(frontier)
            depth += 1
            for _ in range(num_cur_frontier):
                node = frontier.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left is not None:
                    frontier.append(node.left)
                if node.right is not None:
                    frontier.append(node.right)
        
        raise ValueError()
        