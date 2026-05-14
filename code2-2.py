import collections
import dataclasses

@dataclasses.dataclass
class Candidate:
    index: int
    prefix_sum: int  # nums[0] + ... + nums[index]


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:
            return 0

        begin_candidates = collections.deque([Candidate(-1, 0)])
        accumulated_sum = 0
        minimum_subarray_length = float("inf")
        for end_index in range(len(nums)):
            accumulated_sum += nums[end_index]

            # 部分列の和がtarget以上になる開始点を採用
            while begin_candidates and accumulated_sum - begin_candidates[0].prefix_sum >= target:
                begin_candidate = begin_candidates.popleft()  # 採用した開始点は今後使わない
                subarray_length = end_index - begin_candidate.index
                minimum_subarray_length = min(minimum_subarray_length, subarray_length)
            
            # 現在の累積和以上の候補は不要
            while begin_candidates and begin_candidates[-1].prefix_sum >= accumulated_sum:
                begin_candidates.pop()
            begin_candidates.append(Candidate(end_index, accumulated_sum))

        if minimum_subarray_length == float("inf"):
            return 0
        else:
            return minimum_subarray_length
            
solution = Solution()
print(solution.minSubArrayLen(2, [1, -5, 2]))