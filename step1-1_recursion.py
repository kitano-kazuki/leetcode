# solved 8:33
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

        def mergeTrees_helper(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> Optional[TreeNode]:
            if node1 is None:
                return deepcopy(node2)
            if node2 is None:
                return deepcopy(node1)
            
            merged_node = TreeNode(val=node1.val + node2.val)
            merged_tree_left = mergeTrees_helper(node1.left, node2.left)
            merged_tree_right = mergeTrees_helper(node1.right, node2.right)
            merged_node.left = merged_tree_left
            merged_node.right = merged_tree_right
            return merged_node

        return mergeTrees_helper(root1, root2)
            
        