# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        sum = numbers[left] + numbers[right]
        while(sum != target):
            if sum > target:
                right -= 1
            else:
                left += 1
            sum = numbers[left] + numbers[right]

        return [left + 1, right + 1]


numbers = [2,7,11,15]
target = 9
solution = Solution()
print(solution.twoSum(numbers, target))
        