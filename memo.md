# Step1

## アプローチ

* prefix sumを作ったら, 考えられるパターンをO(n^2)で探せる
    * 今回は n=10^5なので実行には10^10 / 10^6 = 10^4秒もかかってしまう
* prefix sumをソートして元のindexも保持するようにしたら・・・？
    * 配列の後ろ側から順番にペア候補を見るけど, それが今のindexよりも小さい場合は候補を一つ前の要素にして。。。
    * 結局 O(n^2)なのは変わらず
* sliding windowも、window内がinvalidなら広げてもinvalidみたいな条件はないから適用できない
* DPのカテゴリだからDPで考えるというのは少し癪だけど, DPでできないか考える
    * 実際に人手で作業するとして, 引き継がれたいものと引き継ぐものを考える
        * 引き継がれたいもの: 一個前で終わるsubarrayのうち一番大きいもの
        * 引きj継ぎたいもの: 今見ている部分で終わるsubarrayのうち一番大きいもの
* 1pathで処理するだけなのでO(n)


## Code1-1 (DP)

```python
# solved: 1:47

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray_sum = float("-inf")
        max_subarray_sum_before = 0
        for num in nums:
            max_subarray_sum_before = max(max_subarray_sum_before + num, num)
            max_subarray_sum = max(max_subarray_sum, max_subarray_sum_before)
        return max_subarray_sum

```

# Step2

## Code2-1 (DP)

変更なし

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray_sum = float("-inf")
        max_subarray_sum_before = 0
        for num in nums:
            max_subarray_sum_before = max(max_subarray_sum_before + num, num)
            max_subarray_sum = max(max_subarray_sum, max_subarray_sum_before)
        return max_subarray_sum

```
## 他の人のコードやコメントを見る

* https://github.com/mamo3gr/arai60/pull/30
    * 分割統治法による解法(=sol1)
        * 真ん中を跨ぐ場合, 跨がない場合で分ける
        * 真ん中を跨ぐ場合, 真ん中を基準に右と左にそれぞれ伸ばしていく. それぞれの最大をたす
    * 貪欲法による解法(=sol2)
        * 和を手前から計算していく
        * 負になった場合はリセットで0にして, 次の値を足していく

* https://github.com/Satorien/LeetCode/pull/32
    * sol2と同じ
* https://github.com/naoto-iwase/leetcode/pull/37
    * sol2と同じ


## Code2-2 (Divide and Conquer)

O(nlogn)になってしまう

```python

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        return self.max_subarray_in_range(nums, 0, len(nums) - 1)

        
    def max_subarray_in_range(self, nums: list[int], left, right):
        if left == right:
            return nums[left]
       
        mid = (left + right)  // 2
        max_subarray_in_left_half = self.max_subarray_in_range(nums, left, mid)
        max_subarray_in_right_half = self.max_subarray_in_range(nums, mid + 1, right)
        max_subarray_through_mid = self.max_subarray_from_mid(nums, mid, left, right)
        return max(max_subarray_in_left_half,
                   max_subarray_in_right_half,
                   max_subarray_through_mid)


    def max_subarray_from_mid(self, nums: list[int], mid, left, right):
        leftward_sum = 0
        max_leftward_sum = float("-inf")
        for i in range(mid, left - 1, -1):
            leftward_sum += nums[i]
            max_leftward_sum = max(max_leftward_sum, leftward_sum)

        rightward_sum = 0
        max_rightward_sum = float("-inf")
        for i in range(mid + 1, right + 1, 1):
            rightward_sum += nums[i]
            max_rightward_sum = max(max_rightward_sum, rightward_sum)

        return max_leftward_sum + max_rightward_sum

```

# Step3

## Code3-1 (DP)

```python
# 1st: 1:08
# 2st: 1:00
# 3rd: 0:55

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_subarray = float("-inf")
        max_subarray_ending_before = 0
        for num in nums:
            max_subarray_ending_before = max(max_subarray_ending_before + num, num)
            max_subarray = max(max_subarray_ending_before, max_subarray)
        return max_subarray

```

## Code3-2 (Divide and Conquer)

```python
# 1st: 8:10
# 2nd: 6:50
# 3rd: 3:01

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        return self.max_subarray_in_range(nums, 0, len(nums) - 1)
    
    def max_subarray_in_range(self, nums, left, right) -> int:
        if left == right:
            return nums[left]
        
        def max_subarray_through_mid(nums, left, right, mid) -> int:
            leftward_max_sum = float("-inf")
            leftward_sum = 0
            for i in range(mid, left - 1, -1):
                leftward_sum += nums[i]
                leftward_max_sum = max(leftward_max_sum, leftward_sum)
            
            rightward_max_sum = 0
            rightward_sum = 0
            for i in range(mid + 1, right + 1, 1):
                rightward_sum += nums[i]
                rightward_max_sum = max(rightward_max_sum, rightward_sum)
            
            return leftward_max_sum + rightward_max_sum
        
        mid = (left + right) // 2
        left_max_subarray = self.max_subarray_in_range(nums, left, mid)
        right_max_subarray = self.max_subarray_in_range(nums, mid + 1, right)
        mid_through_max_subarray = max_subarray_through_mid(nums, left, right, mid)

        return max(
            left_max_subarray,
            right_max_subarray,
            mid_through_max_subarray
        )

```