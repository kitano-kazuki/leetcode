class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        all_subsets = []

        def generate_subset_after_index(index :int, subset: list[int]) -> None:
            if index == len(nums):
                all_subsets.append(subset.copy())
                return 
            
            subset.append(nums[index])
            generate_subset_after_index(index + 1, subset)
            subset.pop()
            generate_subset_after_index(index + 1, subset)
        
        generate_subset_after_index(0, [])
        return all_subsets
