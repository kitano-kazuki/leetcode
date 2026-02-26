from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        already_in_heap_or_taken = set()
        candidate = []
        heapq.heappush(candidate, (nums1[0] + nums2[0], 0, 0))
        result = []
        while len(result) < k:
            if not candidate:
                raise ValueError("k is too large")
            _, idx1, idx2 = heapq.heappop(candidate)
            result.append((nums1[idx1], nums2[idx2]))
            if idx1 + 1 < len(nums1) and (idx1 + 1, idx2) not in already_in_heap_or_taken:
                already_in_heap_or_taken.add((idx1 + 1, idx2))
                heapq.heappush(candidate, (nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2))
            if idx2 + 1 < len(nums2) and (idx1, idx2 + 1) not in already_in_heap_or_taken:
                already_in_heap_or_taken.add((idx1, idx2 + 1))
                heapq.heappush(candidate, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))
        return result