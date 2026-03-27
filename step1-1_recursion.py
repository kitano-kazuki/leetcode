# solved 10:01


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def is_valid_bst_helper(node: TreeNode, minimum_val: int, maximum_val: int) -> bool:
            if not (minimum_val < node.val < maximum_val):
                return False

            is_left_subtree_valid = True
            if node.left is not None:
                is_left_subtree_valid = is_valid_bst_helper(node.left, minimum_val, node.val)

            is_right_subtree_valid = True
            if node.right is not None:
                is_right_subtree_valid = is_valid_bst_helper(node.right, node.val, maximum_val)

            return is_left_subtree_valid and is_right_subtree_valid

        return is_valid_bst_helper(root, float("-inf"), float("inf"))