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

## Code2-3-1 (Union-find, 何も見ずに描いたやつ. Step1相当)

```python
from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.ranks = [1] * size
    
    def find(self, idx):
        if self.parents[idx] == idx:
            return idx
        parent = self.find(self.parents[idx])
        self.parents[idx] = parent
        return parent
    
    def union(self, idx1, idx2):
        parent1 = self.find(idx1)
        parent2 = self.find(idx2)
        if self.ranks[parent1] < self.ranks[parent2]:
            self.parents[parent1] = parent2
        elif self.ranks[parent1] > self.ranks[parent2]:
            self.parents[parent2] = parent1
        else:
            self.parents[parent2] = parent1
            self.ranks[parent1] += 1
        return


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        calc_flatten_idx = lambda row_col_tuple : row_col_tuple[0] * num_cols + row_col_tuple[1]
        num_elements = num_rows * num_cols
        uf = UnionFind(num_elements)
        NO_GROUP = -1
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "0":
                    uf.parents[calc_flatten_idx((r, c))] = NO_GROUP
                if r + 1 < num_rows:
                    if grid[r][c] == "1" and grid[r + 1][c] == "1":
                        uf.union(calc_flatten_idx((r, c)), calc_flatten_idx((r + 1, c)))
                if c + 1 < num_cols:
                    if grid[r][c] == "1" and grid[r][c + 1] == "1":
                        uf.union(calc_flatten_idx((r, c)), calc_flatten_idx((r, c + 1)))
        island_groups = set()
        for i in range(num_elements):
            if uf.parents[i] == NO_GROUP:
                continue
            island_groups.add(uf.find(i))
        return len(island_groups)

```

## Code2-3-2 (Union-find, Step2相当)

* `lambda`で複数引数取る方法を知らなかったので調べた.
    * https://docs.python.org/3/reference/expressions.html#lambda
    * 普通に引数を`lambda`の後に`,`区切りで並べるだけでよい
* 直接`uf.parents`を`UnionFind`のクラス外からいじるのは良くなさそうなので, 他の人のコードを参考に`is_root`を定義. islandの数を数える時にgridの値が1でかつ, rootとなる要素の時に島の数を増加
    * https://github.com/shining-ai/leetcode/blob/8615f109c56fa5dacdfff743d81f8d27b6ab90e4/arai60/17-20_Graph_BFS_DFS/17_200_Number%20of%20Islands/level_2.py#L89

```python
from typing import List
from collections import defaultdict


class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.ranks = [1] * size
    
    def find(self, idx):
        if self.parents[idx] == idx:
            return idx
        parent = self.find(self.parents[idx])
        self.parents[idx] = parent
        return parent
    
    def union(self, idx1, idx2):
        parent1 = self.find(idx1)
        parent2 = self.find(idx2)
        if self.ranks[parent1] < self.ranks[parent2]:
            self.parents[parent1] = parent2
        elif self.ranks[parent1] > self.ranks[parent2]:
            self.parents[parent2] = parent1
        else:
            self.parents[parent2] = parent1
            self.ranks[parent1] += 1
        return

    def is_root(self, idx):
        if self.find(idx) == idx:
            return True
        return False


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        calc_flatten_idx = lambda row, col : row * num_cols + col
        num_elements = num_rows * num_cols
        uf = UnionFind(num_elements)
        for r in range(num_rows):
            for c in range(num_cols):
                if r + 1 < num_rows:
                    if grid[r][c] == "1" and grid[r + 1][c] == "1":
                        uf.union(calc_flatten_idx(r, c), calc_flatten_idx(r + 1, c))
                if c + 1 < num_cols:
                    if grid[r][c] == "1" and grid[r][c + 1] == "1":
                        uf.union(calc_flatten_idx(r, c), calc_flatten_idx(r, c + 1))
        num_islands = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1" and uf.is_root(calc_flatten_idx(r, c)):
                    num_islands += 1
        return num_islands
```

# Step3

## Code3-1 (DFS)

```python
from typing import List
import copy

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_copy = copy.deepcopy(grid)
        num_rows = len(grid)
        num_cols = len(grid[0])

        WATER = "0"
        LAND = "1"
        
        def rewrite_land_to_water_and_recur_adjacents(row, col):
            if row < 0 or num_rows <= row:
                return
            if col < 0 or num_cols <= col:
                return
            if grid_copy[row][col] == WATER:
                return
            
            grid_copy[row][col] = WATER
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
            for dr, dc in dirs:
                next_row = row + dr
                next_col = col + dc
                if next_row < 0 or num_rows <= next_row:
                    continue
                if next_col < 0 or num_cols <= next_col:
                    continue
                if grid_copy[next_row][next_col] == WATER:
                    continue
                rewrite_land_to_water_and_recur_adjacents(next_row, next_col)

            return     

        
        num_islands = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid_copy[r][c] == WATER:
                    continue
                num_islands += 1
                rewrite_land_to_water_and_recur_adjacents(r, c)
        
        return num_islands
            
```

## Code3-3 (Union-find)

```python
from typing import List

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

    def is_root(self, idx):
        return self.parent[idx] == idx

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])

        WATER = "0"
        LAND = "1"

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
        
        num_islands = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == WATER:
                    continue
                if uf.is_root(flatten_row_col(r, c)):
                    num_islands += 1
        
        return num_islands

```