import functools


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        
        @functools.cache
        def combination_sum_helper(target: int) -> list[list[int]]:
            if target < 0:
                return []

            if target == 0:
                return [[]]

            all_combinations = []
            for candidate in candidates:
                combinations = combination_sum_helper(target - candidate)
                if not combinations:
                    continue
                all_combinations.extend([combination + [candidate] for combination in combinations])
            
            return all_combinations

        combinations_with_duplicates = sorted([sorted(combination) for combination in combination_sum_helper(target)])
        previous_combination = None
        unique_combinations = []
        for combination in combinations_with_duplicates:
            if previous_combination is not None and previous_combination == combination:
                continue
            unique_combinations.append(combination)
            previous_combination = combination

        return unique_combinations
            

            