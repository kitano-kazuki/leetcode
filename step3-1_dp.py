# 1st: 1:08

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray_sum = float("-inf")
        max_prefix_sum_ending_before = 0
        for num in nums:
            max_prefix_sum_ending_before = max(max_prefix_sum_ending_before + num, num)
            max_subarray_sum = max(max_subarray_sum, max_prefix_sum_ending_before)
        return max_subarray_sum