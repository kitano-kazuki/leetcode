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
    # print("pivot", pivot)
    n = len(nums)
    less_than_or_eq_pivot = 0
    more_than_pivot = n - 1
    while True:
        # TODO: pivot以下の要素だけで構成されているとOutOfIndexになる
        while nums[less_than_or_eq_pivot] <= pivot:
            less_than_or_eq_pivot += 1
        # TODO: pivotより大きい要素だけで構成されていると無限ループになる
        while nums[more_than_pivot] > pivot:
            more_than_pivot -= 1
        if more_than_pivot < less_than_or_eq_pivot:
            return more_than_pivot, nums
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

def quick_select(nums, k):
    print(nums, k, "search")
    partition_idx, partitioned_nums = partition(nums, PartitionMethod.LOMUTO, PivotMethod.LAST_ELEMENT)
    print(partitioned_nums, partition_idx)
    num_elements_lte_pivot = partition_idx + 1
    # hoare使ったらk番目とは限らなくなるのでは？？
    if k == num_elements_lte_pivot:
        return partitioned_nums[partition_idx]
    
    if num_elements_lte_pivot > k:
        return quick_select(partitioned_nums[:partition_idx], k)
    
    return quick_select(partitioned_nums[partition_idx + 1:], k - num_elements_lte_pivot)

print(quick_select([1,5,3,9,2], 3))