class Solution:
    def findMin(self, nums: list[int]) -> int:
        if not nums:
            raise ValueError("nums must not be empty.")
        
        if len(nums) == 1:
            return nums[0]

        left_inclusive = 0
        right_inclusive = len(nums) - 1
        while left_inclusive < right_inclusive:
            mid = left_inclusive + (right_inclusive - left_inclusive) // 2
            if nums[mid] > nums[-1]:
                left_inclusive = mid + 1
            else:
                right_inclusive = mid
        
        return nums[left_inclusive]
                
        