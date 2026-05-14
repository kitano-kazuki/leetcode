# Step1

## アプローチ

* 全部正の数からなる配列が与えられる
* 合計が与えられたtarget以上になる区間のうち長さが一番短いものを答える
* 全部正だから, 一度validになったらvalidになり続けるしsliding windowが使えそう
* ただ, これが負の値も入ってくると, 一度validになった後にinvalidになり得るからsliding windowは使えない
* 負の値が入ってきても対応できるアルゴリズムはあるか
    * O(N^2)ですべてのstart, endのパターンについて和を見る
        * prefix_sumを使えばO(N^2)でできるけど, 今回はN=10^5なので数秒のオーダーで実行できない
    * O(N)でできるらしい
        * https://leetcode.com/problems/minimum-size-subarray-sum/solutions/3725912/generalization-for-negative-numbers-o-n-time-memory/
            * prefix_sumを作って, prefix_sum[j] - prefix_sum[i] >= targetとなり j - i + 1が最小となるようにしたい
            * prefix_sum[j]ごとに, `0~j-1`の`i`についてprefix_sum[i]をみる.
                * だけど、全部見る必要はない.
                * k < lとなるインデックスで, prefix_sum[k] >= prefix_sum[l]となっていたら, kはみなくていい
                    * 和が小さくなる上に, 長さも長くなっちゃう
            * prefix_sumが単調増加になるようにしておく
            * あとは一回答えを出すのに使った左側の端はその先で使う必要がない
                * 右側が伸びているので, 左側をそのままにしても答えとして短い長さはできない
        * これはstep2で実装しましょう

## Code1-1

* `left`は数え始める開始点
* `right`はこれから追加する予定の点

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:
            return 0

        left = 0
        right = 0
        current_sum = 0
        minimum_subarray_length = float("inf")
        while True:

            while current_sum < target:
            
                # 以降,和がtarget以上になることはない
                if right == len(nums):
                    if minimum_subarray_length == float("inf"):
                        return 0
                    else:
                        return minimum_subarray_length

                current_sum += nums[right]
                right += 1

            while current_sum >= target:
                minimum_subarray_length = min(minimum_subarray_length, right - left)

                if left == len(nums):
                    if minimum_subarray_length == float("inf"):
                        return 0
                    else:
                        return minimum_subarray_length

                current_sum -= nums[left]
                left += 1

```

# Step2

## Code2-1 (sliding window)

* 変更なし

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:
            return 0

        left = 0
        right = 0
        current_sum = 0
        minimum_subarray_length = float("inf")
        while True:

            while current_sum < target:
            
                # 以降,和がtarget以上になることはない
                if right == len(nums):
                    if minimum_subarray_length == float("inf"):
                        return 0
                    else:
                        return minimum_subarray_length

                current_sum += nums[right]
                right += 1

            while current_sum >= target:
                minimum_subarray_length = min(minimum_subarray_length, right - left)

                if left == len(nums):
                    if minimum_subarray_length == float("inf"):
                        return 0
                    else:
                        return minimum_subarray_length

                current_sum -= nums[left]
                left += 1

```

## Code2-2 (prefix sum)

* 負の数に対応させるアルゴリズム
* 以下の例はsliding windowだと解が見つからない
* [1,-5, 2], target=2
* prefix sumを用意する
    * [1, -4, -2]
    * 終点を固定して, その終点ごとに部分列がtarget以上になる開始点を探す
    * 終点のprefix_sumをxとすると, `x - target`以下の値をprefix_sumから探したい
    * 毎回終点ごとに, 終点までのすべてのprefixを確認していたら, 追加でO(N)かかってトータルでO(N^2)になる
    * 以下の最適化を行う
        * 見るべき値が最小になるように候補を昇順で並べる
        * 一度採用したprefix_sumのindexは以降採用されない
            * もしそれが以降で採用される場合
                * 開始点は変わらず、終点だけ後ろにいっているため, 長さは必ず長くなる
    * 全体で開始点も終了点も一回ずつしか訪れないためO(N)

```python
import collections
import dataclasses

@dataclasses.dataclass
class Candidate:
    index: int
    prefix_sum: int  # nums[0] + ... + nums[index]


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:
            return 0

        begin_candidates = collections.deque([Candidate(-1, 0)])
        accumulated_sum = 0
        minimum_subarray_length = float("inf")
        for end_index in range(len(nums)):
            accumulated_sum += nums[end_index]

            # 部分列の和がtarget以上になる開始点を採用
            while begin_candidates and accumulated_sum - begin_candidates[0].prefix_sum >= target:
                begin_candidate = begin_candidates.popleft()  # 採用した開始点は今後使わない
                subarray_length = end_index - begin_candidate.index
                minimum_subarray_length = min(minimum_subarray_length, subarray_length)
            
            # 現在の累積和以上の候補は不要
            while begin_candidates and begin_candidates[-1].prefix_sum >= accumulated_sum:
                begin_candidates.pop()
            begin_candidates.append(Candidate(end_index, accumulated_sum))

        if minimum_subarray_length == float("inf"):
            return 0
        else:
            return minimum_subarray_length

```

# Step3

## 他の人のコードを見る

### olsen-blue: https://github.com/olsen-blue/Arai60/pull/50

* 解法1 sliding window
    * 方針としては自分のコードと同じ
    * `while`の代わりに`for`を使用して右側の端点を動かす
    * 自然言語的なイメージ
        * 和がtarget以上だったら, 短い方がいいので左側の端点を縮める
        * その結果target未満になったら, また右側の端点を動かすフェーズに戻る
* 解放2 二分探索
    * prefix_sumを構築しておく
    * 現在見ている点を左の端点として, 右の端点になる値を二分探索で探す
    * 配列の要素が全部正だから, 単調増加となり二分探索が使える

### naoto-iwase: https://github.com/naoto-iwase/leetcode/pull/50

* sliding windowの解法
    * forループで回している


# Step4

## Code4-1 (Sliding Window)

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:
            return 0
        
        minimum_subarray_length = float("inf")
        left = 0
        current_sum = 0
        for right in range(len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                minimum_subarray_length = min(minimum_subarray_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        if minimum_subarray_length == float("inf"):
            return 0

        return minimum_subarray_length
                
```

## Code4-2 (Prefix sum)

```python
import dataclasses
import collections


@dataclasses.dataclass
class Candidate:
    index: int
    prefix_sum: int  # nums[0] + ... + nums[index]


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if not nums:
            return 0
        
        minimum_subarray_length = float("inf")
        begin_candidates = collections.deque([Candidate(-1, 0)])
        accumulated_sum = 0
        for end_index in range(len(nums)):
            accumulated_sum += nums[end_index]

            while begin_candidates and accumulated_sum - begin_candidates[0].prefix_sum >= target:
                begin_candidate = begin_candidates.popleft()
                subarray_length = end_index - begin_candidate.index
                minimum_subarray_length = min(minimum_subarray_length, subarray_length)
            
            while begin_candidates and begin_candidates[-1].prefix_sum >= accumulated_sum:
                begin_candidates.pop()
            begin_candidates.append(Candidate(end_index, accumulated_sum))

        if minimum_subarray_length == float("inf"):
            return 0
        
        return minimum_subarray_length
                

```