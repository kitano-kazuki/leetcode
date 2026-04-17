class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        robbed_last = 0
        skipped_last = 0
        for num in nums:
            robbed_last, skipped_last = skipped_last + num, max(robbed_last, skipped_last)
        
        return max(robbed_last, skipped_last)