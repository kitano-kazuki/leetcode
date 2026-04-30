import bisect


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        if not weights:
            return 0

        # weight_prefix_sum[i] = weights[0] + ... + weights[i]
        weight_prefix_sum = [0] * len(weights)
        weight_prefix_sum[0] = weights[0]
        for i in range(1, len(weights)):
            weight_prefix_sum[i] = weight_prefix_sum[i - 1] + weights[i]

        min_capacity = min(weights)
        max_capacity = weight_prefix_sum[-1]
        
        # 運べる最小を二分探索で探す
        while min_capacity < max_capacity:
            mid = (min_capacity + max_capacity) // 2
            if self._is_shippable(mid, days, weight_prefix_sum):
                max_capacity = mid
            else:
                min_capacity = mid + 1
        
        return min_capacity

    def _is_shippable(self, capacity, days, weight_prefix_sum) -> bool:
        weight_begin = 0
        for _ in range(days):
            if weight_begin == 0:
                weight_end = bisect.bisect_right(
                    weight_prefix_sum, 
                    capacity)
            else:
                weight_end = bisect.bisect_right(
                    weight_prefix_sum, 
                    capacity, 
                    lo=weight_begin,
                    key=lambda w: w - weight_prefix_sum[weight_begin - 1])
                
            if weight_end == len(weight_prefix_sum):
                return True

            weight_begin = weight_end

        return False


        