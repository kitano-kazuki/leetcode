# Step1

## アプローチ

* 順番に採用するかどうかを決めて, 保存すればいい
* 前回のpermutationsと同様にbacktrack
* 最終的には, 2^n個のリストができあがる.
* 保存をする時に, O(N)かかるから計算量はO(N * 2^N)かな？
* 実行時間は, 10 * 2^10 / 10^6 ~= 10^-2 = 10 msくらい
* たしか, 半全探索みたいな手法もあった気がする
    * subsetの構築にも使えるのかな？どれだけ計算量が緩和されるのかな？
    * 詳しく覚えていないから後で調べる

## Code1-1

```python
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        subset = []
        all_subsets = []
        def generate_subsets(start: int) -> None:
            if start == len(nums):
                all_subsets.append(subset.copy())
                return

            subset.append(nums[start])
            generate_subsets(start + 1)
            subset.pop()
            generate_subsets(start + 1)
            

        generate_subsets(0)
        return all_subsets

```


# Step2

* 半分全探索について調べた.
* 今回は使えないけど、以下のような場面で使えそう
    * 条件を満たすsubsetを探す
    * 部分和問題

## Code2-1

* 前からの引き継ぎを考えたらだいぶシンプルになった
    * 今までに作ったやつに何も加えなかったものと今注目している数字を加えたものを追加して引き継ぐ

```python
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        all_subsets = [[]]
        for i in range(len(nums)):
            next_all_subsets = []
            for subset in all_subsets:
                next_all_subsets.append(subset)
                next_all_subsets.append(subset + [nums[i]])
            all_subsets = next_all_subsets
        
        return all_subsets

```

# Step3

## 他の人のコードを見る

* https://github.com/olsen-blue/Arai60/pull/52
    * 解法１ではbit全探索
    * 解法２のbacktrackは自分の方法code1-1と同じ
* https://github.com/naoto-iwase/leetcode/pull/52
    * 実装2は自分のcode2-1と同じ

## 他の実装をやってみる

### Code3-2 (Bit全探索)

```python
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        all_subsets = []
        for bit_pattern in range(1 << len(nums)):
            subset = []
            for i in range(len(nums)):
                if 1 << i & bit_pattern:
                    subset.append(nums[i])
            all_subsets.append(subset)
        
        return all_subsets
        
```

# Step4

* Backtrackで実装する

## Code4-1

```python
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        all_subsets = []

        def generate_subset_after_index(index :int, subset: list[int]) -> None:
            if index == len(nums):
                all_subsets.append(subset.copy())
                return 
            
            subset.append(nums[index])
            generate_subset_after_index(index + 1, subset)
            subset.pop()
            generate_subset_after_index(index + 1, subset)
        
        generate_subset_after_index(0, [])
        return all_subsets


```