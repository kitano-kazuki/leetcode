# Step1

## アプローチ

* 一番ナイーブなのは, あらゆるsubsequenceのパターンを列挙すること
    * 2^n種類あるので, n=2500の時, log_10_(2^2500) = 2500 * log_10_2 = 750より, 10^750 => 絶対おわらん
    * 10^6ステップが1secだとすると, n * log_10_2 = 6となるnは20くらい
* 仕事を引き継いでもらってできないか考える
    * 何がわかっていればいい？？
        * これまでのLISの長さ = m
        * ↑を実現した時の値 = x
    * 何をすればいい？
        * 今見ている値がxよりも大きければ, mやxを更新する
        * そうでなかったら何もしない??
            * `1 4 100 5 7 8`とかでうまくいかない
        * 長さ1の時のx, 長さ2の時のx...とかで保存しておく??
        * うまくいきそうだけど, 計算量が気になる
            * 事前に長さnの配列(=l)を用意
            * 各iにつき, nums[i]とlを見比べながら更新
            * O(n^2)
            * n=2.5 * 10^3なので, n^2 = 7 * 10^6くらい
            * 10^6 steps / 1secだとちょうど1秒くらいで終わる
            * これでいきましょう

## Code1-1

```python
# solved: 10:18


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        # minimum_values[i] represents the minimum tail value among possile LIS with length i
        minimum_values = [float("inf")] * (n + 1)
        minimum_values[0] = float("-inf")

        for i in range(n):
            for length in range(1, i + 2):
                if minimum_values[length - 1] < nums[i] and nums[i] < minimum_values[length]:
                    minimum_values[length] = nums[i]
        
        for i in range(n, -1, -1):
            if minimum_values[i] != float("inf"):
                return i

```

# Step2

## Code2-2

```python
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        # minimum_values[i] represents the minimum tail value among possile LIS with length i
        minimum_values = [float("inf")] * (n + 1)
        minimum_values[0] = float("-inf")

        for num_index in range(n):
            num_of_elements = num_index + 1
            for length in range(1, num_of_elements + 1):
                if minimum_values[length - 1] < nums[num_index]:
                    minimum_values[length] = min(nums[num_index], minimum_values[length])
        
        for i in range(n, -1, -1):
            if minimum_values[i] != float("inf"):
                return i

```

## 他の人のコード

* https://github.com/mamo3gr/arai60/pull/29
    * step3では二つの解法を用いている
        * 解法1
            * 自分のコードで`minimum_values`としていたものは以下のように工夫して表現できた
                * 最初からn個分確保しない. 単調増加列となる場合に配列に`append`する.
                * 配列内で更新が必要な部分は, 配列の中でなるべく右側でかつ`nums[i]`より大きい数があった時
                    * 二分探索を活用できる
        * 解法2
            * 他にも各iごとに以下の処理を行う方法もある
                * 今までに作成した単調増加列を保持してあるものとする
                * それら全てに対して, 末尾に今の数を追加できそうなら追加する.
                * その回で最も長くなる単調増加列を、新たに保持するリストに追加

* https://github.com/Satorien/LeetCode/pull/31
    * mamo3grの解法1と同様.
    * bisect_leftを自前で実装.
* https://github.com/naoto-iwase/leetcode/pull/36
    * mamo3grの解法1と同様.

## 過去のコメント

* https://discord.com/channels/1084280443945353267/1200089668901937312/1209563502407065602
    * 3-5番は、セグメント木 (BITでも可) を使います。セグメント木は、ある範囲の MAX を計算させることができます。nums[i] の範囲は、-10^4 <= nums[i] <= 10^4 なので、この範囲に対してセグメント木を構築します。

# 調べた上で色々実装

## 二分探索を活用

## 各iごとに単調増加列を用意

## Segment Tree

## Binary Indexed Tree