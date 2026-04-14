class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        return self.max_subarray_in_range(nums, 0, len(nums) - 1)

        
    def max_subarray_in_range(self, nums: list[int], left, right):
        if left == right:
            return nums[left]
       
        mid = (left + right)  // 2
        max_subarray_in_left_half = self.max_subarray_in_range(nums, left, mid)
        max_subarray_in_right_half = self.max_subarray_in_range(nums, mid + 1, right)
        max_subarray_through_mid = self.max_subarray_from_mid(nums, mid, left, right)
        return max(max_subarray_in_left_half,
                   max_subarray_in_right_half,
                   max_subarray_through_mid)


    def max_subarray_from_mid(self, nums: list[int], mid, left, right):
        leftward_sum = 0
        max_leftward_sum = float("-inf")
        for i in range(mid, left - 1, -1):
            leftward_sum += nums[i]
            max_leftward_sum = max(max_leftward_sum, leftward_sum)

        rightward_sum = 0
        max_rightward_sum = float("-inf")
        for i in range(mid + 1, right + 1, 1):
            rightward_sum += nums[i]
            max_rightward_sum = max(max_rightward_sum, rightward_sum)

        return max_leftward_sum + max_rightward_sum
