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

## Code2-1
