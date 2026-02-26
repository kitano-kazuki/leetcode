from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        taken_count1 = [0] * len(nums1)
        taken_count2 = [0] * len(nums2)
        sum_idx1_idx2_heap = []
        def append_if_possible(idx1, idx2):
            if idx1 < 0 or idx1 >= len(nums1):
                return
            if idx2 < 0 or idx2 >= len(nums2):
                return
            is_idx1_takable = taken_count1[idx1] == idx2
            is_idx2_takable = taken_count2[idx2] == idx1
            if is_idx1_takable and is_idx2_takable:
                heapq.heappush(sum_idx1_idx2_heap, (nums1[idx1] + nums2[idx2], idx1, idx2))
            return

        heapq.heappush(sum_idx1_idx2_heap, (nums1[0] + nums2[0], 0, 0))
        result = []
        while len(result) < k:
            if len(sum_idx1_idx2_heap) == 0:
                print("Not enough elements in nums1 and nums2. Try after changing k.")
                return
            _, idx1, idx2 = heapq.heappop(sum_idx1_idx2_heap)
            taken_count1[idx1] += 1
            taken_count2[idx2] += 1
            result.append((nums1[idx1], nums2[idx2]))
            append_if_possible(idx1 + 1, idx2)
            append_if_possible(idx1, idx2 + 1)
        return result