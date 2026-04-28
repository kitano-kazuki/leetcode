class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0

        begin = 0
        end = len(nums)

        while begin < end:
            mid = begin + (end - begin) // 2
            
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                begin = mid + 1
            else:
                end = mid
        
        return end
                