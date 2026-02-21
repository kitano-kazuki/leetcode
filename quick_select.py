import copy
import random
from enum import Enum


class PivotMethod(Enum):
    LAST_ELEMENT = 0
    RANDOM_ELEMENT = 1
    MEDIAN_OF_MEDIANS = 2

class PartitionMethod(Enum):
    LOMUTO = 0
    HOARE = 1

def get_pivot_by_last_element(nums):
    return nums[-1]

def get_pivot_by_random_element(nums):
    random_idx = random.choice(range(len(nums)))
    nums[random_idx], nums[-1] = nums[-1], nums[random_idx]
    return nums[-1]
    

# Wikipedia URL
# https://en.wikipedia.org/wiki/Quicksort#Lomuto_partition_scheme
def partition_by_lomuto(arg_nums, pivot_func):
    nums = copy.deepcopy(arg_nums)
    pivot = pivot_func(nums)
    # print("pivot", pivot)
    n = len(nums)
    idx_to_exchange = 0
    for i in range(n - 1):
        if nums[i] <= pivot:
            nums[i], nums[idx_to_exchange] = nums[idx_to_exchange], nums[i]
            idx_to_exchange += 1
    nums[idx_to_exchange], nums[n - 1] = nums[n - 1], nums[idx_to_exchange]
    return idx_to_exchange, nums
    

# Wikipedia URL
# https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
def partition_by_hoare(arg_nums, pivot_func):
    nums = copy.deepcopy(arg_nums)
    pivot = pivot_func(nums)
    print("pivot", pivot)
    n = len(nums)
    less_than_or_eq_pivot = 0
    more_than_pivot = n - 1
    while True:
        while less_than_or_eq_pivot < n and nums[less_than_or_eq_pivot] <= pivot:
            less_than_or_eq_pivot += 1
        if less_than_or_eq_pivot == n:
            return n - 1, nums
        while more_than_pivot >= 0 and nums[more_than_pivot] > pivot:
            more_than_pivot -= 1
        if more_than_pivot == -1:
            return 0, nums
        if more_than_pivot < less_than_or_eq_pivot:
            print("returning", more_than_pivot, nums)
            return more_than_pivot, nums
        print("swap", less_than_or_eq_pivot, more_than_pivot)
        nums[less_than_or_eq_pivot], nums[more_than_pivot] = nums[more_than_pivot], nums[less_than_or_eq_pivot]
    

def partition(nums, partition_method, pivot_method):
    pivot_func = None
    if pivot_method == PivotMethod.LAST_ELEMENT:
        pivot_func = get_pivot_by_last_element
    elif pivot_method == PivotMethod.RANDOM_ELEMENT:
        pivot_func = get_pivot_by_random_element
    else:
        raise ValueError("pivot method must be the value of PivotMethod(Enum)")
    
    if partition_method == PartitionMethod.HOARE:
        return partition_by_hoare(nums, pivot_func)
    elif partition_method == PartitionMethod.LOMUTO:
        return partition_by_lomuto(nums, pivot_func)
    else:
        raise ValueError("partition method must be the value of PartitionMethod(Enum)")



def test_partition(nums):
    idx, partitioned_nums = partition(nums, PartitionMethod.HOARE, PivotMethod.LAST_ELEMENT)
    print(partitioned_nums, idx)
    idx, partitioned_nums = partition(nums, PartitionMethod.LOMUTO, PivotMethod.LAST_ELEMENT)
    print(partitioned_nums, idx)
    idx, partitioned_nums = partition(nums, PartitionMethod.HOARE, PivotMethod.RANDOM_ELEMENT)
    print(partitioned_nums, idx)
    idx, partitioned_nums = partition(nums, PartitionMethod.LOMUTO, PivotMethod.RANDOM_ELEMENT)
    print(partitioned_nums, idx)
    """
    pivot 5
    [1, 3, 5, 51] 2
    pivot 5
    [1, 3, 5, 51] 2
    pivot 3
    [1, 3, 51, 5] 1
    pivot 51
    [1, 3, 5, 51] 3
    """

def quick_select(nums, k, partition_method):
    if partition_method == PartitionMethod.HOARE:
        partition_idx, partitioned_nums = partition(nums, PartitionMethod.HOARE, PivotMethod.LAST_ELEMENT)
    else:
        partition_idx, partitioned_nums = partition(nums, PartitionMethod.LOMUTO, PivotMethod.LAST_ELEMENT)
    num_elements_lte_pivot = partition_idx + 1
    if k == num_elements_lte_pivot:
        # ここはhoareだと正しく動作しない. 
        # lomutoはpartition_idxに必ずpivotとなった値が存在するが, hoareでは何が存在するか不明
        # nums = [4, 10, 1, 2, 7] k = 4をhoareで動作することを考える
        # pivotでいちばんうしろの7を選択.
        # 4 10 1 2 7
        # l        r
        # 4 10 1 2 7
        #    l     r
        # swap!!!
        # 4 7 1 2 10
        #   l      r
        # 4 7 1 2 10
        #     l    r
        # 4 7 1 2 10
        #       l  r
        # 4 7 1 2 10
        #         lr
        # 4 7 1 2 10
        #       r l 
        # return the position of r(=3)
        # num_elements_lte_pivot = 3 + 1 = 4
        # これはkに等しいのでpartitioned_nums[3]を返す
        # しかしこれの値は2であり, 正しい値の7とは異なる
        return partitioned_nums[partition_idx]
    
    if num_elements_lte_pivot > k:
        return quick_select(partitioned_nums[:partition_idx], k, partition_method)
    
    return quick_select(partitioned_nums[partition_idx + 1:], k - num_elements_lte_pivot, partition_method)

def test_quick_select():
    num_iteration = 100
    for _ in range(num_iteration):
        nums = [random.randint(0, 10) for _ in range(5)]
        k = random.randint(0, 4)
        hoare_result = quick_select(nums, k, PartitionMethod.HOARE)
        lomuto_result = quick_select(nums, k, PartitionMethod.LOMUTO)
        gt = sorted(nums)[k - 1]
        assert hoare_result == lomuto_result, f"hoare {hoare_result}, lomuto: {lomuto_result}.  nums: {nums},  k: {k}, gt: {gt}"


print(quick_select([4, 10, 1, 2, 7], 4, PartitionMethod.HOARE))