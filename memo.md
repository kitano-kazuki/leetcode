# Step1

## アプローチ

* mapに数字ごとの出現回数を記録.
  * 全て記録し終わった後に出現回数の多い順に取り出し
    * ordered_mapとかpythonにあるのかな？
    * 自分の知っている知識でやるなら, heapにタプルで入れていく. 順番にk個取り出し
* 他の方法はパッと思いつかなかった.
* map -> heapの時間とか空間の見積もり
  * 要素数をnとする
  * O(n)で出現回数mapの構築
  * O(nlogn)で全ての出現回数と値のペアをheapに挿入.
  * O(klogn)で上位k件を取り出し.
  * 辞書の保存, heapともに, O(n)

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