from collections import defaultdict
import bisect

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        prefix_sum_to_idx = defaultdict(list)
        prefix_sum = [0] * n
        for i in range(n):
            prev_prefix_sum = prefix_sum[i - 1] if i > 0 else 0
            prefix_sum[i] = prev_prefix_sum + nums[i]
            prefix_sum_to_idx[prefix_sum[i]].append(i)

        result = 0

        if k in prefix_sum_to_idx:
            result += len(prefix_sum_to_idx[k])

        for start_idx in range(n):
            prefix_sum_for_k = k + prefix_sum[start_idx]
            if prefix_sum_for_k not in prefix_sum_to_idx:
                continue
            end_idx_candidates =  prefix_sum_to_idx[prefix_sum_for_k]
            boundary_idx = bisect.bisect_right(end_idx_candidates, start_idx)
            result += len(end_idx_candidates) - boundary_idx

        return result