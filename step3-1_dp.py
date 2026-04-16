# 1st: 1:08
# 2st: 1:00
# 3rd: 0:55

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_subarray = float("-inf")
        max_subarray_ending_before = 0
        for num in nums:
            max_subarray_ending_before = max(max_subarray_ending_before + num, num)
            max_subarray = max(max_subarray_ending_before, max_subarray)
        return max_subarray
