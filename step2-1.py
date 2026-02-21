import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k <= 0:
            raise ValueError("k must be more than 0.")
        value_to_count = {}
        for num in nums:
            value_to_count[num] = value_to_count.get(num, 0) + 1
        max_heap = []
        for value, count in value_to_count.items():
            heapq.heappush(max_heap, (-count, value))
        result = []
        for _ in range(k):
            _, most_frequent_value = heapq.heappop(max_heap)
            result.append(most_frequent_value)
        return result