class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must not be empty")

        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                return nums[i]
        
        return nums[0]