# Step1

## アプローチ

* `sr`, `sc`をスタートとして, 隣接する色が同じセルを`color`に変えていく
* BFSまたはDFSでできる
* BFSの方がより現実の動作に近いからBFSで実装する
* 再帰でもループでもいいが練習のためループで実装する
* 全部のセルを見る場合が最大の実行時間になる
    * 50 * 50 / 10^6 ~= 10^-3 sec程度
* 2:50

## Code1-1

* 8:02

```python
import copy


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        image = copy.deepcopy(image)

        num_rows = len(image)
        num_cols = len(image[0])
        if (sr < 0 or num_rows <= sr) or (sc < 0 or num_cols <= sc):
            return image

        original_color = image[sr][sc]

        frontier = [(sr, sc)]
        visited = set()
        while frontier:
            next_frontier = []
            for r, c in frontier:
                visited.add((r, c))
                image[r][c] = color
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_r = r + dr
                    new_c = c + dc
                    if (new_r < 0 or num_rows <= new_r) or (new_c < 0 or num_cols <= new_c):
                        continue
                    if (new_r, new_c) in visited:
                        continue
                    if image[new_r][new_c] != original_color:
                        continue
                    next_frontier.append((new_r, new_c))
            frontier = next_frontier
        
        return image
        
```

# Step2

## Code2-1

* 範囲に入っているかどうかの判定を関数に切り出した

```python
import copy


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def is_in_image(row: int, col: int):
            if row < 0 or num_rows <= row:
                return False
            if col < 0 or num_cols <= col:
                return False
            return True

        image = copy.deepcopy(image)

        num_rows = len(image)
        num_cols = len(image[0])
        if not is_in_image(sr, sc):
            return image

        original_color = image[sr][sc]

        frontier = [(sr, sc)]
        visited = set()
        while frontier:
            next_frontier = []
            for r, c in frontier:
                visited.add((r, c))
                image[r][c] = color
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_r = r + dr
                    new_c = c + dc
                    if not is_in_image(new_r, new_c):
                        continue
                    if (new_r, new_c) in visited:
                        continue
                    if image[new_r][new_c] != original_color:
                        continue
                    next_frontier.append((new_r, new_c))
            frontier = next_frontier
        
        return image
        
```

## 他の解法を見る

* 再帰(dfs)が多かった

# Step3

## Code3-1

* 6:09
* 4:33
* 3:07

```python
import copy


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        image_copy = copy.deepcopy(image)

        num_rows = len(image_copy)
        num_cols = len(image_copy[0])

        def is_in_image(row: int, col: int) -> bool:
            if row < 0 or num_rows <= row:
                return False
            if col < 0 or num_cols <= col:
                return False
            return True
        
        if not is_in_image(sr, sc):
            return image_copy
        
        original_color = image_copy[sr][sc]

        coordinates = [(sr, sc)]
        visited = set()
        while coordinates:
            next_coordinates = []
            for r, c in coordinates:
                visited.add((r, c))
                image_copy[r][c] = color
                for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_r = r + dr
                    new_c = c + dc
                    if not is_in_image(new_r, new_c):
                        continue
                    if (new_r, new_c) in visited:
                        continue
                    if image_copy[new_r][new_c] != original_color:
                        continue
                    next_coordinates.append((new_r, new_c))
            coordinates = next_coordinates

        return image_copy

```
