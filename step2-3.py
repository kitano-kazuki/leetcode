# Bucket Sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_count = 0
        num_to_count = {}
        for num in nums:
            num_to_count.setdefault(num, 0)
            num_to_count[num] += 1
            max_count = max(max_count, num_to_count[num])
        nums_by_count = [[] for _ in range(max_count + 1)]
        for num, count in num_to_count.items():
            nums_by_count[count].append(num)
        result = []
        for count in range(max_count, -1, -1):
            if len(nums_by_count[count]) + len(result) <= k:
                result.extend(nums_by_count[count])
                continue
            num_elements_to_add = k - len(result)
            result.extend(nums_by_count[count][:num_elements_to_add])
            break
        return result