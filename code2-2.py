class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swap_index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[i], nums[swap_index] = nums[swap_index], nums[i]
            swap_index += 1

        return
        