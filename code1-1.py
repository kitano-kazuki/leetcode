class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_nums = []
        for num in nums:
            if num != 0:
                non_zero_nums.append(num)
        
        if not non_zero_nums:
            return

        processed_tail = 0
        for i in range(len(nums)):
            if processed_tail < len(non_zero_nums):
                nums[i] = non_zero_nums[processed_tail]
                processed_tail += 1
            else:
                nums[i] = 0
        
        return
