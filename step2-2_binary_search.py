
class Solution:
    def binary_search(self, array: list[int], value: int) -> int:
        left_inclusive = 0
        right_exclusive = len(array)
        while left_inclusive < right_exclusive:
            mid = (left_inclusive + right_exclusive) // 2
            if value <= array[mid]:
                right_exclusive = mid
            else:
                left_inclusive = mid + 1
        return right_exclusive

    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # ith element is the minimum tail value for increasing subsequence of length i
        minimum_tails = [float("-inf")]

        for num in nums:
            index = self.binary_search(minimum_tails, num)
            if index == len(minimum_tails):
                minimum_tails.append(num)
            else:
                minimum_tails[index] = num
        
        return len(minimum_tails) - 1