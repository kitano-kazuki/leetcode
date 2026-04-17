from functools import cache


class Solution:
    def rob(self, nums: list[int]) -> int:
        
        @cache
        def rob_upto(end: int) -> int:
            if end < 0:
                return 0
            if end == 0:
                return nums[0]
            
            return max(rob_upto(end - 1), rob_upto(end - 2) + nums[end])

        return rob_upto(len(nums) - 1)