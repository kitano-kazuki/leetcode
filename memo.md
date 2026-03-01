# Step1

## アプローチ
* 二重のループを使って最初にターゲットになるペアが見つかったら終了
* 辞書を使って, みた値とインデックスを保持しておく、新しい値に対してはtarget - numをした値が辞書に入っていたらペアが見つかったことになるのでインデックスのペアを返せる
* 一つの値に対して複数のインデックスが対応する場合があるが、問題の条件的にどれか一つ返せば問題がない。今回は最後に遭遇したインデックスを優先させる。
* どちらの方法を使うか
* 二重ループの方法は最悪の場合でO(N^2)かかるが、空間計算量はO(1). 
* 辞書を使う方法は最悪の場合でもO(N)だが、空間計算量として辞書文の領域を確保するためO(N)。
* 計算量の差が顕著に辞書の方法の方が優位なため、辞書を使う方法で実装する。

## Code1-1

```python
class Solution:
    def twoSum(self, nums, target):
        num_to_idx = {}
        for i, num in enumerate(nums):
            if target - num in num_to_idx:
                return [num_to_idx[target - num], i]
            num_to_idx[num] = i
        raise ValueError("No solution found")

```

# Step2

## Code2-1

```python
class Solution:
    def twoSum(self, nums, target):
        num_to_idx = {}
        for i, num in enumerate(nums):
            remain = target - num   # num + remain = target
            if remain  in num_to_idx:
                return [num_to_idx[remain], i]
            num_to_idx[num] = i
        raise ValueError("No solution found")

```

# Step3

## Code3-1

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_idx = {}
        for i, num in enumerate(nums):
            remain = target - num   # target = num + remain
            if remain in num_to_idx:
                return [num_to_idx[remain], i]
            num_to_idx[num] = i
        raise ValueError("No solution found")
```