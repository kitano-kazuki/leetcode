class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        if not weights:
            return -1

        min_capacity = max(weights)
        max_capacity = sum(weights) + 1
        while min_capacity < max_capacity:
            mid = (min_capacity + max_capacity) // 2
            if self._is_shippable(mid, weights, days):
                max_capacity = mid
            else:
                min_capacity = mid + 1
        
        return min_capacity
    
    def _is_shippable(self, capacity, weights, days):
        spent_days = 1
        weights_on_ship = 0
        for i in range(len(weights)):
            if weights_on_ship + weights[i] <= capacity:
                weights_on_ship += weights[i]
                continue
                
            spent_days += 1
            weights_on_ship = weights[i]
        
        return spent_days <= days
        