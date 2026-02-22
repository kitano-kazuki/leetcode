# QuickSelectを使用
import random

class Solution:
    def partition(self, unique_nums, num_to_count, left, right, pivot_idx):
        pivot = num_to_count[unique_nums[pivot_idx]]
        unique_nums[pivot_idx], unique_nums[right] = unique_nums[right], unique_nums[pivot_idx]
        partitioned_idx = left
        for i in range(left, right):
            if num_to_count[unique_nums[i]] <= pivot:
                unique_nums[i], unique_nums[partitioned_idx] = unique_nums[partitioned_idx], unique_nums[i]
                partitioned_idx += 1
        unique_nums[partitioned_idx], unique_nums[right] = unique_nums[right], unique_nums[partitioned_idx]
        return partitioned_idx
        

    def quick_select(self, unique_nums, num_to_count, left, right, smallest_k):
        if left == right:
            return
        pivot_idx = random.randint(left, right)
        partitioned_idx = self.partition(unique_nums, num_to_count, left, right, pivot_idx)
        if partitioned_idx == smallest_k:
            return
        if partitioned_idx > smallest_k:
            self.quick_select(unique_nums, num_to_count, left, partitioned_idx - 1, smallest_k)
            return
        self.quick_select(unique_nums, num_to_count, partitioned_idx + 1, right, smallest_k)
        return

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = {}
        for num in nums:
            num_to_count.setdefault(num, 0)
            num_to_count[num] += 1
        unique_nums = list(num_to_count)
        n = len(unique_nums)
        self.quick_select(unique_nums, num_to_count, 0, n - 1, n - k)
        return unique_nums[n - k:]

        