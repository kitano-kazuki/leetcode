# 1st: 8:28
# 2nd: 3:32

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        minimum_tails = [float("-inf")]

        for num in nums:
            insertion_index = self.binary_search(minimum_tails, num)
            if insertion_index == len(minimum_tails):
                minimum_tails.append(num)
            else:
                minimum_tails[insertion_index] = num
        
        return len(minimum_tails) - 1

    def binary_search(self, array: list[int], target: int) -> int:
        left_inclusive = 0
        right_exclusive = len(array)
        while left_inclusive < right_exclusive:
            mid = (left_inclusive + right_exclusive) // 2
            if array[mid] < target:
                left_inclusive = mid + 1
            else:
                right_exclusive = mid
        return right_exclusive