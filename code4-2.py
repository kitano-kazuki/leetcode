import dataclasses
import collections


@dataclasses.dataclass
class Candidate:
    index: int
    prefix_sum: int  # nums[0] + ... + nums[index]


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:
            return 0
        
        minimum_subarray_length = float("inf")
        begin_candidates = collections.deque([Candidate(-1, 0)])
        accumulated_sum = 0
        for end_index in range(len(nums)):
            accumulated_sum += nums[end_index]

            while begin_candidates and accumulated_sum - begin_candidates[0].prefix_sum >= target:
                begin_candidate = begin_candidates.popleft()
                subarray_length = end_index - begin_candidate.index
                minimum_subarray_length = min(minimum_subarray_length, subarray_length)
            
            while begin_candidates and begin_candidates[-1].prefix_sum >= accumulated_sum:
                begin_candidates.pop()
            begin_candidates.append(Candidate(end_index, accumulated_sum))

        if minimum_subarray_length == float("inf"):
            return 0
        
        return minimum_subarray_length
                