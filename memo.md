# Step1

## アプローチ

* 一番小さいところで買って一番大きいところで売りたい
* 将来的に出てくる自分より大きいやつのなかで最大値を探したい
* 手作業でやるなら, 今見ているところごとに, その先に出てくる自分より大きい最大値を探したい
* O(N^2)かければ同じことができる
* ただ, 無駄が多い
    * めっちゃでかいものがあったとしたら, 自分より後ろの要素を全て見る必要もないはず
* 自分より後ろに存在する最大値を常に保存しておければ嬉しい
* Increasing Monotonous stackの使用も思いついたが, 最も大きいものだけわかればいいから今回は不要そう

## Code1-1 

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # max_price[i]: maximum price of prices[i:]
        max_price = [None] * len(prices)
        for i in range(len(prices) - 1, -1, -1):
            if i == len(prices) - 1:
                max_price[i] = prices[i]
            else:
                max_price[i] = max(prices[i], max_price[i + 1])

        max_profit = 0
        for i in range(len(prices) - 1):
            if max_price[i + 1] <= prices[i]:
                continue
            max_profit = max(max_profit, max_price[i + 1] - prices[i])
        
        return max_profit

```

# Step2

## Code2-1

* 修正なし

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        # max_price[i]: maximum price of prices[i:]
        max_price = [None] * len(prices)
        for i in range(len(prices) - 1, -1, -1):
            if i == len(prices) - 1:
                max_price[i] = prices[i]
            else:
                max_price[i] = max(prices[i], max_price[i + 1])

        max_profit = 0
        for i in range(len(prices) - 1):
            if max_price[i + 1] <= prices[i]:
                continue
            max_profit = max(max_profit, max_price[i + 1] - prices[i])
        
        return max_profit

```

## 他の人のコード


* https://github.com/olsen-blue/Arai60/pull/37/
    * 前から見て最小値を記録する方法
* https://github.com/naoto-iwase/leetcode/pull/42
    * 同上
    * itertools.isliceを使っている
* https://github.com/mamo3gr/arai60/pull/35
    * 前から見て最小値を記録する方法

## 他の人のコメント

* 前から見るか, 後ろから見るか
    * https://github.com/fhiyo/leetcode/pull/38/files#r1667641801
        * > 自分は前からpricesを見ていくほうが自然だと思います。あえてreverseして処理する必要性がないかなと思いました。
    * 自分は逆に後ろからの方が自然だと思った. 手作業を考えた時に「自分の見ている株価以降で登場する最大値を知りたい」があるので.
* `prices`が空の時
    * https://discord.com/channels/1084280443945353267/1206101582861697046/1219181674038820945
        * > prices が空の場合は、何を返すことが想定されているでしょうか。
        * > これはどう答えてもいい問題です。ただ、if not prices: の処理を先頭に書くことにすると、INT_MAX などを使わずに、prices[0] が使えるようになります。

## Code2-2 (track min)

```python
from itertools import islice


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            raise ValueError("given array is empty")

        max_profit = 0
        min_price = prices[0]
        for price in islice(prices, 1, len(prices)):
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit

```

## Code2-3 (recursion)

* `cache`をつけることで, 計算量はO(N)にできる. 
    * stateの種類 * pricesの長さ
* `cache`をつけなかったら計算量はどうなるのだろうか
    * 最悪の場合は配列の最後まで`state`が`Empty`で渡され続ける時
    * O(2^N)になりそう

```python
from enum import Enum
from functools import cache

class State(Enum):
    EMPTY = 0
    HOLD = 1


class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        @cache
        def max_profit_with_state(day: int, state: State) -> int:
            if day == len(prices):
                return 0
                
            if state == State.EMPTY:
                return max(
                    max_profit_with_state(day + 1, State.EMPTY),
                    -prices[day] + max_profit_with_state(day + 1, State.HOLD)
                )
            if state == State.HOLD:
                return max(
                    max_profit_with_state(day + 1, State.HOLD),
                    prices[day]
                )
        
        return max_profit_with_state(0, State.EMPTY)

```

# Step3

## Code3-2 (track min)

```python

```