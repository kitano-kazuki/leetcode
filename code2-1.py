class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:
            return 0

        left = 0
        right = 0
        current_sum = 0
        minimum_subarray_length = float("inf")
        while True:

            while current_sum < target:
            
                # 以降,和がtarget以上になることはない
                if right == len(nums):
                    if minimum_subarray_length == float("inf"):
                        return 0
                    else:
                        return minimum_subarray_length

                current_sum += nums[right]
                right += 1

            while current_sum >= target:
                minimum_subarray_length = min(minimum_subarray_length, right - left)

                if left == len(nums):
                    if minimum_subarray_length == float("inf"):
                        return 0
                    else:
                        return minimum_subarray_length

                current_sum -= nums[left]
                left += 1
                
solution = Solution()
print(solution.minSubArrayLen(2, [1, -5, 2]))