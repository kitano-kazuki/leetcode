class Solution:
    def twoSum(self, nums, target):
        num_to_idx = {}
        for i, num in enumerate(nums):
            remain = target - num   # num + remain = target
            if remain  in num_to_idx:
                return [num_to_idx[remain], i]
            num_to_idx[num] = i
        raise ValueError("No solution found")