class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum_sum = 0
        sum_to_count = {0: 1}
        result = 0
        for num in nums:
            cum_sum += num
            target_sum = cum_sum - k
            if target_sum in sum_to_count:
                result += sum_to_count[target_sum]
            sum_to_count.setdefault(cum_sum, 0)
            sum_to_count[cum_sum] += 1
        return result