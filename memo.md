# Step1

## アプローチ

* 与えられた配列をそれぞれSetに変換して, PythonのSetの`.intersection`メソッドを使用 (Pattern1)
* `nums1`に存在しているものを辞書(or set)に保存. `nums2`を見ながら, 辞書にある要素のみを結果に追加する. (Pattern2)
* それぞれをあらかじめソートしておく, 二つのポインタを使って捜査 (Pattern3)
    * それぞれのポインタは現在処理中の要素を指す.
    * 同じ要素を指していたら, それを結果に追加&ポインタを進める
        * ポインタを進めるときは, 結果に追加した値と異なる値になるまで進める
    * 二つのポインタが異なる値を指していたら, 小さい方を一つ進める.
    * どちらかのポインタが配列のサイズに到達したら終了
* それぞれの方法のメリットとデメリットを検討
    * Pattern 1
        * 実装が簡単
        * list -> setへの変換はどのくらい？？ O(n)かな
        * `intersection`の処理がどのくらい？？ 短い方のsetの長さ分かな？？
        * 時間計算量
            * O(n + m + min(n, m))?
        * 空間計算量
            * それぞれのsetの保存用でO(n + m)
    * Pattern 2
        * 時間計算量
            * 配列１を見て、辞書を生成するのにO(n) (配列1をsetに変換する方法でもいい)
            * 配列２の各要素(m個)についてO(1)で辞書にあるかを確認. O(m)
            * 結果の配列にO(1)で追加
            * O(n + m)
        * 空間計算量
            * 配列１の要素の辞書を作るのでO(n)
            * 配列のサイズが短い方に合わせれば O(min(n, m))
            * 結果を格納する部分は空間計算量に含めない
    * Pattern 3
        * 時間計算量
            * それぞれの配列をソートするのにO(nlogn + mlogm)
            * それぞれの配列を順番にみるので最悪の場合でO(n + m)
            * 全体だとO(n + nlogn + m + mlogm)
        * 空間計算量
            * in-placeにしない場合は, sortしたものを保存するのにO(n + m)
* Pattern2で実装する


## Code1

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            smaller_nums = nums1
            larger_nums = nums2
        else:
            smaller_nums = nums2
            larger_nums = nums1
        exist_in_smaller = set()        
        for num in smaller_nums:
            exist_in_smaller.add(num)
        
        result = set()
        for num in larger_nums:
            if num in exist_in_smaller:
                result.add(num)
        
        return list(result)

```

# Step2

## Code

* 読みやすくしていたら結局`.intersection`を使う方法になってしまった.
* でもそうすると`larger`と`smaller`に分ける必要すらない

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            smaller_nums = nums1
            larger_nums = nums2
        else:
            smaller_nums = nums2
            larger_nums = nums1
        exist_in_smaller = set(smaller_nums)        
        exist_in_larger = set(larger_nums)
        
        result = exist_in_smaller.intersection(exist_in_larger)
        
        return list(result)

```

簡略化したコード

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        return list(nums1_set.intersection(nums2_set))

```

# Step3

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            smaller_nums = nums1
            larger_nums = nums2
        else:
            smaller_nums = nums2
            larger_nums = nums1
        
        exist_in_smaller = set()
        for num in smaller_nums:
            exist_in_smaller.add(num)
        
        result_set = set()
        for num in larger_nums:
            if num not in exist_in_smaller:
                continue
            result_set.add(num)
        
        return list(result_set)
        
```