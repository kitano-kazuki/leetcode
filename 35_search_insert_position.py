from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[-1]:
            return len(nums)

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1

        return right


nums = [1, 3, 5, 6]
target = 2
solution = Solution()
res = solution.searchInsert(nums, target)
print(res)
