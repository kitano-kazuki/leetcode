# Step1

## アプローチ

* 腐っているオレンジに隣接しているオレンジがどんどん腐っていく
* 腐っているオレンジを起点に隣接するオレンジを腐らせる
    * 新しく腐ったオレンジについて次は処理をする
* すべてのオレンジの個数分処理が行われるから
    * O(N * M)
* 1:36


## Code1-1

* AC: 6:14

```python
import copy


EMPTY = 0
FRESH = 1
ROTTEN = 2


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        grid = copy.deepcopy(grid)
        
        num_fresh_oranges = 0
        rotten_oranges = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == EMPTY:
                    continue
                if grid[r][c] == FRESH:
                    num_fresh_oranges += 1
                    continue
                if grid[r][c] == ROTTEN:
                    rotten_oranges.append((r, c))
                    continue

        if num_fresh_oranges == 0:
            return 0
        
        minutes = 0
        while rotten_oranges:
            next_rotten_oranges = []
            minutes += 1
            for r, c in rotten_oranges:
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if r + dr < 0 or len(grid) <= r + dr or c + dc < 0 or len(grid[0]) <= c + dc:
                        continue
                    if grid[r + dr][c + dc] == FRESH:
                        grid[r + dr][c + dc] = ROTTEN
                        num_fresh_oranges -= 1
                        if num_fresh_oranges == 0:
                            return minutes
                        next_rotten_oranges.append((r + dr, c + dc))
                        continue
            rotten_oranges = next_rotten_oranges

        return -1
        
```

# Step2

## Code2-1

* 変更なし

```python
import copy


EMPTY = 0
FRESH = 1
ROTTEN = 2


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        grid = copy.deepcopy(grid)
        
        num_fresh_oranges = 0
        rotten_oranges = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == EMPTY:
                    continue
                if grid[r][c] == FRESH:
                    num_fresh_oranges += 1
                    continue
                if grid[r][c] == ROTTEN:
                    rotten_oranges.append((r, c))
                    continue

        if num_fresh_oranges == 0:
            return 0
        
        minutes = 0
        while rotten_oranges:
            next_rotten_oranges = []
            minutes += 1
            for r, c in rotten_oranges:
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if r + dr < 0 or len(grid) <= r + dr or c + dc < 0 or len(grid[0]) <= c + dc:
                        continue
                    if grid[r + dr][c + dc] == FRESH:
                        grid[r + dr][c + dc] = ROTTEN
                        num_fresh_oranges -= 1
                        if num_fresh_oranges == 0:
                            return minutes
                        next_rotten_oranges.append((r + dr, c + dc))
                        continue
            rotten_oranges = next_rotten_oranges

        return -1
        
```

## 他の人のPRを見る

* https://github.com/tom4649/Coding/pull/70
    * DFSでも実装している
* https://github.com/huyfififi/coding-challenges/pull/41
    * whileの条件に`fresh_count`を入れて, 最後に経経時間を返す方法
        * 読みやすそう

# Step3

## Code3-1

* 7:02
* 5:46
* 3:27

```python
import copy

EMPTY = 0
FRESH = 1
ROTTEN = 2


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        grid = copy.deepcopy(grid)
        num_rows = len(grid)
        num_cols = len(grid[0])

        fresh_count = 0
        rotten_oranges = []
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == EMPTY:
                    continue
                if grid[r][c] == FRESH:
                    fresh_count += 1
                    continue
                if grid[r][c] == ROTTEN:
                    rotten_oranges.append((r, c))
                    continue
        
        minutes = 0
        while fresh_count > 0 and rotten_oranges:
            next_rotten_oranges = []
            for r, c in rotten_oranges:
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if r + dr < 0 or num_rows <= r + dr or c + dc < 0 or num_cols <= c + dc:
                        continue
                    if grid[r + dr][c + dc] == EMPTY or grid[r + dr][c + dc] == ROTTEN:
                        continue
                    if grid[r + dr][c + dc] == FRESH:
                        grid[r + dr][c + dc] = ROTTEN
                        fresh_count -= 1
                        next_rotten_oranges.append((r + dr, c + dc))
                        continue
            minutes += 1
            rotten_oranges = next_rotten_oranges
        
        if fresh_count > 0:
            return -1
        return minutes

```
