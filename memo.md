# Step1

## アプローチ

* 原点からの距離が近い順に`k`個の点を返す
* 普通に各点ごとの距離を計算, sortして先頭からk件だとどうか
    * 点の個数をNとする
    * O(N + NlogN) -> O(NlogN)
    * 10^4 * log10^4 / 10^6 ~= 10^-2 sec
* 2:11

## Code1-1

* 3:39でAC
* 変数名の改善とか, 上位k件だけのheapにするとかをstep2でやりたい

```python
import operator

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def calculate_distance(point: list[int]):
            return point[0]**2 + point[1]**2

        distances = []
        for point in points:
            distance = calculate_distance(point)
            distances.append((distance, [point[0], point[1]]))
        
        distances = sorted(distances, key=operator.itemgetter(0))

        return [d[1] for d in distances[:k]]
        
```

# Step2

## Code2-1

* O(Nlogk + k)にできた

```python
import operator
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def calculate_distance(point: list[int]):
            return point[0]**2 + point[1]**2

        topk_distances = []
        for point in points:
            distance = calculate_distance(point)
            if len(topk_distances) < k:
                heapq.heappush(topk_distances, (-distance, point))
                continue
            if distance >= abs(topk_distances[0][0]):
                continue
            heapq.heapreplace(topk_distances, (-distance, point))

        return [point for _, point in topk_distances]
        
```

## 他の人のPRを見る

* https://github.com/tom4649/Coding/pull/123
    * quick selectの解法があるらしい. 思いつかなかった
        * https://github.com/kitano-kazuki/leetcode/pull/87/changes
        * ここでもやっていたのに...
* https://github.com/huyfififi/coding-challenges/pull/28
    * max_heapについて
        * > 距離にマイナスがかかっていることが自明ではないため、コメントで補足するちょいと思いました。

## Code2-2 (Quick Select)

* 最悪の場合の計算量は, partitionで毎回その中の最大の要素を選んでいる場合で, O(N^2)
* 平均的には、O(N)
    * N + N / 2 +  N / 4 + ...

```python
import random


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def calculate_squared_distance(point: list[int]) -> int:
            x, y = point
            return x * x + y * y
        
        squared_distance_and_points = [(calculate_squared_distance(point), point) for point in points]

        self.quick_select(squared_distance_and_points, k - 1)

        return [point for _, point in squared_distance_and_points[:k]]


    def quick_select(self, array: list[tuple[int, Any]], k: int) -> None:

        def partition(left: int, right: int) -> int:
            pivot_index = random.randint(left, right)
            pivot = array[pivot_index][0]
            array[pivot_index], array[right] = array[right], array[pivot_index]

            partition_index = left
            for i in range(left, right):
                if array[i][0] < pivot:
                    array[i], array[partition_index] = array[partition_index], array[i]
                    partition_index += 1
            
            array[partition_index], array[right] = array[right], array[partition_index]
            
            # array[partition_index:]は>=pivot
            return partition_index

        def quick_select_helper(left: int, right: int) -> None:
            partition_index = partition(left, right)
            if partition_index == k:
                return
            elif partition_index > k:
                quick_select_helper(left, partition_index - 1)
                return
            else:
                quick_select_helper(partition_index + 1, right)
                return
        
        quick_select_helper(0, len(array) - 1)
        return
            
```

# Step3

## Code3-1

```python
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def calculate_squared_distance(point: list[int]) -> int:
            x, y = point
            return x * x + y * y
        
        # max heap: (-1 * squared_distance, point)
        k_nearest = []

        for point in points:
            squared_distance = calculate_squared_distance(point)
            if len(k_nearest) < k:
                heapq.heappush(k_nearest, (-squared_distance, point))
                continue
            if squared_distance >= abs(k_nearest[0][0]):
                continue
            heapq.heapreplace(k_nearest, (-squared_distance, point))
        
        return [point for _, point in k_nearest]

```