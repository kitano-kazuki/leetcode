# Step1

## アプローチ

* mapに数字ごとの出現回数を記録.
  * 全て記録し終わった後に出現回数の多い順に取り出し
    * ordered_mapとかpythonにあるのかな？
    * 自分の知っている知識でやるなら, heapにタプルで入れていく. 順番にk個取り出し
* 他の方法はパッと思いつかなかった.
  * 追記: bucket sortとquick selectを思いつけると良かった.
* map -> heapの時間とか空間の見積もり
  * 要素数をnとする
  * O(n)で出現回数mapの構築
  * O(nlogn)で全ての出現回数と値のペアをheapに挿入.
  * O(klogn)で上位k件を取り出し.
  * 辞書の保存, heapともに, O(n)
    * 追記: heapには常にk件だけが保存されるようにしたら, heapの使用する外部メモリはO(k)に収まる.

  ## Code1-1

  ```python
  import heapq
  class Solution:
      def topKFrequent(self, nums: List[int], k: int) -> List[int]:
          if k <= 0:
              raise ValueError("k must be more than 0.")
          value_to_count = {}
          for num in nums:
              if num not in value_to_count:
                  value_to_count[num] = 0
              value_to_count[num] += 1
          heap = []
          for value, count in value_to_count.items():
              heapq.heappush(heap, (-count, value))
          result = []
          for _ in range(k):
              _, value = heapq.heappop(heap)
              result.append(value)
          return result
  ```

  # Step2

  ## Code2-1

  * 後から振り返り: heapに全件を入れる必要はなかった. 上位k件だけが入るように, 最初のk件以降は一番小さい値より小さいものは入れない.

  ```python
  import heapq
  class Solution:
      def topKFrequent(self, nums: List[int], k: int) -> List[int]:
          if k <= 0:
              raise ValueError("k must be more than 0.")
          value_to_count = {}
          for num in nums:
              value_to_count[num] = value_to_count.get(num, 0) + 1
          max_heap = []
          for value, count in value_to_count.items():
              heapq.heappush(max_heap, (-count, value))
          result = []
          for _ in range(k):
              _, most_frequent_value = heapq.heappop(max_heap)
              result.append(most_frequent_value)
          return result
  ```

  ## Code2-2

  * collections.Counterには標準で上位n件を表示するメソッドがある.

  ```python
  from collections import Counter


  class Solution:
      def topKFrequent(self, nums: List[int], k: int) -> List[int]:
          if k <= 0:
              raise ValueError("k must be more than 0.")
          num_counter = Counter(nums)
          return [value for (value, count) in num_counter.most_common(k)]
  ```

  # 他の人の回答も見てみる

  ## 学んだこと

  * defaultdict
    * 初めて遭遇したkeyに対しては, default_factoryが引数なしで呼ばれる.
    * [ドキュメント](https://docs.python.org/3/library/collections.html#collections.defaultdict)

  * heapq.nlargest
    * `sorted(iterable, key=key, reverse=True)[:n]`と同じ動作をする
      * 内部的なアルゴリズムはもっと効率的.
      * [公式実装](https://github.com/python/cpython/blob/06292614ff7cef0ba28da6dfded58fb0e731b2e3/Lib/heapq.py#L411)
  
  * Quick Select
    * Quick Sortを途中までやるアルゴリズム
    * [Discordの該当箇所](https://discord.com/channels/1084280443945353267/1183683738635346001/1185972070165782688)

  * 今回はたまたま大丈夫だったが, 同率k位がたくさんあるとどうなるかまで思考を巡らせられると良かった.
    * https://github.com/potrue/leetcode/pull/9/files#r2083755650

  * bucket sortの解法
    * https://github.com/potrue/leetcode/pull/9/files#diff-dce85bf5bc3acb0f755f06a75043875e90f52eadc5e761421acc856335cfec86R55
    * https://github.com/t-ooka/leetcode/commit/fbde086fff574ad5ff59eb6d39992a1de646c481

  * 標準の辞書の順番
    * [公式ドキュメント](https://docs.python.org/3/library/stdtypes.html#dict:~:text=Dictionaries%20preserve%20insertion%20order.%20Note%20that%20updating%20a%20key%20does%20not%20affect%20the%20order.%20Keys%20added%20after%20deletion%20are%20inserted%20at%20the%20end.)
    * > Dictionaries preserve insertion order. Note that updating a key does not affect the order. Keys added after deletion are inserted at the end.

## Quick Selectの実装(今回の問題の解法ではなく, k番目に小さい値を返す)

* partitionの方法をLomutoにしないと, 正しい動作はしない

```python
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
```