class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}
        for i, num in enumerate(nums):
            remain = target - num   # target = num + remain
            if remain in num_to_idx:
                return [num_to_idx[remain], i]
            num_to_idx[num] = i
        raise ValueError("No solution found")