import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def compute_priority_of_rotated_array(num: int) -> tuple[int, int]:
            return (num <= nums[-1], num)
        
        index = bisect.bisect_left(
            nums,
            x = compute_priority_of_rotated_array(target),
            key=compute_priority_of_rotated_array
        )
        
        if nums[index] == target:
            return index
        return -1