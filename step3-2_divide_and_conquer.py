# 1st: 8:10

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.max_sub_array_in_range(nums, 0, len(nums) - 1)

    def max_sub_array_in_range(self, nums, left, right) -> int:
        if left == right:
            return nums[left]

        def max_subarray_in_range_through_middle(nums, left, right, mid) -> int:
            leftward_max_subarray = float("-inf")
            leftward_sum = 0
            for i in range(mid, left - 1, -1):
                leftward_sum += nums[i]
                leftward_max_subarray = max(leftward_max_subarray, leftward_sum)

            rightward_max_subarray = 0
            rightward_sum = 0
            for i in range(mid + 1, right + 1, 1):
                rightward_sum += nums[i]
                rightward_max_subarray = max(rightward_max_subarray, rightward_sum)
            
            return leftward_max_subarray + rightward_max_subarray

        mid = (left + right) // 2
        max_sub_array_in_left_half = self.max_sub_array_in_range(nums, left, mid)
        max_sub_array_in_right_half = self.max_sub_array_in_range(nums, mid + 1, right)
        max_sub_array_through_middle = max_subarray_in_range_through_middle(nums, left, right, mid)
        return max(
            max_sub_array_in_left_half,
            max_sub_array_in_right_half,
            max_sub_array_through_middle
        )
