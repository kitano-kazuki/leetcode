class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_tail = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[non_zero_tail] = nums[i]
            non_zero_tail += 1
        for i in range(non_zero_tail, len(nums)):
            nums[i] = 0
        
        return
