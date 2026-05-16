class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        
        result = []

        permutation_and_candidates = [([], nums)]
        while permutation_and_candidates:
            permutation, candidates = permutation_and_candidates.pop()

            if not candidates:
                result.append(permutation)
                continue

            for i in range(len(candidates)):
                permutation_and_candidates.append(
                    (permutation + [candidates[i]], candidates[:i] + candidates[i + 1:])
                )
        
        return result
