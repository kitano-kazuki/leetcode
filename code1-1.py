import copy


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        def generate_permutations(candidates: list[int], permutations: list[list[int]]):
            if not candidates:
                return permutations

            result = []
            for i, candidate in enumerate(candidates):
                permutations_copy = copy.deepcopy(permutations)
                for permutation in permutations_copy:
                    permutation.append(candidate)
                result.extend(generate_permutations(candidates[:i] + candidates[i + 1:], permutations_copy))
            
            return result

        return generate_permutations(nums, [[]])
            