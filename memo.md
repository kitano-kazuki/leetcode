# Step1

## アプローチ

* 全ての取りうる組み合わせをheapに入れて, 小さい順にk件保存する
  * 一つ目の配列の長さをm, 二つ目の配列の長さをnとする
  * 取りうるペアの数は m * n個
  * heapに入れる過程.
    * log(k) * m * n
  * 大まかなステップ数は,k = 10^4,  m = n = 10^5の時を考える
    * log(10^4) * 10^5 * 10^5 = 10^10
  * Pythonの1secでの実行可能ステップ数を10^7とすると, 1000秒かかる計算
* もっと効率的な方法を考える.
* 配列があらかじめ整列されているという特性を使いたい.
* 最後の方は絶対に今入っているものより大きいことが保証されるようにして, 途中でheapに入れる作業を切り上げたい
* 二つのポインタを使って絶対に小さい順になるように入れることはできないか.
* 次のペアを作る時, 各配列で採用した前の要素のうちどちらかを一つ大きい次の要素に変える.
  * この時に考えられる二つの候補のうち, 小さい方を採用することにする.
  * でもこの方法だと数えられていないペアが存在している.
* 思いつかなかったので回答を一回流し読みした.
  * 二つの配列をA, Bとする.
  * 最初にとるのは, A[0]とB[0]
  * 次に小さい値となる可能性があるもの
    * A[0], B[1]
    * A[1], B[0]
  * 例えば, A[0], B[1]が二番目に小さいものだった場合, 3番目に小さいものは
    * A[0], B[2]
    * A[1], B[0]
  * A[1], B[0]が三番目だった場合, 4番目は
    * A[0], B[2]
    * A[1], B[1]
  * つまり, 小さい数のペアを撮るたび, そのペアのどちらかのindexを+1したものを候補に加える.
  * 候補の中で一番小さいものをheapを使ってとる.
  * A[1], B[0]とA[1], B[1]が同時にheapに入ることはあるが, A[1], B[1]がA[1], B[0]より先に取られることはないので特に気にしなくていいか.
* 計算量の見積もり
  * 取り出すたびに, 2個のペアをpushしている. 全体で１個の増加
  * heapの中は多くてもk個の要素
  * O(klog(k))


## Code1-1

```python
from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        already_in_heap = set()
        candidates_heap = []
        result = []
        num_taken = 0
        if len(nums1) * len(nums2) < k:
            raise ValueError("Given arrays wouldn't yield enough pairs.")
        heapq.heappush(candidates_heap, (nums1[0] + nums2[0], 0, 0))
        while num_taken < k:
            _, smallest_idx1, smallest_idx2 = heapq.heappop(candidates_heap)
            result.append((nums1[smallest_idx1], nums2[smallest_idx2]))
            num_taken += 1
            if smallest_idx1 < len(nums1) - 1 and (smallest_idx1 + 1, smallest_idx2) not in already_in_heap:
                heapq.heappush(candidates_heap, (nums1[smallest_idx1 + 1] + nums2[smallest_idx2], smallest_idx1 + 1, smallest_idx2))
                already_in_heap.add((smallest_idx1 + 1, smallest_idx2))
            if smallest_idx2 < len(nums2) - 1 and (smallest_idx1, smallest_idx2 + 1) not in already_in_heap:
                heapq.heappush(candidates_heap, (nums1[smallest_idx1] + nums2[smallest_idx2 + 1], smallest_idx1, smallest_idx2 + 1))
                already_in_heap.add((smallest_idx1, smallest_idx2 + 1))
        return result
```

# Step2

## Code2-1 (Setですでに入れてたものかどうかを管理)

