class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:

        completed_combinations = set()
        all_combinations = []
        def generate_combination_sum(target: int, combination: list[int]) -> None:
            if target < 0:
                return
            if target == 0:
                combination_tuple = tuple(sorted(combination))
                if combination_tuple in completed_combinations:
                    return
                all_combinations.append(combination.copy())
                completed_combinations.add(combination_tuple)
                return

            for candidate in candidates:
                combination.append(candidate)
                generate_combination_sum(target - candidate, combination)
                combination.pop()
            
            return
        
        generate_combination_sum(target, [])
        return all_combinations

        