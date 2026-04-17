# solved: 3:33

class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        robbed_before = 0
        not_robbed_before = 0
        for num in nums:
            robbed_before, not_robbed_before = not_robbed_before + num, max(not_robbed_before, robbed_before)
        
        return max(robbed_before, not_robbed_before)