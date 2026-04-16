class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray_sum = float("-inf")
        max_subarray_sum_before = 0
        for num in nums:
            max_subarray_sum_before = max(max_subarray_sum_before + num, num)
            max_subarray_sum = max(max_subarray_sum, max_subarray_sum_before)
        return max_subarray_sum