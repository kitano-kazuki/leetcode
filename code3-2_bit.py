class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        all_subsets = []
        for bit_pattern in range(1 << len(nums)):
            subset = []
            for i in range(len(nums)):
                if 1 << i & bit_pattern:
                    subset.append(nums[i])
            all_subsets.append(subset)
        
        return all_subsets
        