from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # TODO:
        # 配列を２分割して、それぞれの配列の最初と最後を比較
        # 昇順になっていたら、ターゲットが間にあるか確認
        # 昇順になっていなかったら、配列をさらに分割

        print(nums)

        if len(nums) < 4:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
            return -1

        mid = len(nums) // 2
        nums1, nums2 = nums[:mid], nums[mid:]

        fst, snd = nums1[0], nums1[-1]
        if fst < snd:
            if fst <= target <= snd:
                searched = self.search(nums1, target)
                if searched == -1:
                    return -1
                return searched
            searched = self.search(nums2, target)
            if searched == -1:
                return -1
            return len(nums1) + searched

        fst, snd = nums2[0], nums2[-1]
        if fst < snd:
            if fst <= target <= snd:
                searched = self.search(nums2, target)
                if searched == -1:
                    return -1
                return len(nums1) + searched
            searched = self.search(nums1, target)
            if searched == -1:
                return -1
            return searched

        return 999


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
solution = Solution()
res = solution.search(nums, target)
print(res)
