# Step1

## アプローチ

* 一般的な二分探索の問題
* [1, 3, 5, 6], 7 -> [1, 3, 5, 6, 7]と末尾に追加するケースと
* [1, 3], 0 -> [0, 1, 3]と先頭に追加するケースに気を付ける
* [1, 2, 2, 3], 3では -> [1, 2, 2, "3", 3]か [1, 2, 2, 3, "3"]かどちらか
* pythonライブラリでいうところのbisec_leftかbisec_rightかの違いになりそう
    * 今回は制約からdistinct valueであることが保証されてはいるけども
* 重複する要素が複数ある時は、後ろに挿入した方が計算量が少しだけ良くなるので、後ろの位置を返そう
    * **今回の問題では見つかった数字の場所を変えさにといけなかった**
* 計算料はO(logN)で, 実行時間は, 10^4 / 10^6 = 0.01 secほど

## Code1-1 (Binary Search)


```python
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0

        start = 0
        end = len(nums)
        while start < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        
        return end

```

# Step2

* Step1の範囲を表す変数名で, startはinclusiveで, endはexclusive
* リーダブルコードにinclusiveとexclusiveのそれぞれに応じた名前があったなぁという記憶をもとにした
* 正しくは ,begin/endとするべきだった
    * 限界値を含める時は min/max
    * 範囲を指定する時は first/last (両方ともinclusive)
    * 包含/排他的関係には begin/end (開始はinclusive, 終了はexclusive)
* あとは, 二分探索のイメージをするときに以下のようなイメージにした
    * 等しい値があった時は後ろに挿入したい(bisec_right)を想定
    * 長い棒が昇順に並んでいる (サスケのステージみたいな)
    * スタート地点は一番左（＝０）
    * 棘が一番最後の棒の上に置かれている(=n)
    * スタート地点か棘を動かして, 自分が行けるギリギリの棒(=target)を探す
    * 自分はスタート地点と棘の真ん中にワープし続ける

```python
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0

        begin = 0
        end = len(nums)

        while begin < end:
            mid = begin + (end - begin) // 2
            
            if nums[mid] == target:
                return mid

            if nums[mid] < target:
                begin = mid + 1
            else:
                end = mid
        
        return end
                
```

# Step3

## 他の人のコードやコメントを見る

* https://github.com/olsen-blue/Arai60/pull/41/files
* https://github.com/naoto-iwase/leetcode/pull/24/files
    * 開区間, 閉区間のそれぞれの組み合わせについて詳細に吟味
* https://github.com/mamo3gr/arai60/pull/39/files


# Step4

```python
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if not nums:
            return 0

        begin = 0
        end = len(nums)
        while begin < end:
            mid = begin + (end - begin) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                begin = mid + 1
            else:
                end = mid

        return end

```