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
        if root1 is None:
            return deepcopy(root2)
        if root2 is None:
            return deepcopy(root1)

        merged_dummy_head = TreeNode()
        tree1_frontier = [root1]
        tree2_frontier = [root2]
        merge_instructions = [(merged_dummy_head, "left")]
        while tree1_frontier and tree2_frontier:
            node1 = tree1_frontier.pop()
            node2 = tree2_frontier.pop()
            target, creation_side = merge_instructions.pop()
            if node1 is None and node2 is None:
                continue
            if creation_side == "left":
                if node1 is None:
                    target.left = deepcopy(node2)
                    continue
                if node2 is None:
                    target.left = deepcopy(node1)
                    continue
                merged_node = TreeNode(node1.val + node2.val) 
                target.left = merged_node
            elif creation_side == "right":
                if node1 is None:
                    target.right = deepcopy(node2)
                    continue
                if node2 is None:
                    target.right = deepcopy(node1)
                    continue
                merged_node = TreeNode(node1.val + node2.val) 
                target.right = merged_node
            else:
                raise ValueError("creation side should be either right or left")
            tree1_frontier.append(node1.left)
            tree2_frontier.append(node2.left)
            merge_instructions.append((merged_node, "left"))
            tree1_frontier.append(node1.right)
            tree2_frontier.append(node2.right)
            merge_instructions.append((merged_node, "right"))

        return merged_dummy_head.left