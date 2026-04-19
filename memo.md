# Step1

## アプローチ

### 最初に思いついた解放 (谷間探し)

* 121.best-time-to-buy-and-sell-stockの, 何回も購入&売却をできるようにしたバージョン
* 山登りを考えた時に, 登る標高の合計が高くなる区間を列挙する
* 各谷から頂点までを繰り返し登るようにすればいい
* 各山の地点ごとに, 両サイドの高さを見ればいいのでO(N)で頂点か谷かを判定可能
* 時間計算量: O(N) -> 10^4 / 10^6 ~= 0.01 sec程度の実行時間
* 空間計算量: O(1)


### 他の解法1 (再帰)

* 121の問題でもやったが, 再帰呼び出しで今の日付と今の株の保持状態から最大の利益を出すことはできそう
* メモ化することは大前提
    * メモ化しないときの計算量
        * 各日付の担当者は, 次の日付に対して, 買った場合と, 買わなかった場合それぞれで計算をお願いする.
        * 2^Nほどパターンを計算する
    * メモ化した時の計算量
        * 各日付, 状態(株を持っている, 株をすでに売っている)ごとに状態が存在するので O(N)
    * メモ化した時の空間計算量
        * 各日付　状態ごとに値を計算するので O(N)
        * 再帰の深さも O(N)
        * 10^4だと,　デフォルトの再帰上限(=1000)には引っかかる

### 他の解法2 (DP)

* メモ化再帰の代わりにDPにすることもできる
    * 日付iから最終日までに出せる最大の利益を考える
        * 株を持っている場合 A_i
        * 株を持っていない場合 B_i
    * A_(i-1) = max(A_i, prices[i-1] + B_i)
    * B_(i-1) = max(-prices[i-1] + A_i, B_i)
* 時間計算量: O(N)
* 空間計算量: O(N)

## Code1-1 (Vally)

```python
# solved: 14:56
import enum


class Solution:

    class _GradientState(enum.Enum):
        SLOPE = 0
        VALLEY = 1
        EDGE = 2
        
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        def _calculate_gradient_state(array: list[int], index: int) -> Solution._GradientState:
            left_height = array[index - 1] if index - 1 >= 0 else float("inf")
            right_height = array[index + 1] if index + 1 < len(array) else float("-inf")
            if left_height < array[index] < right_height or left_height > array[index] > right_height:
                return Solution._GradientState.SLOPE
            if left_height >= array[index] and array[index] < right_height:
                return Solution._GradientState.VALLEY
            if left_height < array[index] and array[index] >= right_height:
                return Solution._GradientState.EDGE
            assert True, "unreachable"

        profit = 0
        for i in range(len(prices)):
            gradient_state = _calculate_gradient_state(prices, i)
            if gradient_state == Solution._GradientState.SLOPE:
                continue
            if gradient_state == Solution._GradientState.VALLEY:
                profit -= prices[i]
                continue
            if gradient_state == Solution._GradientState.EDGE:
                profit += prices[i]
                continue
        
        return profit
            
```

## Code1-2 (recursion)

```python
# solved: 2:53
import functools


class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        @functools.cache
        def max_profit_with_state(day: int, has_stock: bool) -> int:
            if day == len(prices) - 1:
                return prices[day] if has_stock else 0

            if has_stock:
                return max(
                    prices[day] + max_profit_with_state(day + 1, False),
                    max_profit_with_state(day + 1, True)
                )
            
            return max(
                -prices[day] + max_profit_with_state(day + 1, True),
                max_profit_with_state(day + 1, False)
            )

        return max_profit_with_state(0, False)
```

## Code1-3 (dp)

```python
class Solution:

    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        EMPTY_STOCK_STATE = 0
        HOLDING_STOCK_STATE = 1
        maximum_profit_from_today = [[None, None] for _ in range(len(prices))]
        maximum_profit_from_today[-1][EMPTY_STOCK_STATE] = 0
        maximum_profit_from_today[-1][HOLDING_STOCK_STATE] = prices[-1]
        for i in range(len(prices) - 2, -1, -1):
            maximum_profit_from_today[i][EMPTY_STOCK_STATE] = max(
                maximum_profit_from_today[i + 1][EMPTY_STOCK_STATE], 
                -prices[i] + maximum_profit_from_today[i + 1][HOLDING_STOCK_STATE]
            )
            maximum_profit_from_today[i][HOLDING_STOCK_STATE] = max(
                prices[i]  + maximum_profit_from_today[i + 1][EMPTY_STOCK_STATE],
                maximum_profit_from_today[i + 1][HOLDING_STOCK_STATE]
            )

        return maximum_profit_from_today[0][EMPTY_STOCK_STATE]
            
```