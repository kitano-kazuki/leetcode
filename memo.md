# Step1

## アプローチ

* 一番単純な方法は0以外の要素を記録しておく. 前から0以外の要素を埋める. 残った部分はすべて0にする.
    * 時間計算量: O(N)
        * 実行時間は, 10^4 / 10^6 = 10^-2 sec
    * 空間計算量: O(N)
        * 28 bytes * 10^4 / 1024 ~= 280KB

## Code1-1

```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_nums = []
        for num in nums:
            if num != 0:
                non_zero_nums.append(num)
        
        if not non_zero_nums:
            return

        processed_tail = 0
        for i in range(len(nums)):
            if processed_tail < len(non_zero_nums):
                nums[i] = non_zero_nums[processed_tail]
                processed_tail += 1
            else:
                nums[i] = 0
        
        return

```

# Step2

* 1パスでできないか考える
    * 0の先頭を記録しておく
    * 0以外の要素が出てきたら, 0の先頭とそれを入れ替える

## Code2-2

* 0が登場していない場合は, i == swap_indexとなって, 入れ替えのコードでは中身が変わらない
    * ここがややパズルになりそうだが、ロジックを別に分けるとかえってコード量が増えて見にくくなりそうなのでそのまま

```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        swap_index = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[i], nums[swap_index] = nums[swap_index], nums[i]
            swap_index += 1

        return

```

# Step3

## 他の人のコードを見る

* https://github.com/olsen-blue/Arai60/pull/55
    * 解法1
        * 全く一緒
        * `swap_index`に対応する命名について
            * `index_to_put_non_zero`
            * `non_zero_putting_index`
            * など
    * 解法4
        * forを２回回す解法
        * 1回目ではswapではなく, つめる形でnon-zeroな値を配置
        * 2回目では, 詰めきった後の残りを0で埋める

* https://github.com/naoto-iwase/leetcode/pull/55
* https://github.com/mamo3gr/arai60/pull/51

# Step4

## Code4-3

```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_tail = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[non_zero_tail] = nums[i]
            non_zero_tail += 1
        for i in range(non_zero_tail, len(nums)):
            nums[i] = 0

        return
        
```