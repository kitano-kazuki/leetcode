# 1st: 3:28
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

        def get_merged_val(node1, node2):
            val = 0
            if node1 is not None:
                val += node1.val
            if node2 is not None:
                val += node2.val
            return val

        def get_left(node):
            if node is None:
                return None
            return node.left
        
        def get_right(node):
            if node is None:
                return None
            return node.right
        
        merged_root = TreeNode()
        frontier = [(root1, root2, merged_root)]
        while frontier:
            node1, node2, merged_node = frontier.pop()
            merged_node.val = get_merged_val(node1, node2)
            node1_left, node2_left = get_left(node1), get_left(node2)
            if node1_left is not None or node2_left is not None:
                merged_node.left = TreeNode()
                frontier.append((node1_left, node2_left, merged_node.left))
            node1_right, node2_right = get_right(node1), get_right(node2)
            if node1_right is not None or node2_right is not None:
                merged_node.right = TreeNode()
                frontier.append((node1_right, node2_right, merged_node.right))
        return merged_root