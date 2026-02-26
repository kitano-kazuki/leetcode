from typing import List
import heapq


class Solution:
    def _append_sum_idx_tuple_if_possible(self, idx1, idx2, candidate_heap, taken_count_from_nums1_list, taken_count_from_nums2_list, nums1, nums2):
        if idx1 < 0 or idx1 >= len(nums1):
            return
        if idx2 < 0 or idx2 >= len(nums2):
            return
        is_idx1_takable = taken_count_from_nums1_list[idx1] == idx2
        is_idx2_takable = taken_count_from_nums2_list[idx2] == idx1
        if is_idx1_takable and is_idx2_takable:
            heapq.heappush(candidate_heap, (nums1[idx1] + nums2[idx2], idx1, idx2))
            return
        return
        

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        taken_count_from_nums1_list = [0] * nums1_len
        taken_count_from_nums2_list = [0] * nums2_len
        candidate_sum_idx1_idx2_tuple = []
        heapq.heappush(candidate_sum_idx1_idx2_tuple, (nums1[0] + nums2[0], 0, 0))
        result = []
        while len(result) < k:
            if len(candidate_sum_idx1_idx2_tuple) == 0:
                print("Not enough elements in nums1 and nums2. Try after changing k.")
                return result
            _, idx1, idx2 = heapq.heappop(candidate_sum_idx1_idx2_tuple)
            result.append((nums1[idx1], nums2[idx2]))
            taken_count_from_nums1_list[idx1] += 1
            taken_count_from_nums2_list[idx2] += 1
            self._append_sum_idx_tuple_if_possible(
                idx1 + 1,
                idx2,
                candidate_sum_idx1_idx2_tuple,
                taken_count_from_nums1_list,
                taken_count_from_nums2_list,
                nums1,
                nums2
            )
            self._append_sum_idx_tuple_if_possible(
                idx1,
                idx2 + 1,
                candidate_sum_idx1_idx2_tuple,
                taken_count_from_nums1_list,
                taken_count_from_nums2_list,
                nums1,
                nums2
            )
        return result