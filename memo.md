# Step1

## アプローチ

* 自分以外を掛け算した結果を保存したい
* 割り算を使ってはだめ, O(N)でやる
* 左からの累積積と右からの累積積を組み合わせたらいけそう(ヒントを見た)

## Code1-1

* AC: 12:53

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        left_accumulated_mul = [0] * len(nums)
        left_accumulated_mul[0] = nums[0]
        for i in range(1, len(nums)):
            left_accumulated_mul[i] = nums[i] * left_accumulated_mul[i - 1]
        
        right_accumulated_mul = [0] * len(nums)
        right_accumulated_mul[-1] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            right_accumulated_mul[i] = nums[i] * right_accumulated_mul[i + 1]
        
        product_except_self = [0] * len(nums)
        for i in range(len(nums)):
            left_mul = left_accumulated_mul[i - 1] if i - 1 >= 0 else 1
            right_mul = right_accumulated_mul[i + 1] if i + 1 < len(nums) else 1
            product_except_self[i] = left_mul * right_mul
    
        return product_except_self
        
```

# Step2

## Code2-1'

* leetcodeのfollow-upに空間計算量をO(1)にできるかとあるのでやってみる

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        product_except_self = [1] * len(nums)

        for i in range(1, len(nums)):
            product_except_self[i] = product_except_self[i - 1] * nums[i - 1]

        prefix_mul = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            product_except_self[i] *= prefix_mul
            prefix_mul *= nums[i]
        
        return product_except_self
        
```

## 他の人のPRを見る

* https://github.com/TaisukeFujise/leetcode_tafujise/pull/7
    * `Code2-1'`を書く時に対称性を意識したらもうちょっと読みやすくなりそう
* https://github.com/huyfififi/coding-challenges/pull/37
    * `prefix_products`や`suffix_products`といった命名は良い
* https://github.com/Ryotaro25/leetcode_first60/pull/67


# Step3

* 空間計算量をO(1)にしない方が読みやすいのでそっちで実装

## Code3-1

* 2:34
* 1:51
* 1:23

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        
        suffix_product = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]

        product_except_self = [None] * len(nums)
        for i in range(len(nums)):
            product_except_self[i] = prefix_product[i] * suffix_product[i]
        
        return product_except_self
        
```
