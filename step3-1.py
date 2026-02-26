from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        already_in_heap_or_taken_idx_pair = set()
        candidate_heap = []
        result = []
        heapq.heappush(candidate_heap, (nums1[0] + nums2[0], 0, 0))
        already_in_heap_or_taken_idx_pair.add((0,0))
        while len(result) < k:
            if not candidate_heap:
                raise ValueError("k is too large.")
            _, idx1, idx2 = heapq.heappop(candidate_heap)
            result.append((nums1[idx1], nums2[idx2]))
            if idx1 >= 0 and idx1 + 1 < len(nums1) and (idx1 + 1, idx2) not in already_in_heap_or_taken_idx_pair:
                heapq.heappush(candidate_heap, (nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2))
                already_in_heap_or_taken_idx_pair.add((idx1 + 1, idx2))
            if idx2 >= 0 and idx2 + 1 < len(nums2) and (idx1 , idx2 + 1) not in already_in_heap_or_taken_idx_pair:
                heapq.heappush(candidate_heap, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))
                already_in_heap_or_taken_idx_pair.add((idx1, idx2 + 1))
        return result
            
        