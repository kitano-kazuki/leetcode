import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k <= 0:
            raise ValueError("k must be more than 0.")
        value_to_count = {}
        for num in nums:
            if num not in value_to_count:
                value_to_count[num] = 0
            value_to_count[num] += 1
        heap = []
        for value, count in value_to_count.items():
            heapq.heappush(heap, (-count, value))
        result = []
        for _ in range(k):
            _, value = heapq.heappop(heap)
            result.append(value)
        return result
            