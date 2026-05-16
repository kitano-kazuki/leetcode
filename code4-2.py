class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        all_combinations = []

        def generate_combinations(index: int, sum_in_combination: int, combination: list[int]) -> None:
            if sum_in_combination > target:
                return
            if sum_in_combination == target:
                all_combinations.append(combination.copy())
                return
            if index == len(candidates):
                return
            
            combination.append(candidates[index])
            generate_combinations(index, sum_in_combination + candidates[index], combination)
            combination.pop()

            generate_combinations(index + 1, sum_in_combination, combination)

            return
        
        generate_combinations(0, 0, [])
        return all_combinations
