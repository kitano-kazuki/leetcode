# solved 2:38


from collections import deque


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

        frontier = deque([(root, float("-inf"), float("inf"))])
        while frontier:
            next_frontier = deque()
            while frontier:
                node, minimum_val, maximum_val = frontier.popleft()
                if not (minimum_val < node.val < maximum_val):
                    return False
                if node.left is not None:
                    next_frontier.append((node.left, minimum_val, node.val))
                if node.right is not None:
                    next_frontier.append((node.right, node.val, maximum_val))
            frontier = next_frontier
        return True

        