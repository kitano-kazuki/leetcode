# Step1

## アプローチ

* 配列の長さの半分よりも多い数出現する要素を返す
* 配列の長さが偶数だったら, [2,2,1,1] => majorityエレメントはないことになる
* 今回は問題の制約から必ずmajorityエレメントが存在するとする
* 一番単純な方法は, 最初にcounterなどで個数を記録. その後, n/2以上出現しているものを探す
* 普通に前から見て行って, 個数がn/2超えたらってやってもいい
    * ワンパスでできるけど読みやすさで言うなら先に辞書に個数を記録した方がいいかな
* 計算量はO(N)で, 実行時間は10^4 / 10^6 ~= 10^-2 sec程度
* 使用メモリは, ユニークな数字の種類をmとして, m * 28(intのバイト数)程度
* 最大でも, 10^4 * 28 ~= 10KBくらい
* 3:20

## Code1-1

* AC: 1:01

```python
import collections


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter = collections.Counter(nums)
        
        for num, count in counter.items():
            if count > len(nums) // 2:
                return num
        
        raise ValueError("something went wrong.")
        
```

# Step2

## Code2-1

* 変更なし

```python
import collections


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counter = collections.Counter(nums)
        
        for num, count in counter.items():
            if count > len(nums) // 2:
                return num
        
        raise ValueError("something went wrong.")
        
```

## 他の人のPRを見る

* https://github.com/huyfififi/coding-challenges/pull/19
    * quick_selectで部分的にソートして, 真ん中にくる要素を見に行く方法など, k番目に小さい数を取得する方法として問題を捉え直していくつか解法をあげている
    * 全部が同じ数字だった場合にTLEになるらしいけど, 練習のためにQuick Selectを実装しておく

## Code2-2 (Quick Select)

* 47:12
* 調べずに思い出しながらやっていたら時間がめっちゃかかった

```python
import random


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        return self.quick_select(nums, 0, len(nums) - 1, len(nums) // 2)

    def _swap(self, nums: list[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]
        return

    def quick_select(self, nums: list[int], left: int, right: int, k: int) -> int:
        if left == right:
            return nums[left]
        
        i_pivot = random.randint(left, right)
        pivot = nums[i_pivot]
        self._swap(nums, i_pivot, right)

        i_store = left
        for j in range(left, right):
            if nums[j] < pivot:
                self._swap(nums, i_store, j)
                i_store += 1

        self._swap(nums, i_store, right)
        
        if k == i_store:
            return nums[i_store]
        if k < i_store:
            return self.quick_select(nums, left, i_store - 1, k)
        else:
            return self.quick_select(nums, i_store + 1, right, k)
    
```

# Step3

## Code3-1

```python
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.Counter(nums)
        for num, count in counter.items():
            if count > len(nums) // 2:
                return num
        
```
