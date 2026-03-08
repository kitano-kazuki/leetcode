# Step1

## アプローチ

* `200. number of islands`のように, `LAND`を`WATER`に変えていく. その時に消した個数を記録して, その最大値を求める.
    * 追記: 結局, visitedを使って再帰関数を面積を返す関数にして設計した
    * 元の配列を破壊しないようにしたい. 
        * ユースケース的には, 一番大きい島を見つけたいだけ（変更はしたくなさそう）
    * `DFS`でやる場合, Pythonのデフォルトの再帰上限は`1000`だから`setrecursionlimit`で変更してあげる必要がある.
        * leetcodeでは大丈夫
    * 再帰回数の見積もり. 行数を`m`, 列数を`n`とする.
        * `LAND`となっているものは`WATER`に書き換えられるので, たかだかマスの数分しか処理は行われない.
        * 再帰の回数は最大で`m * n`
    * 空間計算量
        * 配列を非破壊にするためにコピーするので`m * n`
        * それとは別に, 再帰呼び出しでも`m * n`使う可能性がある.
        * 全体で O(m * n)
    * 時間計算量
        * 全てのマスを見るのでO(m * n)
* `UnionFind`を使ってもできそう, 同じグループに属しているものの個数の最大値を考えればいい
    * 元の配列はコピーしなくても破壊することはない
    * 各マスをみるので m * n回のunionが最大で行われる.
        * 一回のunionにかかる処理の最悪の場合を考える.
            * Nをunionfindのサイズとして, 逆アッカーマン関数 O(α(N))
            * でも逆アッカーマン関数がどのくらいか知らない...
            * path compressionだけでlogNになっているから, それよりは早いはず...
    * でも一番最初の方は, 最悪の場合にはならない
        * 各要素が自身がrootになっているので
        * O(m * n * α(N))とするのは不適切？？
            * もちろん Upper boundではあるが...
    

## Code1-1 (DFS)

```python
from typing import List
import copy

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        num_rows = len(grid)
        num_cols = len(grid[0])

        WATER = 0
        LAND = 1

        def calc_area_size_from_unvisited(row, col, visited):
            if row < 0 or num_rows <= row or col < 0 or num_cols <= col:
                return 0
            if grid[row][col] == WATER:
                return 0
            visited[row][col] = True
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            areas = 1
            for dr, dc in dirs:
                next_row = row + dr
                next_col = col + dc
                if next_row < 0 or num_rows <= next_row:
                    continue
                if next_col < 0 or num_cols <= next_col:
                    continue
                if grid[next_row][next_col] == WATER:
                    continue
                if visited[next_row][next_col]:
                    continue
                areas += calc_area_size_from_unvisited(next_row, next_col, visited)
            return areas

        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]
        
        max_areas = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == WATER:
                    continue
                if not visited[r][c]:
                    area = calc_area_size_from_unvisited(r, c, visited)
                    max_areas = max(area, max_areas)

        return max_areas
                
```

## Code1-2 (UnionFind)

```python
from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, idx):
        if self.parent[idx] == idx:
            return idx
        parent_idx = self.find(self.parent[idx])
        self.parent[idx] = parent_idx
        return parent_idx

    def union(self, idx1, idx2):
        parent_idx1 = self.find(idx1)
        parent_idx2 = self.find(idx2)
        if parent_idx1 == parent_idx2:
            return
        
        if self.rank[parent_idx1] < self.rank[parent_idx2]:
            self.parent[parent_idx1] = parent_idx2
            return
        elif self.rank[parent_idx2] < self.rank[parent_idx1]:
            self.parent[parent_idx2] = parent_idx1
            return
        else:
            self.parent[parent_idx2] = parent_idx1
            self.rank[parent_idx1] += 1
            return


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        WATER = 0
        LAND = 1

        uf = UnionFind(num_rows * num_cols)
        flatten_row_col = lambda row, col : row * num_cols + col

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == WATER:
                    continue
                if r + 1 < num_rows and grid[r + 1][c] == LAND:
                    uf.union(flatten_row_col(r, c), flatten_row_col(r + 1, c))
                if c + 1 < num_cols and grid[r][c + 1] == LAND:
                    uf.union(flatten_row_col(r, c), flatten_row_col(r, c + 1))
        
        group_number_to_area = defaultdict(int)
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == WATER:
                    continue
                group_number_to_area[uf.find(flatten_row_col(r, c))] += 1

        if not group_number_to_area:
            return 0

        return max(group_number_to_area.values())

```

# Step2

* どちらのコードも変更なし

## Code2-1 (DFS)

