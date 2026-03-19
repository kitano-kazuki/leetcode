# 1st: 1:41
# 1st: 1:19
# 1st: 1:12


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def sortedArrayToBST_with_range(nums, left, right):
            if left > right:
                return None
            if left == right:
                return TreeNode(nums[left])
            
            mid = (left + right) // 2
            return TreeNode(
                val=nums[mid],
                left=sortedArrayToBST_with_range(nums, left, mid - 1),
                right=sortedArrayToBST_with_range(nums, mid + 1, right)
            )
        return sortedArrayToBST_with_range(nums, 0, len(nums) - 1)