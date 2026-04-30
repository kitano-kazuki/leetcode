# Step1

## アプローチ

* capcityを変えて行った時にどこかのポイントで運べるか運べないかが切り替わる
* 二分探索でその切り替わる場所を探す
* weightsのminとmaxの差は最大で, N * 500 - 1だからNとして計算量を考える時, 二分探索の範囲はNとしてよさそう
* 運べるかどうかの判定はO(N)でGreedyにやればいいかな. 二分探索を使う方法もある
* 全体だとO(NlogN) or O(D(logN)^2)
    * Dは`days`とする
* 実行時間は 10^4 * log(10^4) ~= 0.1 secくらい
* 運べるかどうかの判定ってもう少し効率的にできないかな？？
    * prefix_sum使うくらいか？？
    * prefix_sum使った上で二分探索をday回やるとか

## Code1-1 (Binary Search)

```python
import bisect


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        if not weights:
            return 0

        weight_prefix_sum = [0] * len(weights)
        weight_prefix_sum[0] = weights[0]
        for i in range(1, len(weights)):
            weight_prefix_sum[i] = weight_prefix_sum[i - 1] + weights[i]

        min_capacity = min(weights)
        max_capacity = weight_prefix_sum[-1]
        
        while min_capacity < max_capacity:
            mid = (min_capacity + max_capacity) // 2
            if self._is_shippable(mid, days, weight_prefix_sum):
                max_capacity = mid
            else:
                min_capacity = mid + 1
        
        return min_capacity

    def _is_shippable(self, capacity, days, weight_prefix_sum) -> bool:
        weight_begin = 0
        for _ in range(days):
            if weight_begin == 0:
                weight_end = bisect.bisect_right(
                    weight_prefix_sum, 
                    capacity)
            else:
                weight_end = bisect.bisect_right(
                    weight_prefix_sum, 
                    capacity, 
                    lo=weight_begin,
                    key=lambda w: w - weight_prefix_sum[weight_begin - 1])
                
            if weight_end == len(weight_prefix_sum):
                return True

            weight_begin = weight_end

        return False

```

# Step2

## Code2-1 (Binary Search)

* `_is_shippable`は二通りの実装がありそう
    * days = D, len(weights) = Nとする
    * 今回のように`days`回二分探索を行う方法
        * O(DlogN)
    * 前から順番に和を累積する. capacityを超えたら必要な日付を増加させて和を0にリセット
        * O(N)
    * Dが大きい場合は後者の方がいい
    * 逆に, Dが小さくてNが大きい倍は今回の方法の方がいい

```python
import bisect


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        if not weights:
            return 0

        # weight_prefix_sum[i] = weights[0] + ... + weights[i]
        weight_prefix_sum = [0] * len(weights)
        weight_prefix_sum[0] = weights[0]
        for i in range(1, len(weights)):
            weight_prefix_sum[i] = weight_prefix_sum[i - 1] + weights[i]

        min_capacity = min(weights)
        max_capacity = weight_prefix_sum[-1]
        
        # 運べる最小を二分探索で探す
        while min_capacity < max_capacity:
            mid = (min_capacity + max_capacity) // 2
            if self._is_shippable(mid, days, weight_prefix_sum):
                max_capacity = mid
            else:
                min_capacity = mid + 1
        
        return min_capacity

    def _is_shippable(self, capacity, days, weight_prefix_sum) -> bool:
        weight_begin = 0
        for _ in range(days):
            if weight_begin == 0:
                weight_end = bisect.bisect_right(
                    weight_prefix_sum, 
                    capacity)
            else:
                weight_end = bisect.bisect_right(
                    weight_prefix_sum, 
                    capacity, 
                    lo=weight_begin,
                    key=lambda w: w - weight_prefix_sum[weight_begin - 1])
                
            if weight_end == len(weight_prefix_sum):
                return True

            weight_begin = weight_end

        return False

``` 

# Step3

## 他の人のコードを見る

* https://github.com/olsen-blue/Arai60/pull/44
    * 解法はほぼ同じ
    * `is_shippable`の処理は前からリニアに見ていく方法: O(N)
    * bisect_leftに, range(max(weights), sum(weights) + 1)の配列を渡して, Trueとなる最小のindexを探す方法もある
* https://github.com/naoto-iwase/leetcode/pull/27
    * step1の実装では、自分と同じく`is_shippable`で`days`回数二分探索を行っていた
* https://github.com/mamo3gr/arai60/pull/42

## 他の人のコメントを読む

* https://github.com/ryoooooory/LeetCode/pull/46#discussion_r2659011235
    * > 私も 10^8-10^9 くらいで見積もりそうですが、しかし、一般にソフトウェアの速度は保守的に見積もったほうがいいんですよね。(予想外に速くて困ることはあまりないが逆は困ることがあるので。)
    * 計算量の見積もりは少し余裕を持った方がいい

## 気になった実装をしてみる

### Code3-2 (Bisect lib)

* `range`は今までジェネレータだと思っていたがそうではなかった.
* > The advantage of the range type over a regular list or tuple is that a range object will always take the same (small) amount of memory, no matter the size of the range it represents (as it only stores the start, stop and step values, calculating individual items and subranges as needed).
* > Range objects implement the collections.abc.Sequence ABC, and provide features such as containment tests, element index lookup, slicing and support for negative indices

* `capacity_range = range(min_capacity, max_capacity)`を`capacity_range = list(range(min_capacity, max_capacity))`にするとMemory Limie Exceededになった
* 500 * 5 * 10^4 * 28 byte ~= 10^8 ~ 10^9 byte ~= 0.1 ~ 1 GB
    * 厳しくない？？？ MemoryLimitにかかるの1GBとかだと思っていた。厳しい方で見積もって1GBだからMemory Limitにかからない気もしていた
        * LeetCodeのMemoryLimitが小さい？
        * 見積もりが違う??
        * わかる人教えてください


```python
import bisect


class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        if not weights:
            return -1

        def is_shippable(capacity: int) -> bool:
            spent_days = 1
            weights_on_ship = 0
            for i in range(len(weights)):
                if weights_on_ship + weights[i] <= capacity:
                    weights_on_ship += weights[i]
                    continue

                spent_days += 1
                if spent_days > days:
                    return False

                weights_on_ship = weights[i]

            return True
        
        min_capacity = max(weights)
        max_capacity = sum(weights) + 1
        capacity_range = range(min_capacity, max_capacity)
        index = bisect.bisect_left(capacity_range, True, key=is_shippable)
        return capacity_range[index]


```

# Step4

## Code4-1 (Binary Search)

```python
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        if not weights:
            return -1

        min_capacity = max(weights)
        max_capacity = sum(weights) + 1
        while min_capacity < max_capacity:
            mid = (min_capacity + max_capacity) // 2
            if self._is_shippable(mid, weights, days):
                max_capacity = mid
            else:
                min_capacity = mid + 1
        
        return min_capacity
    
    def _is_shippable(self, capacity, weights, days):
        spent_days = 1
        weights_on_ship = 0
        for i in range(len(weights)):
            if weights_on_ship + weights[i] <= capacity:
                weights_on_ship += weights[i]
                continue
                
            spent_days += 1
            weights_on_ship = weights[i]
        
        return spent_days <= days

```