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
        
        frontier = [(root, targetSum)]
        while frontier:
            next_frontier = []
            while frontier:
                node, target = frontier.pop()
                if node.left is None and node.right is None:
                    if node.val == target:
                        return True
                    continue
                if node.left is not None:
                    next_frontier.append((node.left, target - node.val))
                if node.right is not None:
                    next_frontier.append((node.right, target - node.val))
            frontier = next_frontier
        
        return False
