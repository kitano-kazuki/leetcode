# Step1

## アプローチ

* `for`で`x`を`n`回かけるのが一番ナイーブな方法
    * O(N)
    * 2^31 / 10^6 ~= 1000 secくらい
* `x^(n/2)`が計算できれば、それ同士をかければ`x^n`になる
* 計算しなきゃいけない回数は`logN`回
    * log(2^31) / 10^6 ~= 10^-5 ~= 10ns くらい
* nが負の数もあり得る.
* nが整数以外はあり得ない
* nが2で割り切れない時は, 1を引いてから2で割る
* xは正も負もあり得る

## Code1-1

* `OverflowError: (34, 'Numerical result out of range')`になってしまった
* https://discuss.python.org/t/how-may-we-avoid-overflow-errors/14606/2
    * > The two methods behave differently because they are written differently, one uses the exponentiation operator ** and the other just uses multiplication.
    * `**`と`*`は処理が違うらしい

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:

        def mypow_helper(x: float, n: int) -> float:
            if n == 0:
                return 1
            if n == 1:
                return x

            if n % 2 == 0:
                return (mypow_helper(x, n // 2))**2
            else:
                return x * (mypow_helper(x, n // 2))**2
        
        is_negative = x < 0 and n % 2 == 1
        reverse = n < 0

        powed_value = mypow_helper(abs(x), abs(n))

        if reverse:
            powed_value = 1 / powed_value
        if is_negative:
            powed_value = -1 * powed_value
        
        return powed_value

```

## Code1-1 Modified

* `**`の代わりに`*`を使うようにしたらAC

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:

        def mypow_helper(x: float, n: int) -> float:
            if n == 0:
                return 1
            if n == 1:
                return x

            half_powed = mypow_helper(x, n // 2)
            if n % 2 == 0:
                return half_powed * half_powed
            else:
                return half_powed * half_powed * x
        
        is_negative = x < 0 and n % 2 == 1
        reverse = n < 0

        powed_value = mypow_helper(abs(x), abs(n))

        if reverse:
            powed_value = 1 / powed_value
        if is_negative:
            powed_value = -1 * powed_value
        
        return powed_value

```