# solved: 10:18


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        # minimum_values[i] represents the minimum tail value among possile LIS with length i
        minimum_values = [float("inf")] * (n + 1)
        minimum_values[0] = float("-inf")

        for i in range(n):
            for length in range(1, i + 2):
                if minimum_values[length - 1] < nums[i] and nums[i] < minimum_values[length]:
                    minimum_values[length] = nums[i]
        
        for i in range(n, -1, -1):
            if minimum_values[i] != float("inf"):
                return i