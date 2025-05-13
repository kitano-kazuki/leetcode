# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        curMax = 0
        curArea = 0
        while(left < right):
            curArea = min(height[left], height[right]) * (right - left)
            if curArea > curMax:
                curMax = curArea
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return curMax

height = [1,8,6,2,5,4,8,3,7]
solution = Solution()
print(solution.maxArea(height))
        