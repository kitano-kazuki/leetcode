# QuickSelectを使用
import random


class Solution:
    def partition(self, uniques, num_to_count, left, right, pivot_idx):
        pivot = num_to_count[uniques[pivot_idx]]
        uniques[pivot_idx], uniques[right] = uniques[right], uniques[pivot_idx]
        partition_idx = left
        for i in range(left, right):
            if num_to_count[uniques[i]] <= pivot:
                uniques[i], uniques[partition_idx] = uniques[partition_idx], uniques[i]
                partition_idx += 1
        uniques[partition_idx], uniques[right] = uniques[right], uniques[partition_idx]
        return partition_idx

    def quick_select(self, uniques, num_to_count, left, right, smallest_k):
        if left == right:
            return
        pivot_idx = random.randint(left, right)
        partitioned_idx = self.partition(uniques, num_to_count, left, right, pivot_idx)
        if partitioned_idx == smallest_k:
            return
        if partitioned_idx > smallest_k:
            self.quick_select(uniques, num_to_count, left, partitioned_idx - 1, smallest_k)
            return
        self.quick_select(uniques, num_to_count, partitioned_idx + 1, right, smallest_k)
        return
        
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = {}
        for num in nums:
            num_to_count.setdefault(num, 0)
            num_to_count[num] += 1
        n = len(num_to_count)
        uniques = list(num_to_count)
        self.quick_select(uniques, num_to_count, 0, n - 1, n - k)
        return uniques[n - k:]
        