```python
from typing import List
import copy

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        num_rows = len(grid)
        num_cols = len(grid[0])

        WATER = 0
        LAND = 1

        def calc_area_size_from_unvisited(row, col, visited):
            if row < 0 or num_rows <= row or col < 0 or num_cols <= col:
                return 0
            if grid[row][col] == WATER:
                return 0
            visited[row][col] = True
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            areas = 1
            for dr, dc in dirs:
                next_row = row + dr
                next_col = col + dc
                if next_row < 0 or num_rows <= next_row:
                    continue
                if next_col < 0 or num_cols <= next_col:
                    continue
                if grid[next_row][next_col] == WATER:
                    continue
                if visited[next_row][next_col]:
                    continue
                areas += calc_area_size_from_unvisited(next_row, next_col, visited)
            return areas

        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]
        
        max_areas = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == WATER:
                    continue
                if not visited[r][c]:
                    area = calc_area_size_from_unvisited(r, c, visited)
                    max_areas = max(area, max_areas)

        return max_areas
                

```

## Code2-2 (UnionFind)

```python
from typing import List
from collections import defaultdict

class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.rank = [0] * size

    def find(self, idx):
        if self.parent[idx] == idx:
            return idx
        parent_idx = self.find(self.parent[idx])
        self.parent[idx] = parent_idx
        return parent_idx

    def union(self, idx1, idx2):
        parent_idx1 = self.find(idx1)
        parent_idx2 = self.find(idx2)
        if parent_idx1 == parent_idx2:
            return
        
        if self.rank[parent_idx1] < self.rank[parent_idx2]:
            self.parent[parent_idx1] = parent_idx2
            return
        elif self.rank[parent_idx2] < self.rank[parent_idx1]:
            self.parent[parent_idx2] = parent_idx1
            return
        else:
            self.parent[parent_idx2] = parent_idx1
            self.rank[parent_idx1] += 1
            return


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        WATER = 0
        LAND = 1

        uf = UnionFind(num_rows * num_cols)
        flatten_row_col = lambda row, col : row * num_cols + col

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == WATER:
                    continue
                if r + 1 < num_rows and grid[r + 1][c] == LAND:
                    uf.union(flatten_row_col(r, c), flatten_row_col(r + 1, c))
                if c + 1 < num_cols and grid[r][c + 1] == LAND:
                    uf.union(flatten_row_col(r, c), flatten_row_col(r, c + 1))
        
        group_number_to_area = defaultdict(int)
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == WATER:
                    continue
                group_number_to_area[uf.find(flatten_row_col(r, c))] += 1

        if not group_number_to_area:
            return 0

        return max(group_number_to_area.values())
            

```

## Memo

* `setrecursionlimit`について
    * https://github.com/olsen-blue/Arai60/pull/18#discussion_r1919805259
        * > まあ、setrecursionlimit できるような環境ならば設定すればいいわけですが、たとえば、ライブラリーを作っているとすると、これはグローバルに設定を変えることになるので他のところに影響が出る可能性がありますね。

* `stack`による`DFS`
    * `setrecursionlimit`を変更することに忌避感があるのであれば, stackを用いた`DFS `も検討できる
        * https://github.com/aki235/Arai60/pull/18/files#diff-9fe83a5ebd0765dc3d775b7bbf3048d8f6ff02247c075977086bf46f21a077b4R98

* 内部関数の仕様について気になったから調べた
    * 内部関数はその内部関数の実行時に関数オブジェクトが作られる.
    * 内部関数の定義後に定義した変数も関数オブジェクトに含まれるのでは？
        * スコープでは, どちらも外部関数内の変数として扱われるはず.
        * 以下の例はどちらも同じ動作をした

```python
def outer():
    x = 1
    def inner():
        return x
    print(inner())
    return


def outer2():
    def inner2():
        return x
    x = 1
    print(inner2())
    return
```



## Code2-3 (DFS with Stack)

```python
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        WATER = 0
        LAND = 1
        visited = [[False for _ in range(num_cols)] for _ in range(num_rows)]

        def get_area_of_island(row, col):
            assert not visited[row][col]
            to_visit = [(row, col)]
            area_size = 0
            while to_visit:
                r, c = to_visit.pop()
                if visited[r][c]:
                    continue
                visited[r][c] = True
                area_size += 1
                dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dr, dc in dirs:
                    next_r = r + dr
                    next_c = c + dc
                    if next_r < 0 or num_rows <= next_r:
                        continue
                    if next_c < 0 or num_cols <= next_c:
                        continue
                    if grid[next_r][next_c] == WATER:
                        continue
                    if visited[next_r][next_c]:
                        continue
                    to_visit.append((next_r, next_c))
            return area_size
                
        maximum_area = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == WATER:
                    continue
                if visited[r][c]:
                    continue
                area = get_area_of_island(r, c)
                maximum_area = max(area, maximum_area)
        return maximum_area

```
