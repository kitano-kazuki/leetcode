import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def is_between_minimum_and_right(num: int) -> bool:
            return (num <= nums[-1])

        minimum_index = bisect.bisect_left(nums, True, key=is_between_minimum_and_right)

        if is_between_minimum_and_right(target):
            lo, hi = minimum_index, len(nums)
        else:
            lo, hi = 0, minimum_index
        
        index = bisect.bisect_left(nums, target, lo, hi)
        
        if nums[index] == target:
            return index
        return -1
            
