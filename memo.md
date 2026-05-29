# Step1

## アプローチ

* 各数字を, その桁の数の和に変換する. その結果一番小さい数を返す
* 普通に前から順番に計算していきながら、一番小さい数を保存しておく
* len(nums) <= 100
* nums[i] <= 10^4
* より, 10^2 * 4 / 10^6 ~= 10^-4 sec程度の実行時間
* ここまで1:49

## Code1-1

* AC: 1:51

```python
class Solution:
    def minElement(self, nums: List[int]) -> int:
        def calculate_sum_digits(num: int) -> int:
            sum_digits = 0
            while num > 0:
                sum_digits += num % 10
                num //= 10
            
            return sum_digits

        min_sum_digits = float("inf")
        for num in nums:
            sum_digits = calculate_sum_digits(num)
            min_sum_digits = min(min_sum_digits, sum_digits)
        
        return min_sum_digits
        
```

# Step2

## Code2-1

* 変更なし

```python
class Solution:
    def minElement(self, nums: List[int]) -> int:
        def calculate_sum_digits(num: int) -> int:
            sum_digits = 0
            while num > 0:
                sum_digits += num % 10
                num //= 10
            
            return sum_digits

        min_sum_digits = float("inf")
        for num in nums:
            sum_digits = calculate_sum_digits(num)
            min_sum_digits = min(min_sum_digits, sum_digits)
        
        return min_sum_digits
        
```

## 他の解法を見る

* 最初の初期化は, 37とすることもできる
    * nums[i]の最大値が`10000`なので, 各桁の和の最大は`9999`のとき

# Step3

## Code3-1

```python
class Solution:
    def minElement(self, nums: List[int]) -> int:
        def calculate_sum_digits(num: int) -> int:
            sum_digits = 0
            while num > 0:
                sum_digits += num % 10
                num //= 10
            return sum_digits

        min_sum_digits = float("inf")
        for num in nums:
            sum_digits = calculate_sum_digits(num)
            min_sum_digits = min(min_sum_digits, sum_digits)

        return min_sum_digits
        
```