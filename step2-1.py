# solved: 10:18


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        # minimum_values[i] represents the minimum tail value among possile LIS with length i
        minimum_values = [float("inf")] * (n + 1)
        minimum_values[0] = float("-inf")

        for num_index in range(n):
            num_of_elements = num_index + 1
            for length in range(1, num_of_elements + 1):
                if minimum_values[length - 1] < nums[num_index]:
                    minimum_values[length] = min(nums[num_index], minimum_values[length])
        
        for i in range(n, -1, -1):
            if minimum_values[i] != float("inf"):
                return i