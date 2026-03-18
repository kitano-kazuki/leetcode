from typing import Optional
from collections import deque
from copy import deepcopy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return deepcopy(root2)
        if root2 is None:
            return deepcopy(root1)

        dummy_merged_root = TreeNode()
        frontier = deque([(root1, root2, dummy_merged_root, "left")])
        while frontier:
            next_frontier = deque()
            while frontier:
                node1, node2, target_node, creation_side = frontier.popleft()
                if node1 is None and node2 is None:
                    continue
                if node1 is None:
                    if creation_side == "left":
                        target_node.left = deepcopy(node2)
                        continue
                    if creation_side == "right":
                        target_node.right = deepcopy(node2)
                        continue
                if node2 is None:
                    if creation_side == "left":
                        target_node.left = deepcopy(node1)
                        continue
                    if creation_side == "right":
                        target_node.right = deepcopy(node1)
                        continue
                merged_node = TreeNode(node1.val + node2.val)
                if creation_side == "left":
                    target_node.left = merged_node
                elif creation_side == "right":
                    target_node.right = merged_node
                next_frontier.append((node1.left, node2.left, merged_node, "left"))
                next_frontier.append((node1.right, node2.right, merged_node, "right"))
            frontier = next_frontier
        return dummy_merged_root.left
                
                    