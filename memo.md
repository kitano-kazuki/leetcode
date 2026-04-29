# Step1

## アプローチ

* O(N)で全部見るアプローチなら一瞬でとける
    * 5000 / 10^6 = 0.005 sec程度の実行時間
* O(logN)でやるアプローチを考える
* 同じtarget = 3でも, 真ん中を見ただけではわからない
    * [6 2 3]
    * [3 1 2]
* 折り返し後ってわかっていたなら、targetがどっち側にあるかは一箇所みればわかる
    * 今の地点から折り返しまで
    * 折り返しから今の地点まで
* 前の問題のように最小値の位置をO(logN)で見つけてから, binary searchの端っこをずらして行う

## Code1-1 (Binary Search)

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        offset = self._find_minimum_index(nums)

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            mid_with_offset = (mid + offset) % len(nums)
            if nums[mid_with_offset] < target:
                left = mid + 1
            else:
                right = mid
        
        insertion_index_with_offset = (left + offset) % len(nums)

        if nums[insertion_index_with_offset] == target:
            return insertion_index_with_offset
        return -1

    def _find_minimum_index(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid

        return left

```

# Step2

## Code2-1 (Binary Search)

* 関数でoffset付きのbinary searchを切り出した
* 動作がわかるように例を追加した
    * targetと同じ値が複数あった場合の動作
    * targetが存在しなかった場合の動作
    * offsetがminimumでなかった場合の動作
* 文章で説明するよりもミニマムな入出力例を出した方がわかりやすいかも
* offsetとせずに、minimum_indexを起点にしていることが関数名でわかるようにした方がいいかも
    * `_binary_search_rotated_array`で引数に`minimum_index`をつけるとか

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        offset = self._find_minimum_index(nums)
        index = self._binary_search_left_with_offset(nums, offset, target)
        if nums[index] == target:
            return index
        return -1

    def _find_minimum_index(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid

        return left

    # ex) [6, 4, 5, 6], offset=1, target=6 -> 3
    # ex) [7, 4, 5], offset=1, target=6 -> 0
    # ex) [7, 4, 5], offset=2, target=6 -> Unexpected(offset should be index of the minimum)
    def _binary_search_left_with_offset(self, nums: list[int], offset: int, target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            mid_with_offset = (mid + offset) % len(nums)
            if nums[mid_with_offset] < target:
                left = mid + 1
            else:
                right = mid
       
        return (left + offset) % len(nums)

```

# Step3

## 他の人のコードを見る

* https://github.com/olsen-blue/Arai60/pull/43
    * Step3 - 解法1
        * middleの位置が折り返し後かどうかを判定
        * その判定結果を元にtargetが存在する範囲を絞り込む
    * Step3 - 解法2
        * pythonのbisectに渡すkey関数を工夫している
        * タプルを返す関数
        * (num <= nums[-1], target <= num)
        * > Aで分けられた序列の中で、Bを決める時に target以上なのがどこからなのかが分かれば良い
        * とあるが、これはパズルでは？？
        * 個人的には, `(num <= nums[-1], num)`
        * の方が直感的
        * bisect_leftに渡す配列が`(num <= nums[-1], num)`でソートされています
        * target探す時もそのルール`(num <= nums[-1], num)`に従ってね
        * という感じ
        * Bisectleftのドキュメント
        * > key specifies a key function of one argument that is used to extract a comparison key from each element in the array. To support searching complex records, the key function is not applied to the x value.
        * これ、keyを全ての要素に適用した結果得られる配列が適用前と順序変わったらよくないような気がします

* https://github.com/naoto-iwase/leetcode/pull/26
    * Step2 - 実装2
        * bisectleftの`lo`と`hi`パラメータを使用している
        * 最初に`min_index`をbisectで探して, min_indexの右側の上り坂か、min_indexの左側の上り坂のどちらにtargetあるか決める
        * 上記で決めた部分的な上り坂に対してbisectでloとhiを指定
    * Step2 - 実装3
        * 上記二つ目と同様のbisectleftのkeyをいじる方法
        * 自分の考察した方法: `(num <= nums[-1], num)`をkeyに渡していた

* https://github.com/mamo3gr/arai60/pull/41
    * 上記までの解法と同様

## 他の人のコメントを見る

* https://github.com/Yuto729/LeetCode_arai60/pull/48#issuecomment-4279391605
    * > 個人的には、配列の中の最小の値の位置を検索したあと、 target が前半と後半のどちらに存在しているのかを判定し、その中でもう一度検索したほうが、読み手にとって理解しやすくなると思いました。
* https://github.com/tom4649/Coding/pull/41#discussion_r3035490624
    * > (mid_in_sorted + minimum_index) % len_nums という計算が省け、読み手が理解しやすくなるだろうという意図がありました。
    * たしかにoffsetを使うやり方は計算の手間が増えている文少し読み手の負担がある
    * 関数に括り出したのはそういう意味では認知負荷の軽減につながっていそう

## 上記を踏まえて別の解法を実装

### Code3-2 (bisect with customized key)

* keyに(num <= nums[-1], num)を渡す方法
* keyは関数のことを意味しそうだから, `compute_key`よりも`compute_priority`の方がよいかも？？

```python
import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # rotated array -> corresponding keys
        # [5, 6, 1, 2] -> [(0, 5), (0, 6), (1, 1), (1, 2)]
        def compute_key_for_rotated_array(num: int) -> tuple[int, int]:
            return (num <= nums[-1], num)

        index = bisect.bisect_left(
            a   = nums, 
            x   = compute_key_for_rotated_array(target),
            key = compute_key_for_rotated_array
        )
        if nums[index] == target:
            return index
        return -1
        

```

### Code3-3 (bisect with lo and hi)

* minimum_indexを見つけた後に, lo,hiを指定したbisectleftを実行する方法

```python
import bisect


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def is_between_minimum_and_right(num: int) -> bool:
            return (num <= nums[-1])

        minimum_index = bisect.bisect_left(nums, True, key=is_between_minimum_and_right)

        if is_between_minimum_and_right(target):
            lo, hi = minimum_index, len(nums)
        else:
            lo, hi = 0, minimum_index
        
        index = bisect.bisect_left(nums, target, lo, hi)
        
        if nums[index] == target:
            return index
        return -1

```

### Code3-4 (binary search with complex condition)

* 最小値がどこにあるか、targetがどこにあるかを判定しながら二分探索する方法

```python
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1
        is_target_after_minimum = target <= nums[-1]
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid

            is_mid_after_minimum = nums[mid] <= nums[-1]

            if is_mid_after_minimum:
                if is_target_after_minimum:
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid
                else:
                    right = mid - 1
                continue

            if not is_mid_after_minimum:
                if is_target_after_minimum:
                    left = mid + 1
                else:
                    if nums[mid] < target:
                        left = mid + 1
                    else:
                        right = mid
                continue
        
        if nums[left] == target:
            return left
        return -1
                

```

# Step4

## Code4-2 (bisect with customized key)

```python

```
