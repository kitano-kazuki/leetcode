# Step1

## アプローチ

* Segment Treeを使う
  * 全体の配列の長さが最初から決まりきっていないと難しい？？？
  * 実装は重たそう
  * 例えば配列の長さをkに固定したらどうなる？？
  * 要素の削除がないなら、値が追加されるたびにそれが何番目に該当するか判定して更新すればいい
  * やっていることとしてはheapとあまり変わらない？？
  * Segment Treeは更新が起こるたびに変更されうる特定の値を探すのに特化しているという認識
    * 行われる変更は、変更先のindexが指定されていると思っている
    * 今回のタスクでは変更先のindexがわからないから使えなさそう。。。？
* 優先度つきキュー(heapq)を使う
  * k番目を取得するには毎回popする必要がある？？
* あらかじめ配列をソートしておく。
  * 要素の追加時には、二分探索で要素の挿入位置を探せる
  * k番目は単純にidx = k - 1に存在する要素を見るだけ
  * 挿入による計算量はどのくらいだっけ。
    * 通常のリストだと挿入することによって、それ以降の部分を全部後ろにずらすから挿入箇所以降の要素数分の時間がかかる？？
      * pythonではここの部分が効率化されていたりするのかな？？
  * linkedListを使うと二分探索ができなくなる
    * 要素のアクセスをするためには前から順番にたどる必要があるため
* どの方法を用いるか
  * Segment Treeは今回の問題設定だと使えなさそう
  * 優先度付きキューは、k回popしてk番目の値を取得したあと、k回pushをする必要があっって、毎回heapに存在している要素数のlog分の計算量が最悪でかかる
    * でも取り出された要素はすべて小さい順にソートされているのだから毎回最悪計算量がかかるわけではなさそう.
    * いや、逆に挿入する要素が毎回heapに存在するどの要素よりも小さいから根本に挿入する必要があり、毎回最悪計算量がかかる？？
  * 配列をソートしておくのが一番実装としてはやりやすいし、引っかかる点もない
    * 最初のソートでは与えられた`nums`の要素数をnとしてnlognかかる
    * その後は現時点での内部配列に含まれている要素数をmとしてlogmで挿入箇所を見つけて、挿入をm（最悪の場合）で行う、k番目に大きい要素はindexアクセスなので定数時間
    * 10^4回要素の追加が最大で行われ、最初に与えられていた配列の長さは最大で10^4
    * 最後の方での追加の処理には、log(10^8) + 10^8がかかる
    * これだと時間がかかりすぎる
    * そもそもk番目以降の要素を保存しておく必要はない
    * 配列の末尾がk番目の要素になるようにする
    * そしたら計算するときの配列の長さは最大でも10^4
    * システム全体では最悪の場合の計算量で、10^4 * (log(10^4) + 10^4)がかかる
      * これって2sでぎりぎり終わるかなくらいの認識
      * 詳しく調べたい


## Code1

```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
      sorted_nums = sorted(nums, reverse=True)
      self.topk_nums = sorted_nums[:k]
      self.k = k
        

    def add(self, val: int) -> int:
      if len(self.topk_nums) < self.k - 1:
        raise ValueError("missing number of elements during initialization")
      if len(self.topk_nums) == self.k and val <= self.topk_nums[-1]:
        return self.topk_nums[-1]
      should_check_mte = 0
      should_check_lte =  len(self.topk_nums) - 1
      while should_check_mte <= should_check_lte:
        check_idx = should_check_lte + (should_check_mte - should_check_lte) // 2
        if self.topk_nums[check_idx] >= val:
          should_check_mte = check_idx + 1
        else:
          should_check_lte = check_idx - 1
      insert_idx = should_check_mte
      self.topk_nums.insert(insert_idx, val)
      if len(self.topk_nums) > self.k:
        self.topk_nums.pop()
      return self.topk_nums[-1]

```

# Step2 - 色々と調べてみる.

* 計算時間の見積もり.
    * Pythonの場合は, 1secあたり, 10^8ステップ計算可能.
        * [参考](https://github.com/ichika0615/arai60/pull/8#discussion_r1898337850)
        > Python の場合は 1 秒あたり 100 万ステップ程度計算できます。
* 優先度つきキューを使用する場合は, 要素数をk個に限定していればアクセスをO(1)で行える.
* kが負の場合を弾くことを検討するべきだった.
    * [参考](https://github.com/katataku/leetcode/pull/8/changes#r1856437996)
    > 負の場合、[:k] のところで、予期しないスライスができるか落ちるかで、中途半端にそれらしい値が出てくることになるでしょう。 あまり意味のないものがそれっぽく動き続けるのは、わりとデバッグのときに困ります。
* Pythonのinsertのコストは予想通り`O(n)`だった.
    * [参考１](https://wiki.python.org/moin/TimeComplexity)
    > the largest costs come from ... or from inserting or deleting somewhere near the beginning (because everything after that must move).
    * [参考２](https://docs.python.org/3/library/bisect.html#bisect.insort)
    > Keep in mind that the O(log n) search is dominated by the slow O(n) insertion step.
* 今回実装したものと同じもの（バイナリサーチで探してから挿入）は`insort`メソッドで可能.


## Code2-1

```python
import bisect

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
      if k < 0:
        raise ValueError("k must be positive integer.")
      if len(nums) < k - 1:
        raise ValueError("The number of elements in nums should be more than or equal to k - 1.")
      self.k = k
      sorted_nums = sorted(nums, reverse=True)
      self.topk_nums = sorted_nums[:self.k]

    def add(self, val: int) -> int:
      bisect.insort(self.topk_nums, val, key=lambda x: -x)
      if len(self.topk_nums) > self.k:
        self.topk_nums.pop()
      return self.topk_nums[-1]
```

## Code2-2

```python
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.topk_heap = []
        if k < 0:
            raise ValueError("k must be positive integer")
        if len(nums) < k - 1:
            raise ValueError("The number of elements should be more than or equal to k - 1")
        self.k = k
        for num in nums:
            heapq.heappush(self.topk_heap, num)

    def add(self, val: int) -> int:
        heapq.heappush(self.topk_heap, val)
        while len(self.topk_heap) > self.k:
            heapq.heappop(self.topk_heap)
        return self.topk_heap[0]
```