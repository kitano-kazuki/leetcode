class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # when robbing houses in the range [0, n-2]
        robbed_without_last = self._rob_sequential_houses(nums, 0, len(nums) - 2)
        # when robbing houses in the range [1, n-1]
        robbed_with_last = self._rob_sequential_houses(nums, 1, len(nums) - 1)

        return max(robbed_without_last, robbed_with_last)

    def _rob_sequential_houses(self, nums: list[int], start: int, end: int) -> int:
        if start > end:
            return 0

        robbed_last = 0
        skipped_last = 0
        for i in range(start, end + 1):
            robbed_last, skipped_last = skipped_last + nums[i], max(robbed_last, skipped_last)
        
        return max(robbed_last, skipped_last)
        