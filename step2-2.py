from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k <= 0:
            raise ValueError("k must be more than 0.")
        num_counter = Counter(nums)
        return [value for (value, count) in num_counter.most_common(k)]