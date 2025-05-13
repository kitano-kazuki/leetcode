# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution(object):
    def _append_as_set(self, result, results):
        for existing_result in results:
            is_same = True
            for i in range(len(result)):
                if existing_result[i] != result[i]:
                    is_same = False
                    break
            if is_same:
                return results
        results.append(result)
        return  results


    def _twoSum(self, nums, target, left, right):
        results = []
        sum = nums[left] + nums[right]
        n1, n2 = None, None
        while (left < right):
            if sum > target:
                right -= 1
            elif sum < target:
                left += 1
            else:
                n1 = nums[left]
                n2 = nums[right]
                results.append([n1, n2])
                left += 1
                right -= 1

            sum = nums[left] + nums[right]

        return results


    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        results = []
        for i in range(len(nums) - 2):
            n1 = nums[i]
            target = -n1
            left = i + 1
            right = len(nums) - 1
            two_sum_results = self._twoSum(nums, target, left, right)
            if two_sum_results == []:
                continue
            for result in two_sum_results:
                result.append(n1)
                sorted(result)
                self._append_as_set(result, results)

        return results
        
nums = [-1,0,1,2,-1,-4]

solution = Solution()
print(solution.threeSum(nums))