# 1st: 29:45

from dataclasses import dataclass


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

@dataclass
class Range:
    left_inclusive: int
    right_inclusive: int

    def contains(self, index):
        return self.left_inclusive <= index <= self.right_inclusive

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            raise ValueError()
        if len(preorder) != len(inorder):
            raise ValueError

        inorder_index = {}
        for i in range(len(inorder)):
            inorder_index[inorder[i]] = i

        dummy_root = TreeNode()
        possible_parents = [(dummy_root, Range(0, len(inorder) - 1), Range(0, len(inorder) - 1))]
        preorder_index = 0
        while preorder_index < len(preorder):
            node_value = preorder[preorder_index]
            node = TreeNode(node_value)
            parent_node, left_range, right_range = possible_parents[-1]
            if left_range.contains(inorder_index[node_value]):
                parent_node.left = node
                possible_parents.append((node, Range(left_range.left_inclusive, inorder_index[node_value] - 1), Range(inorder_index[node_value] + 1, left_range.right_inclusive)))
                preorder_index += 1
                continue
            if right_range.contains(inorder_index[node_value]):
                parent_node.right = node
                possible_parents.append((node, Range(right_range.left_inclusive, inorder_index[node_value] - 1), Range(inorder_index[node_value] + 1, right_range.right_inclusive)))
                preorder_index += 1
                continue
            possible_parents.pop()
        
        return dummy_root.left