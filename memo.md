# Step1

## アプローチ

* `nums`の要素3つを足して`0`になるような組み合わせを出したい
* 3重ループが一番単純なやり方
    * O(N^3)
    * 10^9 / 10^6 ~= 10^3 sec
* ある`num`で固定した時,
    * それ以降の部分から二つを選んで`-num`になる和を作りたい
    * `set`を用意しておけば, 対応するペアをO(N)で探せる
    * O(N^2)
    * 9 * 10^6 / 10^6 ~= 10 secくらい
    * これが厳し目に見積もっている値だからギリギリいけるかな？？
* 半全探索みたいなことも組み合わせられたりするのかな？？
    * でもNが3000だからそんなに効果なさそう
    * 効果あるとしたら, N=10とかの規模でパターンいっぱいださなきゃいけないとか
* TLE怖いけど、一つ固定からのtwo sumの方法でやるか

## Code1-1

* AC
* TLEにはならなかった

```python
class Solution:
    def two_sum(self, nums: list[int], start: int, target: int) -> set[tuple[int]]:
        result = set()

        seen = set()
        for num in itertools.islice(nums, start):
            if target - num in seen:
                result.add(tuple(sorted([num, target - num])))
            seen.add(num)
        
        return result


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()

        for i, num in enumerate(nums):
            for n1, n2 in self.two_sum(nums, i, -num):
                result.add(tuple(sorted([n1, n2, num])))
        
        return [list(pair) for pair in result]
        
```

# Step2

## Code2-1

* 変更なし

```python
class Solution:
    def two_sum(self, nums: list[int], start: int, target: int) -> set[tuple[int]]:
        result = set()

        seen = set()
        for num in itertools.islice(nums, start):
            if target - num in seen:
                result.add(tuple(sorted([num, target - num])))
            seen.add(num)
        
        return result


    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()

        for i, num in enumerate(nums):
            for n1, n2 in self.two_sum(nums, i, -num):
                result.add(tuple(sorted([n1, n2, num])))
        
        return [list(pair) for pair in result]
        
```

## 他の人のPRを見る

* https://github.com/tom4649/Coding/pull/69
    * ソート済みの配列に対して二つのポインタを使用する方法は思いつかなかった
        * two sumは解いたことがあったので, 思いつくことはできた
    * 最初にinputの配列をsortしてしまえば, ペアを追加する時にわざわざsortをする必要はない

## Code2-2 (two pointer)

* 重複を避けるために, setを使ったが、値が被り続けている限りポインタを進めることで重複を避けることもできる
    * これは`Code2-2' (two pointer without set)`として実装する

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        pairs = set()

        nums = sorted(nums)
        for i in range(len(nums)):
            for n1, n2 in self.twoSum(nums, -nums[i], i + 1):
                pairs.add((nums[i], n1, n2))
        
        return list(map(list, pairs))


    def twoSum(self, nums: list[int], target: int, start: int) -> list[list[int]]:
        pairs = set()

        left = start
        right = len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                pairs.add((nums[left], nums[right]))
                left += 1
                continue
            if total < target:
                left += 1
                continue
            if total > target:
                right -= 1
                continue
        
        return pairs
        
```

## Code2-2' (two pointer without set)

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)

        pairs = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for two_sum_pair in self.twoSum(nums, -nums[i], i + 1):
                pairs.append([nums[i]] + two_sum_pair)
        
        return pairs


    def twoSum(self, nums: list[int], target: int, start: int) -> list[list[int]]:
        pairs = []

        left = start
        right = len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total < target:
                left += 1
                continue
            if total > target:
                right -= 1
                continue
            # total == target
            pairs.append([nums[left], nums[right]])
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1

        return pairs

```


# Step3

## Code3-2' (two pointer without set)

* 4:13
* 3:05
* 2:42

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        pairs = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for two_sum_pair in self.twoSum(nums, -nums[i], i + 1):
                pairs.append([nums[i]] + two_sum_pair)
        
        return pairs

    
    def twoSum(self, nums: list[int], target: int, start: int) -> list[list[int]]:
        pairs = []

        left = start
        right = len(nums) - 1
        while left < right:
            total = nums[left] + nums[right]
            if total < target:
                left += 1
                continue
            if total > target:
                right -= 1
                continue
            pairs.append([nums[left], nums[right]])
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        
        return pairs

```
