# Heapを使用
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_count = {}
        for num in nums:
            num_to_count.setdefault(num, 0)
            num_to_count[num] += 1
        topk_heap = []
        for num, count in num_to_count.items():
            if len(topk_heap) < k:
                heapq.heappush(topk_heap, (count, num))
                continue
            if count <= topk_heap[0][0]:
                continue
            heapq.heappushpop(topk_heap, (count, num))
        return [num for count, num in topk_heap]