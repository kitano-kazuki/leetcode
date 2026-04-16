# Step1

## 問題

```
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 10^9.

1 <= m, n <= 100
```

## アプローチ

* 自分の上と左がわかっていたら, 自分のマスへの行き方は上と左の行き方のパターン数を足した数のパターンがある
* 時間計算量: O(m * n)なので, 実行時間は 10^4 / 10^6 = 0.01秒ほど
* 空間計算量: O(m * n)なので, 28 byte(Pythonのintオブジェクト)  * 10^4 ~= 2.8 * 10^5 = 300 KBくらい

## Code1-1 (DP)

```python
# solved: 5:10

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        patterns = [[0] * (n + 1) for _ in range(m + 1)]
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if row == 1 and col == 1:
                    patterns[row][col] = 1
                    continue
                patterns[row][col] = patterns[row - 1][col] + patterns[row][col - 1]
        return patterns[m][n]

```

# Step2

## Code2-1 (DP)

* 変更なし

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        patterns = [[0] * (n + 1) for _ in range(m + 1)]
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if row == 1 and col == 1:
                    patterns[row][col] = 1
                    continue
                patterns[row][col] = patterns[row - 1][col] + patterns[row][col - 1]
        return patterns[m][n]


```

## 他の人のコード

* https://github.com/mamo3gr/arai60/pull/31
    * 直接 Combinationを数える方法もある
    * lru_cache decoratorで再帰のメモ化もできる
    * 上の行から２次元配列を埋めているのであれば, 直前の行の情報だけ保持していれば十分
    * 空間計算量をO(m * n) -> O(2 * n) -> O(n)とすることができる
* https://github.com/naoto-iwase/leetcode/pull/38


## 他の人のコメント

* lru_cacheよりもcacheの方がいい
    * https://github.com/tom4649/Coding/pull/31#discussion_r3003990090
* メモリ使用量が許容範囲内ならあえて2次元DPにする選択肢もある
    * https://github.com/n6o/leetcode_arai60/pull/26#pullrequestreview-3950600777
* 無意識に使っていたが`col`は略称だった
    * https://github.com/colorbox/leetcode/pull/46#discussion_r2617214967
* m, nが負で与えられた時に例外処理をする
    * https://github.com/t9a-dev/LeetCode_arai60/pull/33#discussion_r2548391322
* メモ化しなかった時の再帰の計算量の見積もり
    * https://github.com/garunitule/coding_practice/pull/33#discussion_r2396754924
    * https://github.com/olsen-blue/Arai60/pull/33#discussion_r1966730122
    * https://github.com/hroc135/leetcode/pull/33#discussion_r1899009212

## Code2-2 (Recursion + Cache)

```python
import functools


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @functools.cache
        def unique_paths_helper(m, n) -> int:
            if m == 1 or n == 1:
                return 1
            return unique_paths_helper(m - 1, n) + unique_paths_helper(m, n - 1)

        return unique_paths_helper(m, n)


```

## Code2-3 (Math)

```python
import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb((m  + n - 2), m - 1)

```