```python
from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        seen_idx1_idx2_pairs = set()
        sum_idx1_idx2_tuple_heap = []
        result = []
        num_taken = 0
        if len(nums1) * len(nums2) < k:
            raise ValueError("Given arrays wouldn't yield enough pairs.")
        heapq.heappush(sum_idx1_idx2_tuple_heap, (nums1[0] + nums2[0], 0, 0))
        while num_taken < k:
            _, cur_smallest_idx1, cur_smallest_idx2 = heapq.heappop(sum_idx1_idx2_tuple_heap)
            result.append((nums1[cur_smallest_idx1], nums2[cur_smallest_idx2]))
            num_taken += 1
            next_idx_of_idx1 = cur_smallest_idx1 + 1
            next_idx_of_idx2 = cur_smallest_idx2 + 1
            if next_idx_of_idx1 < len(nums1) and (next_idx_of_idx1, cur_smallest_idx2) not in seen_idx1_idx2_pairs:
                heapq.heappush(sum_idx1_idx2_tuple_heap, (nums1[next_idx_of_idx1] + nums2[cur_smallest_idx2], next_idx_of_idx1, cur_smallest_idx2))
                seen_idx1_idx2_pairs.add((next_idx_of_idx1, cur_smallest_idx2))
            if next_idx_of_idx2 < len(nums2) and (cur_smallest_idx1, next_idx_of_idx2) not in seen_idx1_idx2_pairs:
                heapq.heappush(sum_idx1_idx2_tuple_heap, (nums1[cur_smallest_idx1] + nums2[next_idx_of_idx2], cur_smallest_idx1, next_idx_of_idx2))
                seen_idx1_idx2_pairs.add((cur_smallest_idx1, next_idx_of_idx2))
        return result
```

## Code2-2 (Setを使わず次に入れるものを管理)

* 内部関数を使うべきかどうかの考察を下でした.

```python
from typing import List
import heapq


class Solution:
    def _append_sum_idx_tuple_if_possible(self, idx1, idx2, candidate_heap, taken_count_from_nums1_list, taken_count_from_nums2_list, nums1, nums2):
        if idx1 < 0 or idx1 >= len(nums1):
            return
        if idx2 < 0 or idx2 >= len(nums2):
            return
        is_idx1_takable = taken_count_from_nums1_list[idx1] == idx2
        is_idx2_takable = taken_count_from_nums2_list[idx2] == idx1
        if is_idx1_takable and is_idx2_takable:
            heapq.heappush(candidate_heap, (nums1[idx1] + nums2[idx2], idx1, idx2))
            return
        return
        

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        taken_count_from_nums1_list = [0] * nums1_len
        taken_count_from_nums2_list = [0] * nums2_len
        candidate_sum_idx1_idx2_tuple = []
        heapq.heappush(candidate_sum_idx1_idx2_tuple, (nums1[0] + nums2[0], 0, 0))
        result = []
        while len(result) < k:
            if len(candidate_sum_idx1_idx2_tuple) == 0:
                print("Not enough elements in nums1 and nums2. Try after changing k.")
                return result
            _, idx1, idx2 = heapq.heappop(candidate_sum_idx1_idx2_tuple)
            result.append((nums1[idx1], nums2[idx2]))
            taken_count_from_nums1_list[idx1] += 1
            taken_count_from_nums2_list[idx2] += 1
            self._append_sum_idx_tuple_if_possible(
                idx1 + 1,
                idx2,
                candidate_sum_idx1_idx2_tuple,
                taken_count_from_nums1_list,
                taken_count_from_nums2_list,
                nums1,
                nums2
            )
            self._append_sum_idx_tuple_if_possible(
                idx1,
                idx2 + 1,
                candidate_sum_idx1_idx2_tuple,
                taken_count_from_nums1_list,
                taken_count_from_nums2_list,
                nums1,
                nums2
            )
        return result
```

## Code2-3 (Setを使わない&内部関数を使用)

