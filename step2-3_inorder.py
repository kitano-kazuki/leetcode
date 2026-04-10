# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None
        if len(preorder) != len(inorder):
            return None

        node_value_to_preorder_index = {}
        for i in range(len(preorder)):
            node_value_to_preorder_index[preorder[i]] = i

        stack = []  # contains all nodes whose .right has not been decided yet
        for node_value in inorder:
            node = TreeNode(node_value)
            preorder_index = node_value_to_preorder_index[node_value]
            node.left = self._gather_decendants(preorder_index, stack, node_value_to_preorder_index)
            stack.append(node)
        return self._gather_decendants(float("-inf"), stack, node_value_to_preorder_index)

    def _gather_decendants(self, preorder_index, stack,node_value_to_preorder_index):
        child = None
        while stack:
            node = stack[-1]
            if node_value_to_preorder_index[node.val] < preorder_index:
                break
            stack.pop()
            node.right = child
            child = node
        return child

            
