# Step1

## アプローチ

* 198.House robberに対して, 末尾と先頭がつながっている（円上に家が並ぶ）想定
* 1個目を取ったら一番最後は取れない
* 1個目をとらなかったら, 一番最後はとってもとらなくてもいい
* 1~n-1と2~nでそれぞれhouse robberの解を出せばいい
* O(N)で N <= 1000だから 1000 / 10^6 = 10^-3 = 1msくらい

## Code1-1 (DP)

```python
class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        robbed_without_last = self._rob_sequential_houses(nums, 0, len(nums) - 2)
        robbed_with_last = self._rob_sequential_houses(nums, 1, len(nums) - 1)
        return max(robbed_without_last, robbed_with_last)

    def _rob_sequential_houses(self, nums: list[int], start: int, end: int) -> int:
        if start > end:
            return 0

        robbed_last = 0
        skipped_last = 0
        for i in range(start, end + 1):
            robbed_last, skipped_last = skipped_last + nums[i], max(robbed_last, skipped_last)
        
        return max(robbed_last, skipped_last)
        
```

# Step2

## Code2-1 (DP)

* `robbed_with_last`だけだと, 最初の家を飛ばしていることが伝わらない. かつ, 最後の家を必ずrobしているかのように感じられる
* 他にいい命名も思いつかないので, コメントを追加
* でも結局, 関数を呼び出している引数を見たらわかる？？？

```python
class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        # when robbing houses in the range [0, n-2]
        robbed_without_last = self._rob_sequential_houses(nums, 0, len(nums) - 2)
        # when robbing houses in the range [1, n-1]
        robbed_with_last = self._rob_sequential_houses(nums, 1, len(nums) - 1)

        return max(robbed_without_last, robbed_with_last)

    def _rob_sequential_houses(self, nums: list[int], start: int, end: int) -> int:
        if start > end:
            return 0

        robbed_last = 0
        skipped_last = 0
        for i in range(start, end + 1):
            robbed_last, skipped_last = skipped_last + nums[i], max(robbed_last, skipped_last)
        
        return max(robbed_last, skipped_last)

``` 

## 他の人のコード

* https://github.com/olsen-blue/Arai60/pull/35
    * @cacheを自分で実装している
    * 再帰で実装しているけど, 考え方は同じ([0,n-2]と[1,n-1]の結果を利用)
    * 変数の命名で, `rob_without_init`とするのはわかりやすくていいかも
* https://github.com/naoto-iwase/leetcode/pull/41/files
* https://github.com/mamo3gr/arai60/pull/34


## 他の人のコメント

* 特になし

# Step3

## Code3-1 (DP)

```python
class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        robbed_without_tail = self._rob_houses_in_line(nums, 0, len(nums) - 2)
        robbed_without_head = self._rob_houses_in_line(nums, 1, len(nums) - 1)
    
        return max(robbed_without_head, robbed_without_tail)

    
    def _rob_houses_in_line(self, nums: list[int], start: int, end: int) -> int:
        if start > end:
            return 0
        if start == end:
            return nums[start]

        robbed_last = 0
        skipped_last = 0
        for i in range(start, end + 1):
            robbed_last, skipped_last = skipped_last + nums[i], max(robbed_last, skipped_last)
        
        return max(robbed_last, skipped_last)
            

```
