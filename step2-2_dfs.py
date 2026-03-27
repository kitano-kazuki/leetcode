# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        if root is None:
            return True

        node_and_valid_range_pairs = [(root, float("-inf"), float("inf"))]
        while node_and_valid_range_pairs:
            node, minimum_val, maximum_val = node_and_valid_range_pairs.pop()
            if not (minimum_val < node.val < maximum_val):
                return False
            if node.left is not None:
                node_and_valid_range_pairs.append((node.left, minimum_val, node.val))
            if node.right is not None:
                node_and_valid_range_pairs.append((node.right, node.val, maximum_val))
        return True