
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            smaller_nums = nums1
            larger_nums = nums2
        else:
            smaller_nums = nums2
            larger_nums = nums1
        
        exist_in_smaller = set()
        for num in smaller_nums:
            exist_in_smaller.add(num)
        
        result_set = set()
        for num in larger_nums:
            if num not in exist_in_smaller:
                continue
            result_set.add(num)
        
        return list(result_set)
        