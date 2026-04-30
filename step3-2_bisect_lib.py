import bisect


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        if not weights:
            return -1

        def is_shippable(capacity: int) -> bool:
            spent_days = 1
            weights_on_ship = 0
            for i in range(len(weights)):
                if weights_on_ship + weights[i] <= capacity:
                    weights_on_ship += weights[i]
                    continue

                spent_days += 1
                if spent_days > days:
                    return False

                weights_on_ship = weights[i]

            return True
        
        min_capacity = max(weights)
        max_capacity = sum(weights) + 1
        capacity_range = range(min_capacity, max_capacity)
        index = bisect.bisect_left(capacity_range, True, key=is_shippable)
        return capacity_range[index]
