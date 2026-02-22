# Quick Select
import random


class Solution:
    def partition(self, unique_nums, num_to_counts, left, right, pivot_idx):
        unique_nums[right], unique_nums[pivot_idx] = unique_nums[pivot_idx], unique_nums[right]
        pivot = num_to_counts[unique_nums[right]]
        partition_idx = left
        for i in range(left, right):
            if num_to_counts[unique_nums[i]] <= pivot:
                unique_nums[i], unique_nums[partition_idx] = unique_nums[partition_idx], unique_nums[i]
                partition_idx += 1
        unique_nums[partition_idx], unique_nums[right] = unique_nums[right], unique_nums[partition_idx]
        return partition_idx

    def quick_select(self, unique_nums, num_to_counts, left, right, smallest_k):
        if left == right:
            return
        pivot_idx = random.randint(left, right)
        partition_idx = self.partition(unique_nums, num_to_counts, left, right, pivot_idx)
        if partition_idx == smallest_k:
            return
        if partition_idx > smallest_k:
            self.quick_select(unique_nums, num_to_counts, left, partition_idx - 1, smallest_k)
        else:
            self.quick_select(unique_nums, num_to_counts, partition_idx + 1, right, smallest_k)
        return
        
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_counts = {}
        for num in nums:
            num_to_counts.setdefault(num, 0)
            num_to_counts[num] += 1
        unique_nums = list(num_to_counts)
        n = len(unique_nums)
        self.quick_select(unique_nums, num_to_counts, 0, n - 1,  n - k)
        return unique_nums[n - k:]