from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # NOTE:
        # The possible weight is between maximum of weights and sum of len(weight) / days shipments from the largest
        # allocate left to the maximum and right to the sum
        # try middle (left + right) // 2
        # possible -> set right to middle
        # impossible -> set left to middle

        possible_minimum = max(weights)
        num = len(weights)
        num_ave_shipment = num // days
        if num % days != 0:
            num_ave_shipment += 1
        possible_maximum = sum(sorted(weights, reverse=True)[:num_ave_shipment])

        left, right = possible_minimum, possible_maximum
        while left != right:
            middle = (left + right) // 2
            if self.isPossibleShipment(weights, days, middle):
                right = middle
            else:
                left = middle + 1

        return left

    def isPossibleShipment(self, weights, days, capacity):
        day = 1
        sum = 0
        for weight in weights:
            if sum + weight <= capacity:
                sum = sum + weight
            else:
                day += 1
                sum = weight
        return day <= days


solution = Solution()
weights = [10, 50, 100, 100, 50, 100, 100, 100]
solution.shipWithinDays(weights, 5)
