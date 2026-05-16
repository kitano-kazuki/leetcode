class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        all_permutations = []

        permutation = []
        used_indices = set()
        def generate_permutations() -> None:
            if len(permutation) == len(nums):
                all_permutations.append(permutation.copy())
                return

            for i in range(len(nums)):
                if i in used_indices:
                    continue
                used_indices.add(i)
                permutation.append(nums[i])
                generate_permutations()
                permutation.pop()
                used_indices.remove(i)
            return
        
        generate_permutations()
        return all_permutations
                