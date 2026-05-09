# Step1

## アプローチ

* n行k番目のシンボルは, n-1行{(k+1)//2}番目をもとに決まる
    * kが奇数の時は, n-1行目のシンボルと一緒
    * kが偶数の時は, n-1行目のシンボルと反対
* top-down的に求めたい答えから遡って探していく
    * loopでも再帰でも解けそう
    * 今回はloopでやってみる
* 計算量
    * 段数分処理を行う
    * O(N) : 30 / 10^6 ~= 10^-5 sec = 10 ns

## Code1-1

```python
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n <= 0:
            raise ValueError("n must be > 0")
        
        if k > 2 ** (n - 1):
            raise ValueError("k must be less than the number of symbols in the row")

        is_reverse = False
        row = n
        col = k
        while row > 1:
            if col % 2 == 0:
                is_reverse = not is_reverse
            row = row - 1
            col = (col + 1) // 2
        
        if is_reverse:
            return 1
        else:
            return 0
                
```

# Step2

* 引数として受けとった`n`, `k`は変えない方が読みやすそう

## Code2-1

```python
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n <= 0:
            raise ValueError("n must be > 0")
        
        # k > n行目のシンボル数
        if k > 2 ** (n - 1):
            raise ValueError("k must be less than the number of symbols in the row")

        is_reverse = False
        row = n
        col = k
        while row > 1:
            if col % 2 == 0:
                is_reverse = not is_reverse
            row = row - 1
            col = (col + 1) // 2
        
        if is_reverse:
            return 1
        else:
            return 0

```

# Step3

## 他の人のコードを読む

* https://github.com/olsen-blue/Arai60/pull/47
    * 解法2':反転ブロックの利用
        * n + 1行目のシンボル列は, 「n行目のシンボル列 + n行目のシンボル列の反転」となることを利用
        * マクロ的な視点で見ることで気づく解法
* https://github.com/naoto-iwase/leetcode/pull/47
    * 実装4
        * (k - 1)のbit表現で1の数を数えたら反転が何回起こっているかわかる
            * (k - 1)で0-based-indexにする.
            * 一つ上の行で見たい列は col // 2でアクセス可能
            * colが奇数だったら, 反転. colが偶数だったら反転はなし
            * colが奇数かどうかは, bitが1かどうかをみればいい
            * 2で割る動作はbitのシフトに対応
            * => すべてのbitをみて, 1が何個あるかみればいい

## 他の人のコメントを見る

* https://github.com/h1rosaka/arai60/pull/48/files#r2659245198
    * > (k + 1) // 2は切り上げ除算をしたいということだと思うので、意図を明確にするために(k + 2 - 1) // 2と書くのはありかと思いました。//を切り捨て除算の演算子として、(被除数 + 除数 - 1) // 除数で切り上げ除算になるという整数の離散性を使った公式ですね。
    * それやったら, math.ceil()のほうがわかりやすいか
* bitの個数の計算方法はハードウェアとソフトウェアでそれぞれ効率的な方法があるらしい
    * かるくこっちにまとめた.
    * https://kazuki.main.jp/?p=65

# Step4

```python
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n <= 0:
            raise ValueError("n must be > 0")
        
        # k > n行目のシンボル数
        if k > 2 ** (n - 1):
            raise ValueError("k must be less than the number of symbols in the row")

        is_reverse = False
        row = n
        col = k
        while row > 1:
            if col % 2 == 0:
                is_reverse = not is_reverse
            row = row - 1
            col = (col + 1) // 2
        
        if is_reverse:
            return 1
        else:
            return 0

```