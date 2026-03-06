# Step1

## アプローチ

* すべてのパターンを列挙する
    * subarrayの開始点と終了点のそれぞれを変えながら見る O(N^2)
    * 開始点と終了点が決まったら和を計算する O(N)
    * 計算量: O(N^3)
    * 和の計算については, あらかじめprefixsumを計算していれば O(1)に抑えることが可能
    * 計算量: O(N^2)
* prefix_sumsをあらかじめ用意しておく. 各開始点ごとに, prefix_sumを元に終了点を辞書から探す.
    * prefix_sumの構築 O(N)
    * 各開始点ごとの和がkになるようにするための終了点の探索 O(1)
    * 全ての開始点を調べる O(N)
    * 計算量: O(N)
        * 追記: リストに終了点の候補を入れている関係で終了点の探索はO(N)になっていた. トータルではO(N^2). 
        * 追記: Step2で二分探索を使用してトータルを O(NlogN)にした.


## Code1-1

```python
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        n = len(nums)
        prefix_sum_to_idx = defaultdict(list)
        prefix_sum = [0] * n
        for i in range(n):
            prev_prefix_sum = prefix_sum[i - 1] if i > 0 else 0
            prefix_sum[i] = prev_prefix_sum + nums[i]
            prefix_sum_to_idx[prefix_sum[i]].append(i)

        result = 0

        if k in prefix_sum_to_idx:
            result += len(prefix_sum_to_idx[k])

        for start in range(n):
            prefix_sum_for_k = k + prefix_sum[start]
            if prefix_sum_for_k not in prefix_sum_to_idx:
                continue
            end_idx_candidates =  prefix_sum_to_idx[prefix_sum_for_k]
            for end_idx_candidate in end_idx_candidates:
                if start < end_idx_candidate:
                    result += 1
        
        return result

```


# Step2

## Code2-1 (O(NlogN): 開始点を基準に探索)

* 二分探索を使用

```python
from collections import defaultdict
import bisect

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        prefix_sum_to_idx = defaultdict(list)
        prefix_sum = [0] * n
        for i in range(n):
            prev_prefix_sum = prefix_sum[i - 1] if i > 0 else 0
            prefix_sum[i] = prev_prefix_sum + nums[i]
            prefix_sum_to_idx[prefix_sum[i]].append(i)

        result = 0

        if k in prefix_sum_to_idx:
            result += len(prefix_sum_to_idx[k])

        for start_idx in range(n):
            prefix_sum_for_k = k + prefix_sum[start_idx]
            if prefix_sum_for_k not in prefix_sum_to_idx:
                continue
            end_idx_candidates =  prefix_sum_to_idx[prefix_sum_for_k]
            boundary_idx = bisect.bisect_right(end_idx_candidates, start_idx)
            result += len(end_idx_candidates) - boundary_idx

        return result

```

## Code2-2 (O(N):終了点を基準に探索)

* 次項記載のMemoを元に解法を知った.

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum_sum = 0
        sum_to_count = {0: 1}
        result = 0
        for num in nums:
            cum_sum += num
            target_sum = cum_sum - k
            if target_sum in sum_to_count:
                result += sum_to_count[target_sum]
            sum_to_count.setdefault(cum_sum, 0)
            sum_to_count[cum_sum] += 1
        return result

```


# Memo

## O(N)のアルゴリズム

https://github.com/ryosuketc/leetcode_arai60/pull/16/files#r2109771699
```
標高差が ABCDE の5つの駅があって、それぞれの標高差がすべて 1 m です。([1, 1, 1, 1])
高さが 3 m 違う駅の区間を見つけてください。

A の標高を 1000 m としましょう。電車に乗るときに、標高とその駅を書き込んだ手帳を用意します。
1000 m A

B 駅につきます。はて、ここの標高は 1001 m である。ということは、標高が 998 m の駅があればいいんだな。うーん。ないな。じゃあ、B 駅の情報を手帳に書き込むか。
1000 m A
1001 m B

C 駅につきます。はて、ここの標高は 1002 m である。ということは、標高が 999 m の駅があればいいんだな。うーん。ないな。じゃあ、C 駅の情報を手帳に書き込むか。

D 駅につきます。はて、ここの標高は 1003 m である。ということは、標高が 1000 m の駅があればいいんだな。A 駅か。じゃあ、A と D は条件を満たすな。じゃあ、D 駅の情報を手帳に書き込むか。
```

確かに, 今見ているものを後ろの端点として, それまでに開始点が存在したかどうか見るようにすればO(N)で済む.

# Step3

```python
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cum_sum = 0
        sum_to_count = defaultdict(int)
        sum_to_count[0] = 1

        result = 0
        for num in nums:
            cum_sum += num
            target_sum = cum_sum - k
            if target_sum in sum_to_count:
                result += sum_to_count[target_sum]
            sum_to_count[cum_sum] += 1

        return result

```