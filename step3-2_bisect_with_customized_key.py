import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # rotated array -> corresponding keys
        # [5, 6, 1, 2] -> [(0, 5), (0, 6), (1, 1), (1, 2)]
        def compute_key_for_rotated_array(num: int) -> tuple[int, int]:
            return (num <= nums[-1], num)

        index = bisect.bisect_left(
            a   = nums, 
            x   = compute_key_for_rotated_array(target),
            key = compute_key_for_rotated_array
        )
        if nums[index] == target:
            return index
        return -1
        