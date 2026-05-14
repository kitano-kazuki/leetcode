class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:
            return 0
        
        minimum_subarray_length = float("inf")
        left = 0
        current_sum = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                minimum_subarray_length = min(minimum_subarray_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        if minimum_subarray_length == float("inf"):
            return 0

        return minimum_subarray_length
                