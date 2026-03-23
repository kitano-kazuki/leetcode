# Step1

## アプローチ

* BFSを普通にやれば良さそう
* Node全部訪れるので計算量はO(N)

## Code1-1 (BFS)

```python
# 1st: 3:29

from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        result = []
        frontier = deque([(root)])
        while frontier:
            next_level_frontier = deque([])
            nodes_at_this_level = []
            while frontier:
                node = frontier.popleft()
                nodes_at_this_level.append(node.val)
                if node.left is not None:
                    next_level_frontier.append(node.left)
                if node.right is not None:
                    next_level_frontier.append(node.right)
            frontier = next_level_frontier
            result.append(nodes_at_this_level)
        return result

```

# Step2

* `result`という変数名は抽象的すぎるので`node_chunks_by_level`に変更

```python
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        node_chunks_by_level = []
        frontier = deque([(root)])
        while frontier:
            next_level_frontier = deque([])
            nodes_at_this_level = []
            while frontier:
                node = frontier.popleft()
                nodes_at_this_level.append(node.val)
                if node.left is not None:
                    next_level_frontier.append(node.left)
                if node.right is not None:
                    next_level_frontier.append(node.right)
            frontier = next_level_frontier
            node_chunks_by_level.append(nodes_at_this_level)
        return node_chunks_by_level


```

# 他の人のコードやコメントを確認

* mamo3gr(https://github.com/mamo3gr/arai60/pull/25/files)
    * 再帰関数の実装もしているが、BFSが読みやすいとしていた
    * BFS実装は概ね同じ。変数に登場させるのを`node`ではなく`val`にしていた。`val`の方が今回の返り値が`list[list[int]]`であることを考えると適切か。
* nanae772(https://github.com/nanae772/leetcode-arai60/pull/26/files)
    * BFSの実装は概ね同じ。結果の配列に値を加えるタイミングが各レベル処理の手前&for loopでレベルごとの処理をしているのだが、若干読みにくくなっている印象。
        * 次のレベルへの引き継ぎの部分は、各レベルの最後にまとめておきたい
            * 今回で言うと、`frontier = next_level_frontier`と`node_chunks_by_level.append...`の部分
* Satorien(https://github.com/Satorien/LeetCode/pull/26/files)
    * BFSの実装は概ね同じ。結果を格納する配列名が`level_ordered_values`
    * 次のレベルの探索ノード配列にノードを入れる段階で`None`の判定をせずに、最後に`filter`関数でNoneを弾く方法もトライしている。`list(filter(None,nodes))`
    * 結果を入れる配列を、各レベル処理の最初に追加して, 各レベル処理では`level_ordered_values[-1].append...`としてレベルの最初に追加した配列に値を加えるようにしている。