```python
from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        taken_count1 = [0] * len(nums1)
        taken_count2 = [0] * len(nums2)
        sum_idx1_idx2_heap = []
        def append_if_possible(idx1, idx2):
            if idx1 < 0 or idx1 >= len(nums1):
                return
            if idx2 < 0 or idx2 >= len(nums2):
                return
            is_idx1_takable = taken_count1[idx1] == idx2
            is_idx2_takable = taken_count2[idx2] == idx1
            if is_idx1_takable and is_idx2_takable:
                heapq.heappush(sum_idx1_idx2_heap, (nums1[idx1] + nums2[idx2], idx1, idx2))
            return

        heapq.heappush(sum_idx1_idx2_heap, (nums1[0] + nums2[0], 0, 0))
        result = []
        while len(result) < k:
            if len(sum_idx1_idx2_heap) == 0:
                print("Not enough elements in nums1 and nums2. Try after changing k.")
                return
            _, idx1, idx2 = heapq.heappop(sum_idx1_idx2_heap)
            taken_count1[idx1] += 1
            taken_count2[idx2] += 1
            result.append((nums1[idx1], nums2[idx2]))
            append_if_possible(idx1 + 1, idx2)
            append_if_possible(idx1, idx2 + 1)
        return result

```

## 内部関数を使うべきかどうか

`code2-2`では, 内部関数を使わずに, `class Solution`のメソッドとして, 引数に与えられた`idx`を`heap`に加える処理を記述した.
その理由は, 内部関数を定義すると, 関数が呼び出されるたびに毎回関数を生成するように感じられたからである.
改めて, まずは自分の知識をもとにどちらがいいか考えて, その後必要な情報を調べることにする.

### 自分の考えメモ

内部関数を定義すると, その時点での関数の状態を持ったクロージャが作られそう.
クロージャが作られる過程があまり記憶に自信がない.
構文解析の時点ではクロージャは関係ない？？
コンパイル時にクロージャを考慮してコンパイルなのかな？ 内部関数で使う外側の変数を引数と一緒にレジスタに渡して関数呼び出しするようにする？？ それか勝手に全部展開する？？
普通の関数のコンパイルだったら, その処理をまとめたものをどこかに記述してジャンプできるようなラベルつけておく(アセンブリ的な解釈)

コンパイル時に関数が作られるだけなら, 内部関数で定義しても, クラスメソッドとして定義してもコンパイル後の速度には影響しなさそう.
ただ, Pythonにおいては, コンパイルも実行時にするから, 内部関数の呼び出し回数分, 新たにその関数をコンパイルして実行する必要が出てくる？

あとは, 引数の受け渡しのドローバックも考えたい.
内部関数の場合, その内部関数内で使う外側の変数はどうやって渡されているのか.
これが, コンパイルした結果普通の関数呼び出しと同じように引数として渡されているなら, 内部関数で定義しても, クラスメソッドで定義指定も一緒.
でも, 内部関数内で使う外側の変数が何らかの理由で引数として渡されなくて済むなら, 関数呼び出しの際にスタックに積んで, 復帰する手間がない分少しだけ早くなる？？ だとしても, 1変数あたり, ldとstが１回ずつか.


### 調べたこと

* `LOAD_FAST`は関数内でローカル変数にアクセスするときのバイトコード. 配列インデックスへのアクセスなので高速.
* `LOAD_GLOBAL`はグローバル変数にアクセスするときのバイトコード. 辞書ルックアップなので`LOAD_FAST`より低速.
* Pythonでは, 内部関数がある場合, その外側の関数の呼び出しのたびに関数オブジェクトが作られる.
* 内部関数の時, その外部関数のスコープでは, 内部関数は`LOAD_FAST`で読み取れる.
* 一方で, 別の関数として定義した場合は, `LOAD_GLOBAL`で呼びたい関数名を探す必要がある.
* 今回は, `LOAD_GLOBAL`によるオーバーヘッドが内部関数の関数オブジェクトを複数回作るオーバーヘッドを上回った可能性がありそう.

#### [StackOverflow. 2013. Are nested functions faster than global functions in Python?](https://stackoverflow.com/questions/14122195/are-nested-functions-faster-than-global-functions-in-python)

> There are several parts that have an effect here:
> 1) The time to define the function (create the function object)
> 2) The time to look up the function object by name
> 3) The time to actually call the function.

> LOAD_GLOBAL is much slower than LOAD_FAST

