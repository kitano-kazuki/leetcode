from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        seen_idx1_idx2_pairs = set()
        sum_idx1_idx2_tuple_heap = []
        result = []
        num_taken = 0
        if len(nums1) * len(nums2) < k:
            raise ValueError("Given arrays wouldn't yield enough pairs.")
        heapq.heappush(sum_idx1_idx2_tuple_heap, (nums1[0] + nums2[0], 0, 0))
        while num_taken < k:
            _, cur_smallest_idx1, cur_smallest_idx2 = heapq.heappop(sum_idx1_idx2_tuple_heap)
            result.append((nums1[cur_smallest_idx1], nums2[cur_smallest_idx2]))
            num_taken += 1
            next_idx_of_idx1 = cur_smallest_idx1 + 1
            next_idx_of_idx2 = cur_smallest_idx2 + 1
            if next_idx_of_idx1 < len(nums1) and (next_idx_of_idx1, cur_smallest_idx2) not in seen_idx1_idx2_pairs:
                heapq.heappush(sum_idx1_idx2_tuple_heap, (nums1[next_idx_of_idx1] + nums2[cur_smallest_idx2], next_idx_of_idx1, cur_smallest_idx2))
                seen_idx1_idx2_pairs.add((next_idx_of_idx1, cur_smallest_idx2))
            if next_idx_of_idx2 < len(nums2) and (cur_smallest_idx1, next_idx_of_idx2) not in seen_idx1_idx2_pairs:
                heapq.heappush(sum_idx1_idx2_tuple_heap, (nums1[cur_smallest_idx1] + nums2[next_idx_of_idx2], cur_smallest_idx1, next_idx_of_idx2))
                seen_idx1_idx2_pairs.add((cur_smallest_idx1, next_idx_of_idx2))
        return result