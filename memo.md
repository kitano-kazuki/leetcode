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

# Memo

## Nanに対しての==演算について

https://discord.com/channels/1084280443945353267/1201211204547383386/1208701087264280596
> ただ、nan というのがあって、nan == nan が False です。 IEEE754 を確認しておいてください。

https://docs.python.org/ja/3/reference/expressions.html#value-comparisons
> 非数値である float('NaN') と decimal.Decimal('NaN') は特別です。 数と非数値との任意の順序比較は偽です。 直観に反する帰結として、非数値は自分自身と等価ではないことになります。 例えば x = float('NaN') ならば、 3 < x, x < 3, x == x は全て偽で、x != x は真です。 この振る舞いは IEEE 754 に従ったものです。

## 出題意図について

https://github.com/katataku/leetcode/pull/12#discussion_r1894613102
> 要するにこの問題の推定される出題意図は条件を変えたときに案がいくつか出てくるかです。

https://github.com/quinn-sasha/leetcode/pull/13#discussion_r1960884543
> この問題は問題文自体では終わっていなくて、解けた後に、いくつか追加の条件が出てきて、その下でのアルゴリズムとそれらの pros and cons が要求されると思います。

## Python内部のSetのintersectionの実装について

要素数が小さい方のSetを走査して, 各要素が要素数の大きい方のSetに含まれているか見ている

https://github.com/python/cpython/blob/ea90b032a016122e7871e91c5210f3b4e68768b4/Objects/setobject.c#L1675

```c
...
    if (PySet_GET_SIZE(other) > PySet_GET_SIZE(so)) {
        tmp = (PyObject *)so;
        so = (PySetObject *)other;
        other = tmp;
    }

    while (set_next((PySetObject *)other, &pos, &entry)) {
        key = entry->key;
        hash = entry->hash;
        Py_INCREF(key);
        rv = set_contains_entry(so, key, hash);
        if (rv < 0) {
            Py_DECREF(result);
            Py_DECREF(key);
            return NULL;
        }
        if (rv) {
            if (set_add_entry(result, key, hash)) {
                Py_DECREF(result);
                Py_DECREF(key);
                return NULL;
            }
        }
        Py_DECREF(key);
    }
    return (PyObject *)result;
...
```

## 二分探索を使った解法について

`nums2`だけを最初にソートして, `num2`の各要素についてその存在を`nums1`の二分探索で確かめる方法.
`nums1`のソートにO(nlogn)
`nums1`の二分探索にO(logn)
`nums2`の要素数がmとする.
全体では, O(nlogn + mlogn)

引用したコード
https://github.com/aki235/Arai60/pull/13/files#diff-6c0496a496cb8f7a35d43bf248b1df530eadc13c9be2b8c1270a983021b9e762R74

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1は長いソート済みのリスト、nums2は短い未ソートのリストを想定
        nums1 = sorted(nums1) # 想定に合わせるためソート

        intersection = []
        for num in nums2:
            if num in intersection:
                continue

            left = -1
            right = len(nums1)

            while right - left > 1:
                middle = (right + left) // 2
                if num < nums1[middle]:
                    right = middle
                elif num > nums1[middle]:
                    left = middle
                else:
                    intersection.append(num)
                    break

        return intersection
```