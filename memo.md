# Step1

## アプローチ

* capcityを変えて行った時にどこかのポイントで運べるか運べないかが切り替わる
* 二分探索でその切り替わる場所を探す
* 運べるかどうかの判定はO(N)でGreedyにやればいいかな
* 全体だとO(NlogN)になる
* 実行時間は 10^4 * log(10^4) ~= 0.1 secくらい
* 運べるかどうかの判定ってもう少し効率的にできないかな？？
    * prefix_sum使うくらいか？？
    * prefix_sum使った上で二分探索をday回やるとか

## Code1-1 (Binary Search)

```python
import bisect


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        if not weights:
            return 0

        weight_prefix_sum = [0] * len(weights)
        weight_prefix_sum[0] = weights[0]
        for i in range(1, len(weights)):
            weight_prefix_sum[i] = weight_prefix_sum[i - 1] + weights[i]

        min_capacity = min(weights)
        max_capacity = weight_prefix_sum[-1]
        
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

```
