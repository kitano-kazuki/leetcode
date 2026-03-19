from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])

        mid_idx = len(nums) // 2
        root_node = TreeNode(nums[mid_idx])
        left_nums = nums[:mid_idx]
        right_nums = nums[mid_idx + 1:]
        root_node.left = self.sortedArrayToBST(left_nums)
        root_node.right = self.sortedArrayToBST(right_nums)
        return root_node