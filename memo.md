# Step1

## アプローチ

* 実験する
* [1,2,3] -> [1,3,2] -> [2,1,3] -> [2,3,1] -> [3,1,2] -> [3,2,1]
* [1,2,3,4] -> [1,2,4,3] -> [1,3,2,4] -> [1,3,4,2] -> [1,4,2,3] -> [1,4,3,2] -> [2,1,3,4] ...
* 先頭はなるべく固定したい
* 先頭のi文字を固定して, 次に大きい並び順を作るには
    * i+1文字目以降が降順になっていると, i+1文字目以降を並び替えて得られるものは全部今の並びよりも辞書順で小さい
    * 右側から見ていって, 部分列が降順ではなくなった場所を起点に考えると良さそう
* [6,5,3,7,2,4,1] -> [6,5,3,7,4,1,2]
* 同じ値があった場合どうなるか
    * [1,1,2] -> [1,2,1] -> [2,1,1]
    * [1,1,2,3] -> [1,1,3,2] -> [1,2,1,3] -> [1,2,3,1] -> [1,3,1,2] -> [1,3,2,1] -> [2,1,1,3] ...
* 降順ではなくなった場所を探すのに最悪の場合で O(N)
* 見つけた後, 降順の部分から入れ替えるべき対象を見つける
    * 降順ではなくなった値のすぐ左の数字xより大きい最小の値を見つけたい
    * binary_searchをしたら, 最悪の場合でO(logN) (でもボトルネックじゃないからO(N)で普通に探して良さそう)
    * 入れ替えた後, その部分をひっくり返すのでO(N)
* トータルでO(N)
* 実行時間は, 100 / 10^6 ~= 10^-4 sec程度
* 空間計算量はO(1)

## Code1-1 (find non-decending)

* 一部分だけをin-placeでreverseしていないので, 空間計算量はO(N)かかりそう
* 調べたら, そのためのライブラリはないらしいから自分で両端からswapする必要がありそう

```python
import itertools


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        non_decending_point = self._find_non_decending_point(nums)

        # nums is decending order
        if non_decending_point == -1:
            nums.reverse()
            return

        for i in range(len(nums) - 1, non_decending_point, -1):
            if nums[i] <= nums[non_decending_point]:
                continue
            nums[non_decending_point], nums[i] = nums[i], nums[non_decending_point]
            nums[non_decending_point+1:] = reversed(nums[non_decending_point+1:])
            return

        
    # ex) [5,6,7,8] -> non_decending_point = 2
    # ex) [5,6,8,7] -> non_decending_point = 1
    # ex) [8,7,6,5] -> non_decending_point = -1(not found)
    def _find_non_decending_point(self, nums: list[int]) -> int:
        previous_num = -1
        non_decending_point = len(nums) - 1
        while non_decending_point >= 0 and nums[non_decending_point] >= previous_num:
            previous_num = nums[non_decending_point]
            non_decending_point -= 1
        
        return non_decending_point

```

# Step2

## 他の人のコードを見る

* https://github.com/olsen-blue/Arai60/pull/59
    * アルゴリズムは一緒
    * 二重ループでやる方法も紹介していた.
* https://github.com/naoto-iwase/leetcode/pull/59

## 他の人のコメントを見る

* C++の実装
    * https://en.cppreference.com/cpp/algorithm/next_permutation
        * 同様のことを`reverse_iterator`を使って効率的にやっている

# Step3

## Code3-1 (find non-decending)

```python
import bisect


class Solution:

    # ex) [4,6,5] -> 0
    # ex) [4,5,5] -> 0
    # ex) [6,5,4] -> -1
    def rfind_non_decending_point(self, nums: list[int]) -> int:
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= nums[i + 1]:
                continue
            return i
        
        return -1


    def swap(self, nums: list[int], i: int, j: int) -> None:
        nums[i], nums[j] = nums[j], nums[i]
        return


    def reverse_in_place(self, nums: list[int], left: int, right: int) -> None:
        while left < right:
            self.swap(nums, left, right)
            left += 1
            right -= 1
        return


    def nextPermutation(self, nums: list[int]) -> None:
        pivot = self.rfind_non_decending_point(nums)

        if pivot == -1:
            self.reverse_in_place(nums, 0, len(nums) - 1)
            return
        
        # ex) [1,3,2] -> [1,2,3]
        self.reverse_in_place(nums, pivot + 1, len(nums) - 1)

        # ex) [1,2,3] -> [2,1,3]
        swap_index = bisect.bisect_right(nums, nums[pivot], lo=pivot + 1)
        self.swap(nums, pivot, swap_index)
        return

```
