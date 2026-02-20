import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        if k < 0:
            raise ValueError("k must be positive")
        if len(nums) < k - 1:
            raise ValueError("len(nums) should be more than or equal to k - 1")
        self.topk_heap = []
        self.k = k
        for num in nums:
            heapq.heappush(self.topk_heap, num)
        while len(self.topk_heap) > self.k:
            heapq.heappop(self.topk_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.topk_heap, val)
        if len(self.topk_heap) > self.k:
            heapq.heappop(self.topk_heap)
        return self.topk_heap[0]
        
