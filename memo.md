# Step1

## アプローチ

* コンパイラのレジスタ割り当ての時のグラフ彩色問題を思い出した
* 隣り合うポストが連続して３つ以上同じ色になってはだめ
* 再帰あるいはDPで解けそう
* m個塗った時, 
    * `m-1`個目と`m`個目が同じ色である塗り方をA_m
    * `m-1`個目と`m`個目が違う色である塗り方をB_m
* m+1個塗った時の塗り方は
    * A_m+1 = B_m
    * B_m+1 = A_m * (k - 1) + B_m * (k - 1)

## Code1-1 (DP)

```python
# solved: 6:47

class Solution:
    def num_ways(self, n: int, k: int) -> int:
        if n == 1:
            return k

        patterns_same_color = [0] * n
        patterns_different_color = [0] * n

        patterns_same_color[0] = 0
        patterns_different_color[0] = k
        for i in range(1, n):
            patterns_same_color[i] = patterns_different_color[i - 1]
            patterns_different_color[i] = patterns_same_color[i - 1] * (k - 1) + patterns_different_color[i - 1] * (k - 1)
        
        return patterns_same_color[n - 1] + patterns_different_color[n - 1]

```

# Step2

## 他の人のコードを見る

* https://github.com/mamo3gr/arai60/pull/57/files
* https://github.com/Satorien/LeetCode/pull/30/files
    * 直前の値だけわかればいいので, 空間計算量をO(1)にすることもできる
* https://github.com/Satorien/LeetCode/pull/30/files
    * 与えられた`n`や`k`の例外処理を丁寧に行っている
* https://github.com/Fuminiton/LeetCode/pull/30/changes
    * メモ化再帰によるTopdownアプローチ


## Code2-1 (DP)

```python
class Solution:
    def num_ways(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k

        previous_two_same = k
        previous_two_different = k * (k - 1)
        for _ in range(2, n):
            temporary = previous_two_same
            previous_two_same = previous_two_different
            previous_two_different = temporary * (k - 1) + previous_two_different * (k - 1)
        
        return previous_two_same + previous_two_different

```

# Step3

## Code3-1 (DP)

```python
# 1st: 1:34
# 2nd: 4:26
# 3rd: 1:02


class Solution:
    def num_ways(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k * k
        
        previous_two_same = k
        previous_two_different = k * (k - 1)
        for _ in range(2, n):
            new_previous_two_same = previous_two_different
            new_previous_two_different = previous_two_same * (k - 1) + previous_two_different * (k - 1)
            previous_two_same = new_previous_two_same
            previous_two_different = new_previous_two_different
        return previous_two_same + previous_two_different

```