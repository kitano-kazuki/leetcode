from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        already_in_heap = set()
        candidates_heap = []
        result = []
        num_taken = 0
        if len(nums1) * len(nums2) < k:
            raise ValueError("Given arrays wouldn't yield enough pairs.")
        heapq.heappush(candidates_heap, (nums1[0] + nums2[0], 0, 0))
        while num_taken < k:
            _, smallest_idx1, smallest_idx2 = heapq.heappop(candidates_heap)
            result.append((nums1[smallest_idx1], nums2[smallest_idx2]))
            num_taken += 1
            if smallest_idx1 < len(nums1) - 1 and (smallest_idx1 + 1, smallest_idx2) not in already_in_heap:
                heapq.heappush(candidates_heap, (nums1[smallest_idx1 + 1] + nums2[smallest_idx2], smallest_idx1 + 1, smallest_idx2))
                already_in_heap.add((smallest_idx1 + 1, smallest_idx2))
            if smallest_idx2 < len(nums2) - 1 and (smallest_idx1, smallest_idx2 + 1) not in already_in_heap:
                heapq.heappush(candidates_heap, (nums1[smallest_idx1] + nums2[smallest_idx2 + 1], smallest_idx1, smallest_idx2 + 1))
                already_in_heap.add((smallest_idx1, smallest_idx2 + 1))
        return result