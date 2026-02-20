import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.topk_heap = []
        if k < 0:
            raise ValueError("k must be positive integer")
        if len(nums) < k - 1:
            raise ValueError("The number of elements should be more than or equal to k - 1")
        self.k = k
        for num in nums:
            heapq.heappush(self.topk_heap, num)

    def add(self, val: int) -> int:
        heapq.heappush(self.topk_heap, val)
        while len(self.topk_heap) > self.k:
            heapq.heappop(self.topk_heap)
        return self.topk_heap[0]