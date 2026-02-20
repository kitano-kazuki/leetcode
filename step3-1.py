import bisect
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        if k < 0:
            raise ValueError("k must be positive")
        if len(nums) < k - 1:
            raise ValueError("Should meet condition: len(nums) >= k - 1")
        self.k = k
        sorted_nums = sorted(nums, reverse=True)
        self.topk_nums = sorted_nums[:k]
        

    def add(self, val: int) -> int:
        bisect.insort(self.topk_nums, val, key=lambda x: -x)
        if len(self.topk_nums) > self.k:
            self.topk_nums.pop()
        return self.topk_nums[-1]

        
