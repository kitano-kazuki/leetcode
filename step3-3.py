from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        num_taken1 = [0] * len(nums1)
        num_taken2 = [0] * len(nums2)
        candidate = []
        def append_if_possible(idx1, idx2):
            if idx1 < 0 or idx1 >= len(nums1):
                return
            if idx2 < 0 or idx2 >= len(nums2):
                return
            is_idx1_takable = num_taken1[idx1] == idx2
            is_idx2_takable = num_taken2[idx2] == idx1
            if is_idx1_takable and is_idx2_takable:
                heapq.heappush(candidate, (nums1[idx1] + nums2[idx2], idx1, idx2))
            return

        heapq.heappush(candidate, (nums1[0] + nums2[0], 0, 0))
        result = []
        while len(result) < k:
            if not candidate:
                raise ValueError("k is too large")
            _, idx1, idx2 = heapq.heappop(candidate)
            result.append((nums1[idx1], nums2[idx2]))
            num_taken1[idx1] += 1
            num_taken2[idx2] += 1
            append_if_possible(idx1 + 1, idx2)
            append_if_possible(idx1, idx2 + 1)
        return result
