class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        all_subsets = [[]]
        for i in range(len(nums)):
            next_all_subsets = []
            for subset in all_subsets:
                next_all_subsets.append(subset)
                next_all_subsets.append(subset + [nums[i]])
            all_subsets = next_all_subsets
        
        return all_subsets
            