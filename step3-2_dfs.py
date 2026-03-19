# 1st: 1:55
# 1st: 1:41
# 1st: 1:25

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        root = TreeNode()
        frontier = [(0, len(nums) - 1, root)]
        while frontier:
            left, right, node = frontier.pop()
            mid = (left + right) // 2
            node.val = nums[mid]
            if left <= mid - 1:
                node.left = TreeNode()
                frontier.append((left, mid - 1, node.left))
            if mid + 1 <= right:
                node.right = TreeNode()
                frontier.append((mid + 1, right, node.right))
            
        return root