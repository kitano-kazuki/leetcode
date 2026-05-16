class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:

        def generate_permutations(candidates: list[int]):
            if not candidates:
                return [[]]

            permutations = []
            for i, candidate in enumerate(candidates):
                permutations_without_candidate = generate_permutations(candidates[:i] + candidates[i + 1:])
                for permutation in permutations_without_candidate:
                    permutations.append(permutation + [candidate])

            return permutations

        return generate_permutations(nums)
            