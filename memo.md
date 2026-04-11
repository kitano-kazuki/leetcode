# Step1

## アプローチ

* 一番ナイーブなのは, あらゆるsubsequenceのパターンを列挙すること
    * 2^n種類あるので, n=2500の時, log_10_(2^2500) = 2500 * log_10_2 = 750より, 10^750 => 絶対おわらん
    * 10^6ステップが1secだとすると, n * log_10_2 = 6となるnは20くらい
* 仕事を引き継いでもらってできないか考える
    * 何がわかっていればいい？？
        * これまでのLISの長さ = m
        * ↑を実現した時の値 = x
    * 何をすればいい？
        * 今見ている値がxよりも大きければ, mやxを更新する
        * そうでなかったら何もしない??
            * `1 4 100 5 7 8`とかでうまくいかない
        * 長さ1の時のx, 長さ2の時のx...とかで保存しておく??
        * うまくいきそうだけど, 計算量が気になる
            * 事前に長さnの配列(=l)を用意
            * 各iにつき, nums[i]とlを見比べながら更新
            * O(n^2)
            * n=2.5 * 10^3なので, n^2 = 7 * 10^6くらい
            * 10^6 steps / 1secだとちょうど1秒くらいで終わる
            * これでいきましょう

## Code1-1

```python
# solved: 10:18


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        # minimum_values[i] represents the minimum tail value among possile LIS with length i
        minimum_values = [float("inf")] * (n + 1)
        minimum_values[0] = float("-inf")

        for i in range(n):
            for length in range(1, i + 2):
                if minimum_values[length - 1] < nums[i] and nums[i] < minimum_values[length]:
                    minimum_values[length] = nums[i]
        
        for i in range(n, -1, -1):
            if minimum_values[i] != float("inf"):
                return i

```

# Step2

## Code2-2

```python
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        # minimum_values[i] represents the minimum tail value among possile LIS with length i
        minimum_values = [float("inf")] * (n + 1)
        minimum_values[0] = float("-inf")

        for num_index in range(n):
            num_of_elements = num_index + 1
            for length in range(1, num_of_elements + 1):
                if minimum_values[length - 1] < nums[num_index]:
                    minimum_values[length] = min(nums[num_index], minimum_values[length])
        
        for i in range(n, -1, -1):
            if minimum_values[i] != float("inf"):
                return i

```

## 他の人のコード

* https://github.com/mamo3gr/arai60/pull/29
    * step3では二つの解法を用いている
        * 解法1
            * 自分のコードで`minimum_values`としていたものは以下のように工夫して表現できた
                * 最初からn個分確保しない. 単調増加列となる場合に配列に`append`する.
                * 配列内で更新が必要な部分は, 配列の中でなるべく右側でかつ`nums[i]`より大きい数があった時
                    * 二分探索を活用できる
        * 解法2
            * 他にも各iごとに以下の処理を行う方法もある
                * 今までに作成した単調増加列を保持してあるものとする
                * それら全てに対して, 末尾に今の数を追加できそうなら追加する.
                * その回で最も長くなる単調増加列を、新たに保持するリストに追加

* https://github.com/Satorien/LeetCode/pull/31
    * mamo3grの解法1と同様.
    * bisect_leftを自前で実装.
* https://github.com/naoto-iwase/leetcode/pull/36
    * mamo3grの解法1と同様.

## 過去のコメント

* https://discord.com/channels/1084280443945353267/1200089668901937312/1209563502407065602
    * 3-5番は、セグメント木 (BITでも可) を使います。セグメント木は、ある範囲の MAX を計算させることができます。nums[i] の範囲は、-10^4 <= nums[i] <= 10^4 なので、この範囲に対してセグメント木を構築します。

# 調べた上で色々実装

## 二分探索を活用

```python

class Solution:
    def binary_search(self, array: list[int], value: int) -> int:
        left_inclusive = 0
        right_exclusive = len(array)
        while left_inclusive < right_exclusive:
            mid = (left_inclusive + right_exclusive) // 2
            if value <= array[mid]:
                right_exclusive = mid
            else:
                left_inclusive = mid + 1
        return right_exclusive

    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # ith element is the minimum tail value for increasing subsequence of length i
        minimum_tails = [float("-inf")]

        for num in nums:
            index = self.binary_search(minimum_tails, num)
            if index == len(minimum_tails):
                minimum_tails.append(num)
            else:
                minimum_tails[index] = num
        
        return len(minimum_tails) - 1

```

## 各iごとに単調増加列を用意

```python
from dataclasses import dataclass


@dataclass
class IncreasingSequence:
    tail_value: int
    length: int


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        increasing_subsequences = []

        for num in nums:
            longest_tail_length = 1
            for increasing_subsequence in increasing_subsequences:
                if increasing_subsequence.tail_value < num:
                    longest_tail_length = max(longest_tail_length, increasing_subsequence.length + 1)
            increasing_subsequences.append(IncreasingSequence(num, longest_tail_length))

        return max([sequence.length for sequence in increasing_subsequences])

```

## Segment Tree

### メモ

BITとSegment Treeの使い分けは実装の簡単さとメモリ使用量の削減.
Segment TreeでBITの機能を果たすこともできる

