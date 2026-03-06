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