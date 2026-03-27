# solved 1:34

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

        node_to_visit = [(root, float("-inf"), float("inf"))]
        while node_to_visit:
            node, minimum_val, maximum_val = node_to_visit.pop()
            if not (minimum_val < node.val < maximum_val):
                return False
            if node.left is not None:
                node_to_visit.append((node.left, minimum_val, node.val))
            if node.right is not None:
                node_to_visit.append((node.right, node.val, maximum_val))
        return True