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

  # 他の解法

  ## Bucket Sort
  
  ```python

  ```

  ## Quick Select

  ```python

  ```
  
