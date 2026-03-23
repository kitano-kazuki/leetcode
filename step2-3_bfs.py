# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False
        
        frontier = [(root, 0)]
        while frontier:
            next_frontier = []
            while frontier:
                node, pathsum_before_this_node = frontier.pop()
                is_leaf = node.left is None and node.right is None
                if is_leaf and pathsum_before_this_node + node.val == targetSum:
                    return True
                if node.left is not None:
                    next_frontier.append((node.left, pathsum_before_this_node + node.val))
                if node.right is not None:
                    next_frontier.append((node.right, pathsum_before_this_node + node.val))
            frontier = next_frontier
        
        return False
