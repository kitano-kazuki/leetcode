class Solution:
    def twoSum(self, nums, target):
        num_to_idx = {}
        for i, num in enumerate(nums):
            if target - num in num_to_idx:
                return [num_to_idx[target - num], i]
            num_to_idx[num] = i
        raise ValueError("No solution found")