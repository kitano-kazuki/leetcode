class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        offset = self._find_minimum_index(nums)

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            mid_with_offset = (mid + offset) % len(nums)
            if nums[mid_with_offset] < target:
                left = mid + 1
            else:
                right = mid
        
        insertion_index_with_offset = (left + offset) % len(nums)

        if nums[insertion_index_with_offset] == target:
            return insertion_index_with_offset
        return -1

    def _find_minimum_index(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid

        return left