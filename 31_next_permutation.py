# NOTE: [example]
# [1, 2, 3] -> [1, 3, 2]
# [1, 3, 2] -> [2, 1, 3]
# [2, 1, 3] -> [2, 3, 1]
# [2, 3, 1] -> [3, 1, 2]
# [3, 1, 2] -> [3, 2, 1]
# [3, 2, 1] -> [1, 2, 3]

# NOTE: [example]
# [1, 2, 3, 4, 5] -> [1, 2, 3, 5, 4]
# [6, 3, 1, 4, 5] -> [6, 3, 1, 5, 4]
# [6,3, 5 ,4, 1] -> [6, 4, 1, 3, 5]

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        order_start = -1
        for i in range(len(nums) - 1, 0, -1):
            fst = nums[i]
            snd = nums[i - 1]
            if fst > snd:
                order_start = i - 1
                break

        if order_start != -1:
            point = nums[order_start]
            minimum = -1
            minimum_index = -1
            for i, v in enumerate(nums[order_start + 1 :]):
                if v > point and (minimum == -1 or v < minimum):
                    minimum = v
                    minimum_index = i + order_start + 1
            nums[order_start], nums[minimum_index] = (
                nums[minimum_index],
                nums[order_start],
            )
            nums[order_start + 1 :] = sorted(nums[order_start + 1 :])
        else:
            nums.sort()

        return


nums = [1, 3, 2]
solution = Solution()
solution.nextPermutation(nums)
print(nums)
