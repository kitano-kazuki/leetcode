# Step1

## アプローチ

* 62.unique pathsと同様に, 左と上のパターンの数を足して今のマスのパターン数とする
* obstacleがあった場合は, 足さないこと(=0のパターン数)とする
* メモ化再帰の場合は, obstacleの場合は0を返すようにすればいい

## Code1-1 (DP)

```python
# solved: 10:22
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        SPACE = 0
        OBSTACLE = 1

        if obstacleGrid[0][0] == OBSTACLE:
            return 0

        previous_unique_paths = [0] * n
        previous_unique_paths[0] = 1
        for row in range(m):
            unique_paths = [0] * n
            for column in range(n):
                if obstacleGrid[row][column] == OBSTACLE:
                    unique_paths[column] = 0
                else:
                    unique_paths[column] = previous_unique_paths[column] + (unique_paths[column - 1] if column > 0 else 0)
            previous_unique_paths = unique_paths

        return previous_unique_paths[-1]

```

## Code1-2 (Recursion)

```python
# solved: 7:57

from functools import cache


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        @cache
        def unique_paths_with_obstacles_helper(destination_row: int, destination_column: int) -> int:
            if destination_row < 0 or destination_column < 0:
                return 0

            OBSTACLE = 1
            if obstacleGrid[destination_row][destination_column] == OBSTACLE:
                return 0

            if destination_row == 0 and destination_column == 0:
                return 1

            return unique_paths_with_obstacles_helper(destination_row - 1, destination_column) + unique_paths_with_obstacles_helper(destination_row, destination_column - 1)

        return unique_paths_with_obstacles_helper(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)

```

# Step2

* m, nをnum_rowsやnum_colsに変更

## Code2-1 (DP)

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        num_rows = len(obstacleGrid)
        num_columns = len(obstacleGrid[0])
        OBSTACLE = 1

        if obstacleGrid[0][0] == OBSTACLE:
            return 0

        previous_unique_paths = [0] * num_columns
        previous_unique_paths[0] = 1
        for row in range(num_rows):
            unique_paths = [0] * num_columns
            for column in range(num_columns):
                if obstacleGrid[row][column] == OBSTACLE:
                    unique_paths[column] = 0
                else:
                    unique_paths[column] = previous_unique_paths[column] + (unique_paths[column - 1] if column > 0 else 0)
            previous_unique_paths = unique_paths

        return previous_unique_paths[-1]
```

## Code2-2 (Recursion)

```python
from functools import cache


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:

        @cache
        def unique_paths_with_obstacles_helper(destination_row: int, destination_column: int) -> int:
            if destination_row < 0 or destination_column < 0:
                return 0

            OBSTACLE = 1
            if obstacleGrid[destination_row][destination_column] == OBSTACLE:
                return 0

            if destination_row == 0 and destination_column == 0:
                return 1

            return unique_paths_with_obstacles_helper(destination_row - 1, destination_column) + unique_paths_with_obstacles_helper(destination_row, destination_column - 1)

        return unique_paths_with_obstacles_helper(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)

```

## 他の人のコード

* https://github.com/mamo3gr/arai60/pull/32
* https://github.com/naoto-iwase/leetcode/pull/39
    * スタート地点やゴール地点が障害物であるかどうかのチェック
* https://github.com/olsen-blue/Arai60/pull/34 
    * 2次元DP
    * 定数はモジュールレベルで定義する
        * https://github.com/olsen-blue/Arai60/pull/34#discussion_r1967663378
            * > 関数内に定数があるのは違和感を感じました。 PEP8 に下記のように記載ございました。なので関数の外側ではあるのかなと思いました。
        * https://peps.python.org/pep-0008/#constants
            * > Constants are usually defined on a module level and written in all capital letters with underscores separating words. Examples include MAX_OVERFLOW and TOTAL.
    * 変数名はスコープの長さと連動して長くすると良いらしい
        * https://github.com/olsen-blue/Arai60/pull/34#discussion_r1979998266
            * 同じ派です。「複数箇所に出現する」とありますが、GoのGoogleスタイルガイドにも...
        * https://google.github.io/styleguide/go/decisions#variable-names
            * > The general rule of thumb is that the length of a name should be proportional to the size of its scope and inversely proportional to the number of times that it is used within that scope.
    * 入力のリストが空の時の配慮をする

## 他の人のコメント

* 打ち切り処理を入れるかどうか
    * https://github.com/dxxsxsxkx/leetcode/pull/34#discussion_r2935592260
        * > 「打ち切り処理を入れるか」といったことは結局は、そのプログラムがどのようなものを扱うかの分布との兼ね合いです。たとえば、ライブラリーのソート関数は、意外とすでにソート済みが入力に来ることが多い、と判断されて、すでにソート済みの場合は何もしない処理が入っていたりすることがあります。しかし、これは分布を試して確認しないことにはなんとも言えない話です。なので、とりあえず、シンプルに作って、必要性との兼ね合いで後から入れることが割と好まれるのですね。

# Step3

## Code3-1 (DP)

```python
# 1st: 3:30
# 2nd: 2:28
# 3rd: 2:06

OBSTACLE = 1

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        num_rows = len(obstacleGrid)
        num_columns = len(obstacleGrid[0])

        if obstacleGrid[0][0] == OBSTACLE or obstacleGrid[num_rows - 1][num_columns - 1] == OBSTACLE:
            return 0

        previous_unique_paths = [1] + [0] * (num_columns - 1)
        for r in range(num_rows):
            unique_paths = [None] * num_columns
            for c in range(num_columns):
                if obstacleGrid[r][c] == OBSTACLE:
                    unique_paths[c] = 0
                    continue
                unique_paths[c] = previous_unique_paths[c] + (unique_paths[c - 1] if c > 0 else 0)
            previous_unique_paths = unique_paths
        
        return previous_unique_paths[-1]
            
```