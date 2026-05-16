class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        subset = []
        all_subsets = []
        def generate_subsets(start: int) -> None:
            if start == len(nums):
                all_subsets.append(subset.copy())
                return

            subset.append(nums[start])
            generate_subsets(start + 1)
            subset.pop()
            generate_subsets(start + 1)
            

        generate_subsets(0)
        return all_subsets
