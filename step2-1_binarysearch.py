class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        offset = self._find_minimum_index(nums)
        index = self._binary_search_left_with_offset(nums, offset, target)
        if nums[index] == target:
            return index
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

    # ex) [6, 4, 5, 6], offset=1, target=6 -> 3
    # ex) [7, 4, 5], offset=1, target=6 -> 0
    # ex) [7, 4, 5], offset=2, target=6 -> Unexpected(offset should be index of the minimum)
    def _binary_search_left_with_offset(self, nums: list[int], offset: int, target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            mid_with_offset = (mid + offset) % len(nums)
            if nums[mid_with_offset] < target:
                left = mid + 1
            else:
                right = mid
       
        return (left + offset) % len(nums)
