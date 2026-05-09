# Step1

## アプローチ

* x^nを計算する
* n回ループを回すのが一番単純な方法
    * O(N)なので, 2^31 / 10^6 = 1000 secくらいかかりそう
* x^n = (x^(n/2))^2であることを利用すればO(logN)になる
    * log2^31 / 10^6 = 10^-5 secくらい
* loopでも再帰でもかけるので両方やるか

## Code1-1 (loop)

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n *= -1

        multiplier = 1
        while n > 1:
            if n % 2 == 1:
                multiplier *= x
            x = x * x
            n = n // 2

        x *= multiplier

        return x


```

## Code1-2 (Recursion)

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n *= -1

        def my_pow_helper(x: float, n: int) -> float:
            if n == 1:
                return x

            if n % 2 == 0:
                return my_pow_helper(x * x, n // 2)
            else:
                return my_pow_helper(x * x, n // 2) * x

        return my_pow_helper(x, n)


```



# Step2

## Code2-1 (loop)

* 変更なし
* 自然言語的に処理を説明すると
    * xのn乗を計算します
    * nが偶数だったら, (x^2)^(n/2)を計算するように引き継ぎます
    * nが奇数だったら, (x^2)^(n-1/2) * xを計算するように引き継ぎます
        * このとき余分にかけたxは最後にまとめてかけるようにします
* これってfloatのoverflowみたいにならないのかな.
* float(単精度)で表せる限界は, 2^127 * 1.9999... ~= 2^128のイメージだけど合っているか調べる
    * だいたいあっていそう
    * 指数部が表せる最大は, 255 - 1 = 254 (255に対応する値はinfとして特別枠). biasの127を引いて, 127.
    * 仮数部が表せる最大は, 1 + 1/2 + (1/2^2) + ... + (1/2^23)の等比数列の和を考えて
        * 1 * {(1 - (1/2)^24)/(1 - 1/2)} = 2 - 2^(-23)
    * よって, 2^127 * (2 - 2^(-23)) = 2^128 ~= 10^38くらい
* floatでoverflowは存在するのか.
    * IEEE 754より
        * > The overflow exception shall be signaled if and only if the destination format’s largest finite number is exceeded in magnitude by what would have been the rounded floating-point result (see Clause 4) were the exponent range unbounded. 
        * > The default result shall be determined by the rounding-direction attribute and the sign of the intermediate result as follows:
        * > a) roundTiesToEven and roundTiesToAway carry all overflows to ∞ with the sign of the intermediate result.
        * floatのoverflowは, 指数範囲が無限だと仮定して丸めた結果が, 浮動小数として表せる最大の値を超えた場合に起こる. overflow後の値は, 丸め方によって異なる. 多くのプログラミング言語で標準の最近接丸めではinfになる.
* 今回の問題で, overflowはおこりそうか
    * x^n <= 10^4という制限があるので起こり得ない.

```python

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n *= -1

        multiplier = 1
        while n > 1:
            if n % 2 == 1:
                multiplier *= x
            x = x * x
            n = n // 2

        x *= multiplier

        return x


```

# Step3

## 他の人のコードを見る

* https://github.com/olsen-blue/Arai60/pull/45
    * 解法2: whileループ(切り出し)
        * x^(1 + 2 + 4 + ... + 2^k)みたいにxにかかる乗数を2の冪乗に制限してloopで掛け算
    * 解法2':whileループ(ビット処理)
        * 自分のCode2-1(loop)と同様のアルゴリズム
* https://github.com/naoto-iwase/leetcode/pull/46 
    * 実装2
        * x^(2^0 + 2^2 + ... + 2^k)を考えた時,
        * x^(2^0) * x^(2^2) * ... になる
        * x^(2^k) = (x^(2^(k - 1)))^2であることを活用
* https://github.com/mamo3gr/arai60/pull/43
    * step3
        * naoto-iwase(実装2)と同様

## 上記を踏まえての実装

### Code3-3 (loop bit ver)

* 自然言語でのループ部分の引き継ぎの説明
    * x^(2^k)を計算します
    * nの2^kに対応するbitが0
        * 自分の役目は終了
        * 次に見るべきbitを引き継ぐ
    * nの2^kに対応するbitが1
        * 結果に対してx^(2^k)をかける
        * 次に見るべきbitを引き継ぐ

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        abs_n = abs(n)

        # nの各bitごとにx^(2^k)を乗算
        # n = 5(0b101) -> x^(2^0 * 1 + 2^1 * 0 + 2^2 * 1) = x^(2^0) * x^(2^2)
        selection_bit = 0b1
        powed_x = x
        result = 1
        while selection_bit <= abs_n:
            if selection_bit & abs_n > 0:
                result *= powed_x
            powed_x = powed_x * powed_x
            selection_bit = selection_bit << 1
        
        if n < 0:
            result = 1. / result
        
        return result
                
```

# Step4

## Code4-3 (loop bit ver)

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        abs_n = abs(n)

        selection_bit = 0b1
        powed_x = x
        result = 1
        while selection_bit <= abs_n:
            if selection_bit & abs_n > 0:
                result *= powed_x
            powed_x = powed_x * powed_x
            selection_bit = selection_bit << 1
        
        if n < 0:
            result = 1. / result
        
        return result

```