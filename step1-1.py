class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0

        start = 0
        end = len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        
        return end
                