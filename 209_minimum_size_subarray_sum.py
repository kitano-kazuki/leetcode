class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = left
        cur_min_len = 0
        cur_sum = nums[left]
        while (left < len(nums) or right < len(nums)):
            if cur_sum < target:
                if right == len(nums) - 1:
                    break
                right += 1
                cur_sum += nums[right]
            else:
                cur_len = right - left + 1
                if cur_min_len == 0 or cur_len  < cur_min_len:
                    cur_min_len = cur_len
                cur_sum -= nums[left]
                left += 1

        return cur_min_len
        

        
target = 7
nums = [2, 3, 1, 2, 4, 3]
solution = Solution()
print(solution.minSubArrayLen(target, nums))