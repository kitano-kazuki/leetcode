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
        
        result = set()
        for num in larger_nums:
            if num in exist_in_smaller:
                result.add(num)
        
        return list(result)