#### [Python. 2026. dis - Disassembler for Python bytecode](https://docs.python.org/3/library/dis.html)

> LOAD_FAST(var_num)
> Pushes a reference to the local co_varnames[var_num] onto the stack.

> LOAD_GLOBAL(namei)
> Loads the global named co_names[namei>>1] onto the stack.


#### [reddit. 2019. When not to use nested functions?](https://www.reddit.com/r/learnpython/comments/e2wo2x/when_not_to_use_nested_functions/)

> Nesting functions does not make things slower. Whether it's a good idea depends on the structure of your actual program.

#### [KTakao. 2024. the P and E at closures.](https://github.com/KTakao01/learnPython/pull/26/files?short_path=bb366b7#diff-bb366b7159037f4134baa7228f2836d359b62bad41314b813911e41294b74988)

> 外部関数が実行されて初めて内部関数が作成される。




### 実験結果

それぞれの方法で実行した結果を示す
`time_comparison.py`に実装.

内部関数を使った方が早かったけど, ほぼ同じ実行時間くらい

```bash
Class Method: 0.552294839466922
Inner Method: 0.5485293312277645
```

## Setを使うかどうか

* https://discord.com/channels/1084280443945353267/1200089668901937312/1222573940610695341
  * > あと、本当は、(x - 1, y) と (x, y - 1) が両方 pairs の中にある、または、x, y どちらかが0でなければ、heap に足さなくていいとは思うんですよね。
  * 追加する必要のないものを追加していたのは自分も少し気になっていた部分.
    * 今回は実装が楽と思って深い比較をせずに, とりあえず追加する方法をとった.
    * もう少しそれぞれのPro, Conを考えてもよかった.

M = Nの時は, 対角線上に候補が並ぶ時(M個)に最大のHeapの数になりそう.
```bash
. . . o
. . o #
. o # #
o # # #
```

M != Nの時は, MとNのうち小さい方??
```bash
. . o 
. o # 
. # # 
o # # 
```
```bash
. .  
. o  
. #  
o #  
```

でも, Set使う方法でもO(min(k, M, N))になる？？
Set使う方法と使わない方法で差が顕著になる例を考えたい.

以下の例で`x`の部分は, Setを使うと入っている部分

```bash
. . . o
. o x #
. x # #
o # # #
```
```bash
. . . .
. o x x
. x # #
. x # #
. x # #
```

片方の配列のidxが固定され続けた時に, 一番無駄が多い.
`nums1`側のidxを固定し続けて値を取っていた場合, 無駄な候補が最大`M - 1`個ある.
その後, `nums2`側のidxを固定し続けて値を取っていた場合, 無駄な候補が最大`N - 1`個ある.
つまり, Setを使うことによる無駄なスペースの消費量は最悪の場合で`M + N - 2`かな？
結果, 計算量もヒープの長さが増える分, 挿入に最悪で`O(log(X + M + N - 2))`かかる時がある. `O(log(X))`がSetを使わなかった場合の最悪の計算量とする. 

どのくらい遅くなるかでいうと, 
`log(X + M + N - 2) - log(X) = log(1 + M / X + N / X - 2 / X)`
くらい.

`X`は`min(M, N, k)`なので, `M < N`の場合を考えて, `X = M`とする.
`log(1 + 1 + N / M - 2 / M)`
Mが十分大きい時は,
`log(2 + N / M)`

条件より `M < N`なので, `N / M = diff (> 0)`とする
`log(2 + diff)`

つまり, `M`と`N`がほぼ同じ値を取るときは, Setの使用の有無は関係ないが,
`M`と`N`の差が激しい時はSetを使用しない方法の方が効率的になる.

具体的に差が無視できなくなるのを, 挿入に実行時間が1秒変わるタイミングだとすると

`log(2 + diff) = 10^7`
`2 + diff = e^(10^7)`
2は無視できるほどdiffに比べて小さいので
`diff = e^(10^7)`
計算機では, `inf`となってしまった.

ということは, `Set`を使っても使わなくても問題ない？？

