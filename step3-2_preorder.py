# 1st: 29:45
# 2nd: 7:14

from dataclasses import dataclass


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

@dataclass
class Range:
    left_inclusive: int = 0
    right_inclusive: int = 0

    def contains(self, index):
        return self.left_inclusive <= index <= self.right_inclusive


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            raise ValueError()
        if len(preorder) != len(inorder):
            raise ValueError

        inorder_index = {inorder[i] : i for i in range(len(inorder))}
        
        dummy_root = TreeNode()
        child_unresolved = [(dummy_root, Range(0, len(inorder) - 1), Range())]        

        i = 0
        while i < len(preorder):
            node_value = preorder[i]
            parent, left_range, right_range = child_unresolved[-1]
            node = TreeNode(node_value)
            if left_range.contains(inorder_index[node_value]):
                parent.left = node
                child_unresolved.append((node, Range(left_range.left_inclusive, inorder_index[node_value] - 1), Range(inorder_index[node_value] + 1, left_range.right_inclusive)))
                i += 1
                continue
            if right_range.contains(inorder_index[node_value]):
                parent.right = node
                child_unresolved.append((node, Range(right_range.left_inclusive, inorder_index[node_value] - 1), Range(inorder_index[node_value] + 1, right_range.right_inclusive)))
                i += 1
                continue
            child_unresolved.pop() 

        return dummy_root.left