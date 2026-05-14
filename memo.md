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