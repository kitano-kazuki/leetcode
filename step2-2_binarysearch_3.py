import math


class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must not be empty")
        if len(nums) == 1:
            return nums[0]

        # len(nums)>=2よりmidは-1にならない
        left_exclusive = -1
        right_inclusive = len(nums) - 1
        while left_exclusive + 1 != right_inclusive:
            mid = left_exclusive + math.ceil((right_inclusive - left_exclusive) / 2)
            if nums[0] <= nums[mid] and nums[mid] > nums[right_inclusive]:
                left_exclusive = mid
            else:
                right_inclusive = mid

        return nums[right_inclusive]

solution = Solution()
solution.findMin([3, 4, 5, 1, 2])
