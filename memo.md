# Step1

## アプローチ

* 行列`mat`の各セルごとに, 最も近い`0`までの距離を知りたい
* パッと思いつくのは, 各セルごとに, そこを開始点として`bfs`をする方法
* Nをセルの数(行 x 列)とする
* ただ, この場合の計算量は, O(N^2)となり, 実行時間はだいたい10^8 / 10^6 ~= 10^2 sec程度
* 各セルごとにそこからいける最も近い0までの距離は一度だけの計算でも十分な気がする
* ここまで 4:08. 実装に移る

## Code1-1 (DFS with Visit Flag: WA)

* 20:17書いたけどWA
* `(r, c)`で呼び出した`updateMatrix`の結果は, その時の`visited`の状態によって変わるため一意ではない
* 以下の例の場合, (0, 0)が`0`に至るまでのステップが`7`として出力される
* `bfs`をやって最短のものを見つけようとした場合も同様に`visited`の状態によって出力が意図しないものになりそう

```
1 1 1 0
1 1 1 1
1 1 1 1
1 1 1 1
```

```python
import functools


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        num_rows = len(mat)
        num_columns = len(mat[0])

        visited = set()

        @functools.cache
        def measure_distance_from(r: int, c: int) -> int:
            if r < 0 or num_rows <= r or c < 0 or num_columns <= c:
                return float("inf")
            if mat[r][c] == 0:
                return 0
            
            visited.add((r, c))

            return 1 + min(
                measure_distance_from(r + 1, c) if (r + 1, c) not in visited else float("inf"),
                measure_distance_from(r - 1, c) if (r - 1, c) not in visited else float("inf"),
                measure_distance_from(r, c + 1) if (r, c + 1) not in visited else float("inf"),
                measure_distance_from(r, c - 1) if (r, c - 1) not in visited else float("inf"),
            )

        min_distances = [[None] * num_columns for _ in range(num_rows)]
        for r in range(num_rows):
            for c in range(num_columns):
                visited = set()
                min_distances[r][c] = measure_distance_from(r, c)
        
        return min_distances
        
```

## Code1-2 (BFS flooding: AC)

* 逆転の発想をしてみる.
* `0`となっているところから, 時間経過ごとに隣接するセルを`1`から`0`に変えるようにする
* `0`となっているセルの個数を数えておけば, 処理の終了も把握できる
* 6:40でAC

```python
import copy


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        mat = copy.deepcopy(mat)

        num_rows = len(mat)
        num_columns = len(mat[0])

        zero_cells = []
        for r in range(num_rows):
            for c in range(num_columns):
                if mat[r][c] == 0:
                    zero_cells.append((r, c))

        min_distances = [[None] * num_columns for _ in range(num_rows)]
        
        distance = 0
        while zero_cells:
            next_zero_cells = []
            for r, c in zero_cells:
                min_distances[r][c] = distance
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if r + dr < 0 or num_rows <= r + dr or c + dc < 0 or num_columns <= c + dc:
                        continue
                    if mat[r + dr][c + dc] == 0:
                        continue
                    mat[r + dr][c + dc] = 0
                    next_zero_cells.append((r + dr, c + dc))
            distance += 1
            zero_cells = next_zero_cells
        
        return min_distances
        
```

# Step2

## Code2-2 (BFS flooding)

* 変更なし

```python
import copy


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        mat = copy.deepcopy(mat)

        num_rows = len(mat)
        num_columns = len(mat[0])

        zero_cells = []
        for r in range(num_rows):
            for c in range(num_columns):
                if mat[r][c] == 0:
                    zero_cells.append((r, c))

        min_distances = [[None] * num_columns for _ in range(num_rows)]
        
        distance = 0
        while zero_cells:
            next_zero_cells = []
            for r, c in zero_cells:
                min_distances[r][c] = distance
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if r + dr < 0 or num_rows <= r + dr or c + dc < 0 or num_columns <= c + dc:
                        continue
                    if mat[r + dr][c + dc] == 0:
                        continue
                    mat[r + dr][c + dc] = 0
                    next_zero_cells.append((r + dr, c + dc))
            distance += 1
            zero_cells = next_zero_cells
        
        return min_distances
        
```

## 他の人のPRを見る

* https://github.com/naoto-iwase/leetcode/pull/73
    * `実装2`は自分のコードとほぼ同じになっていた
    * `実装3`では, セルに至るパスを`left`と`top`に制限した場合の距離, `bottom`と`right`に制限した場合の距離をそれぞれ出している
        * この方法は思いつかなかった
* https://github.com/ryosuketc/leetcode_grind75/pull/27
    * `Step2`では上記`実装3`と同様の方向を制限したtwo pathでの解法
* https://github.com/huyfififi/coding-challenges/pull/27

## Code2-3 (many path)

```python

UNREACHABLE = float("inf")

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        num_rows = len(mat)
        num_cols = len(mat[0])

        distance = [[UNREACHABLE] * num_cols for _ in range(num_rows)]

        def get_distance(r:int, c: int) -> int|float:
            if r < 0 or num_rows <= r or c < 0 or num_cols <= c:
                return UNREACHABLE
            return distance[r][c]

        for r in range(num_rows):
            for c in range(num_cols):
                if mat[r][c] == 0:
                    distance[r][c] = 0
                else:
                    top_distance = get_distance(r - 1, c)
                    left_distance = get_distance(r, c - 1)
                    distance[r][c] = min(top_distance, left_distance) + 1
        
        for r in range(num_rows - 1, -1, -1):
            for c in range(num_cols - 1, -1, -1):
                if mat[r][c] == 0:
                    distance[r][c] = 0
                else:
                    bottom_distance = get_distance(r + 1, c)
                    right_distance = get_distance(r, c + 1)
                    distance[r][c] = min(distance[r][c], min(bottom_distance, right_distance) + 1)

        return distance

        
```

# Step3

## Code3-2 (BFS flooding)

```python
import copy


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        mat = copy.deepcopy(mat)

        num_rows = len(mat)
        num_cols = len(mat[0])

        zero_cells = []
        for r in range(num_rows):
            for c in range(num_cols):
                if mat[r][c] == 0:
                    zero_cells.append((r, c))
        
        min_distances = [[None] * num_cols for _ in range(num_rows)]
        distance = 0
        while zero_cells:
            next_zero_cells = []
            for r, c in zero_cells:
                min_distances[r][c] = distance
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if r + dr < 0 or num_rows <= r + dr or c + dc < 0 or num_cols <= c + dc:
                        continue
                    if mat[r + dr][c + dc] == 0:
                        continue
                    mat[r + dr][c + dc] = 0
                    next_zero_cells.append((r + dr, c + dc))
            zero_cells = next_zero_cells
            distance += 1
        
        return min_distances


```
