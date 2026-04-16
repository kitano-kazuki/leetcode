# 1st: 8:10
# 2nd: 6:50
# 3rd: 3:01

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        return self.max_subarray_in_range(nums, 0, len(nums) - 1)
    
    def max_subarray_in_range(self, nums, left, right) -> int:
        if left == right:
            return nums[left]
        
        def max_subarray_through_mid(nums, left, right, mid) -> int:
            leftward_max_sum = float("-inf")
            leftward_sum = 0
            for i in range(mid, left - 1, -1):
                leftward_sum += nums[i]
                leftward_max_sum = max(leftward_max_sum, leftward_sum)
            
            rightward_max_sum = 0
            rightward_sum = 0
            for i in range(mid + 1, right + 1, 1):
                rightward_sum += nums[i]
                rightward_max_sum = max(rightward_max_sum, rightward_sum)
            
            return leftward_max_sum + rightward_max_sum
        
        mid = (left + right) // 2
        left_max_subarray = self.max_subarray_in_range(nums, left, mid)
        right_max_subarray = self.max_subarray_in_range(nums, mid + 1, right)
        mid_through_max_subarray = max_subarray_through_mid(nums, left, right, mid)

        return max(
            left_max_subarray,
            right_max_subarray,
            mid_through_max_subarray
        )