https://codeforces.com/blog/entry/6847
> It is possible to simulate a BIT using a segment tree, so you might ask: why would you prefer a BIT over a segment tree? Well, a BIT is much easier to code and requires less memory. So if a BIT is enough to solve the problem, go for it, else try with a segment tree.

https://www.reddit.com/r/compsci/comments/1852b98/in_which_situation_should_a_segmented_tree_should/
> While BIT is more memory-efficient and faster to construct, Segmented Trees offer greater flexibility in handling various types of queries and updates.

### 実装の参考

* [Algorithms for Competitive Programing. Segment Tree](https://cp-algorithms.com/data_structures/segment_tree.html)
* [naoto-iwase/leetcode. pull request 36.](https://github.com/naoto-iwase/leetcode/pull/36/files)
* [leetcode. DP, Binary Search, BIT, Segment Tree Solutions - Picture explain - O(NlogN)](https://leetcode.com/problems/longest-increasing-subsequence/solutions/1326308/c-python-dp-binary-search-bit-segment-tree-solutions-picture-explain-o-nlogn/)

### 実装

```python
from dataclasses import dataclass


@dataclass
class SegmentTreeVertex:
    index: int
    left_inclusive: int
    right_inclusive: int



# SegmentTree for getting maximum value between given left and right.
class SegmentTreeMax:
    def __init__(self, size):
        self.size = size
        self.tree = [None] * (size * 4) # 1-indexed
    
    def build(self, array):
        self._build(array, SegmentTreeVertex(1, 0, self.size - 1))

    def _build(self, array, vertex: SegmentTreeVertex):
        if vertex.left_inclusive == vertex.right_inclusive:
            self.tree[vertex.index] = array[vertex.left_inclusive]
            return

        mid = (vertex.left_inclusive + vertex.right_inclusive) // 2
        left_child = SegmentTreeVertex(vertex.index * 2, vertex.left_inclusive, mid)
        self._build(array, left_child)
        right_child = SegmentTreeVertex(vertex.index * 2 + 1, mid + 1, vertex.right_inclusive)
        self._build(array, right_child)
        self.tree[vertex.index] = max(self.tree[left_child.index], self.tree[right_child.index])
        return

    def get_max(self, query_left_inclusive: int, query_right_inclusive: int) -> int:
        return self._get_max(SegmentTreeVertex(1, 0, self.size - 1), query_left_inclusive, query_right_inclusive)
    
    def _get_max(self, queried_vertex: SegmentTreeVertex, query_left_inclusive: int, query_right_inclusive: int) -> int:
        if query_left_inclusive > query_right_inclusive:
            return 0
        if query_left_inclusive == queried_vertex.left_inclusive and query_right_inclusive == queried_vertex.right_inclusive:
            return self.tree[queried_vertex.index]
        mid = (queried_vertex.left_inclusive + queried_vertex.right_inclusive) // 2
        left_child = SegmentTreeVertex(queried_vertex.index * 2, queried_vertex.left_inclusive, mid)
        right_child = SegmentTreeVertex(queried_vertex.index * 2 + 1, mid + 1, queried_vertex.right_inclusive)
        return max(self._get_max(left_child, query_left_inclusive, min(mid, query_right_inclusive)), self._get_max(right_child, max(query_left_inclusive, mid + 1), query_right_inclusive))

        
    def update(self, position: int, new_value: int) -> None:
        self._update(SegmentTreeVertex(1, 0, self.size - 1), position, new_value)
        return

    def _update(self, vertex: SegmentTreeVertex, position: int, new_value: int):
        if vertex.left_inclusive == vertex.right_inclusive:
            self.tree[vertex.index] = new_value
            return

        mid = (vertex.left_inclusive + vertex.right_inclusive) // 2
        left_child = SegmentTreeVertex(vertex.index * 2, vertex.left_inclusive, mid)
        right_child = SegmentTreeVertex(vertex.index * 2 + 1, mid + 1, vertex.right_inclusive)
        if position <= mid:
            self._update(left_child, position, new_value)
        else:
            self._update(right_child, position, new_value)
        self.tree[vertex.index] = max(self.tree[left_child.index], self.tree[right_child.index])
        return



class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        ranks = self._convert_array_to_ranks(nums)

        # ith element represents the maximum LIS length ending at i(rank)
        maximum_LIS_lengthes = [0] * (len(set(ranks)) + 1)
        n = len(maximum_LIS_lengthes)

        segment_tree = SegmentTreeMax(n)
        segment_tree.build(maximum_LIS_lengthes)

        for rank in ranks:
            # the maximum LIS length ending at x(< rank)
            maximum_length_before = segment_tree.get_max(0, rank - 1)
            maximum_LIS_lengthes[rank] = maximum_length_before + 1
            segment_tree.update(rank, maximum_LIS_lengthes[rank])
        
        return max(maximum_LIS_lengthes)



    def _convert_array_to_ranks(self, array: list[int]) -> list[int]:
        unique_numbers = sorted(set(array))
        value_to_rank = {}
        rank = 1
        for unique_number in unique_numbers:
            value_to_rank[unique_number] = rank
            rank += 1
        return [value_to_rank[num] for num in array]

```