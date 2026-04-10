# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not len(preorder) == len(inorder):
            raise ValueError("the length of the given two list are not equal.")
        value_to_preorder_index = {}
        value_to_inorder_index = {}
        for i in range(len(preorder)):
            value_to_preorder_index[preorder[i]] = i
            value_to_inorder_index[inorder[i]] = i
        
        def build_tree_helper(
            preorder_left_inclusive: int, 
            preorder_right_inclusive: int, 
            inorder_left_inclusive: int, 
            inorder_right_inclusive: int
        ) -> TreeNode | None:
            if not (preorder_left_inclusive <= preorder_right_inclusive):
                return None
            root_value = preorder[preorder_left_inclusive]
            if root_value not in value_to_inorder_index:
                raise KeyError(f"{root_value} is not found in the given inorder list.")
            root_pos_in_inorder = value_to_inorder_index[root_value]
            num_left_nodes = root_pos_in_inorder - inorder_left_inclusive
            left_tree = build_tree_helper(
                preorder_left_inclusive + 1,
                preorder_left_inclusive + num_left_nodes,
                inorder_left_inclusive,
                root_pos_in_inorder - 1
            )
            right_tree = build_tree_helper(
                preorder_left_inclusive + num_left_nodes + 1,
                preorder_right_inclusive,
                root_pos_in_inorder + 1,
                inorder_right_inclusive
            )
            root_node = TreeNode(root_value)
            root_node.left = left_tree
            root_node.right = right_tree
            return root_node

        return build_tree_helper(0, len(preorder) - 1, 0, len(inorder) - 1)
