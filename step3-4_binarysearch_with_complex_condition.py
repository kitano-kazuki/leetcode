class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1
        is_target_after_minimum = target <= nums[-1]
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid

            is_mid_after_minimum = nums[mid] <= nums[-1]

            if is_mid_after_minimum:
                if is_target_after_minimum:
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid
                else:
                    right = mid - 1
                continue

            if not is_mid_after_minimum:
                if is_target_after_minimum:
                    left = mid + 1
                else:
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid
                continue
        
        if nums[left] == target:
            return left
        return -1
                