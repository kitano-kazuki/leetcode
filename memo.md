# Step1

## アプローチ

* 隣り合う二つを同時に取ることはできない
* 複数人でお金を取る作戦を考える
    * 一人１件担当する
    * 自分の前の担当者がお金を取っていたら自分は取らない
    * 自分の前の担当者がお金を取っていなくても, 自分の次の人が取った方が儲かりそうなら自分は取らないこともある
    * 今後どうなるかわからないけど, 自分がとった場合ととらなかった場合で今まで稼いだ額を伝えておく必要はある
* DPで前から順番に処理をしていく
    * 直前を取っていた場合のお金の最大
    * 直前を取っていなかった場合のお金の最大
    * をそれぞれ更新
* 時間計算量: O(N)
    * 100 / 10^6 = 10^-4 sec = 0.1 ms
* 空間計算量: O(N)
    * 28 byte * 400 = 11200 byte 
    * 11200 / 1024 ~= 10KBくらい

## Code1-1 (DP)

```python
# solved: 3:33

class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        robbed_before = 0
        not_robbed_before = 0
        for num in nums:
            robbed_before, not_robbed_before = not_robbed_before + num, max(not_robbed_before, robbed_before)
        
        return max(robbed_before, not_robbed_before)

```

# Step2

## Step1のコードの修正

変更なし

```python
class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        robbed_before = 0
        not_robbed_before = 0
        for num in nums:
            robbed_before, not_robbed_before = not_robbed_before + num, max(not_robbed_before, robbed_before)
        
        return max(robbed_before, not_robbed_before)

```


## 他の思いつく解法

### メモ化再帰

メモ化していたら, 時間計算量はO(N)
メモ化していなかったら、計算量はどうなるだろうか.
f(n) = f(n - 1) + f(n - 2)
フィボナッチ数列だからf(100) = 1.6^100 / √5??
とんでもない量.
@Cacheを無くしたら案の定TLEした.

```python
from functools import cache


class Solution:
    def rob(self, nums: list[int]) -> int:
        
        @cache
        def rob_upto(end: int) -> int:
            if end < 0:
                return 0
            if end == 0:
                return nums[0]
            
            return max(rob_upto(end - 1), rob_upto(end - 2) + nums[end])

        return rob_upto(len(nums) - 1)

```


## 他の人のコード

* https://github.com/mamo3gr/arai60/pull/33
* https://github.com/Mike0121/LeetCode/pull/47
    * メモ化再帰
    * DP
        * 二つの変数を用意する方法と, 一次元配列を使用する方法
* https://github.com/naoto-iwase/leetcode/pull/40
    * グローバル変数のでメリットについて言及している

## 他の人のコメント

* inner functionについて
    * https://github.com/Mike0121/LeetCode/pull/47#discussion_r1799964450
        * > inner function は定義するたびにオブジェクトとして作り直されていることを確認して欲しいです。
    * 作り直されるのは呼び出される度では？？
        * PyFunctionObjectは定義時につくられる
        * PyFrameObjectは呼び出し時につくられる

* 発想の仕方について
    * https://github.com/Yoshiki-Iwasa/Arai60/pull/50/files/3046fa9275ad29e7ea77647922aef66f2a607c91#r1717915563
        * > 各家の前に、泥棒の手下が一人ずつ立って、前から伝言をもらって、最後のところで求めたい数字を知りたいとします。「伝言」の内容は「ここまで最大いくら取れる、俺の眼の前の家に盗みに入らないとすると最大いくら取れる」の二つだけじゃないですか。
    * ほぼ同じ発想を最初にできていたのが嬉しかった

* 変数の命名について
    * https://github.com/n6o/leetcode_arai60/pull/28#discussion_r2961477097
    * > 個人的には robbed_last, skipped_last が好みです。直前をスキップしている（盗んでいない）のだから、n が盗めるでしょう、という理屈が分かりやすいからです。

# Step3

## Code3-1 (DP)

```python
class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        robbed_last = 0
        skipped_last = 0
        for num in nums:
            robbed_last, skipped_last = skipped_last + num, max(robbed_last, skipped_last)
        
        return max(robbed_last, skipped_last)

```