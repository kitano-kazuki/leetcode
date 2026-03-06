# Step1

## アプローチ

* マスを全て見る(DFS or BFS), ますが1だった場合は0に書き換えてそれぞれの方向を確認しに行く
* 計算量は O(M * N)
* in-placeでやらない場合は, visited配列を持っておく or copy作成

## Code1-1 (DFS)

```python
from typing import List
import copy

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_copy = copy.deepcopy(grid)
        m = len(grid_copy)
        n = len(grid_copy[0])
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        def visit_adjacents(r: int, c: int) -> None:
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if grid_copy[r][c] == "0":
                return
            grid_copy[r][c] = "0"
            for dr, dc in dirs:
                next_r = r + dr
                next_c = c + dc
                visit_adjacents(next_r, next_c)
        
        count = 0
        for r in range(m):
            for c in range(n):
                if grid_copy[r][c] == "1":
                    count += 1
                    visit_adjacents(r, c)
        
        return count
                
```

## Code1-2 (BFS)

```python
from collections import deque
import copy
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_copy = copy.deepcopy(grid)
        m = len(grid_copy)
        n = len(grid_copy[0])
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        def visit_adjacents(init_r: int, init_c: int) -> None:
            to_visit = deque()
            to_visit.append((init_r, init_c))
            while to_visit:
                r, c = to_visit.popleft()
                if r < 0 or r >= m or c < 0 or c >= n:
                    continue
                if grid_copy[r][c] == "0":
                    continue
                grid_copy[r][c] = "1"
                for dr, dc in dirs:
                    to_visit.append((r + dr, c + dc))
            return

        count = 0
        for r in range(m):
            for c in range(n):
                if grid_copy[r][c] == "1":
                    count += 1
                    visit_adjacents(r, c)

        return count

```

# Step2

## Code2-1 (DFS)

```python
from typing import List
import copy

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_copy = copy.deepcopy(grid)
        m = len(grid_copy)
        n = len(grid_copy[0])
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        def rewrite_1_to_0_and_recur_adjacents(r: int, c: int) -> None:
            grid_copy[r][c] = "0"
            for dr, dc in dirs:
                next_r = r + dr
                next_c = c + dc
                if next_r < 0 or next_r >= m or next_c < 0 or next_c >= n:
                    continue
                if grid_copy[next_r][next_c] == "0":
                    continue
                rewrite_1_to_0_and_recur_adjacents(next_r, next_c)
        
        count = 0
        for r in range(m):
            for c in range(n):
                if grid_copy[r][c] == "1":
                    count += 1
                    rewrite_1_to_0_and_recur_adjacents(r, c)
        
        return count

```          


## Code2-2 (BFS)

```python
from collections import deque
import copy
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_copy = copy.deepcopy(grid)
        m = len(grid_copy)
        n = len(grid_copy[0])
        dirs = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        def rewrite_island_to_sea(init_r: int, init_c: int) -> None:
            grid_copy[init_r][init_c] = "0"
            to_visit = deque()
            to_visit.append((init_r, init_c))
            while to_visit:
                r, c = to_visit.popleft()
                for dr, dc in dirs:
                    next_r = r + dr
                    next_c = c + dc
                    if next_r < 0 or next_r >= m or next_c < 0 or next_c >= n:
                        continue
                    if grid_copy[next_r][next_c] == "0":
                        continue
                    grid_copy[next_r][next_c] = "0"
                    to_visit.append((next_r, next_c))
            return

        count = 0
        for r in range(m):
            for c in range(n):
                if grid_copy[r][c] == "1":
                    count += 1
                    rewrite_island_to_sea(r, c)

        return count

```

# Memo

## 他の人の解法やコメント

* Magic Numberについて
    * https://github.com/n6o/leetcode_arai60/pull/17
        * WATER, LANDを用いて`0`や`1`などのマジックナンバーの意味をわかりやすくしている
* 内部関数の使用について
    * https://github.com/Hiroto-Iizuka/coding_practice/pull/17/files#r2716085615
        * > 関数のネスト(関数の中に関数を作ること)は、変数をクロージャで使いたいい場合はOK
        * > ただし、関数を隠すためにネストするのはよくない. デバッグしたいときに外部から呼び出せなくなるから
* Stack上限について
    * https://github.com/aki235/Arai60/pull/17
        * > Pythonのrecursion_limitは1000だが、入力の大きさはm,n <= 300なので、300*300=90000くらいまでありうる
    * https://github.com/Hiroto-Iizuka/coding_practice/pull/17/files#r2716085615
        * 1 <= m, n <= 300 より、最大で 9 万回の再帰呼び出しが行われます。これによりスタックオーバーフローが起こる可能性があります。
* Union-findについて
    * https://discord.com/channels/1084280443945353267/1183683738635346001/1197738650998415500
        * > union-find  は、微妙に常識から外れるかな(多くの人が知っているだろうが知らなくてもドン引きはされない)、くらいの感覚です。DFS による解法のほうは常識でしょう。
    * https://github.com/ksaito0629/leetcode_arai60/pull/16
    * https://github.com/dxxsxsxkx/leetcode
        * UnionFindの解法も試している.

## Code2-3 (Union-find)