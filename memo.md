# Step1

## アプローチ

* レベルごとに処理する順番が変わるので、方向を変数として持っておいてBFSをすればいい
    * あるいは最後にreverseするか
* DFSでやることもできる
    * 結果を格納する配列のインデックスとレベルを対応させる
    * 方向に応じて、前に挿入するか後ろに挿入するかを切りかえる（or 最後に奇数盤目をreverseする）
* 計算量は、
    * DFS, BFSともに全てのノードを訪れるのでO(N)
    * reverseする方法だとしても、奇数番目をreverseするのにかかる計算量はO(N)
    * 2000 step / 10^6 = 2ms
* 空間計算量の見積もり
    * 結果を格納する配列で 28 bytes * 2000 / 1024 = 56KB
* BFSかDFSかの使い分け
    * BFSの方が自然言語的に処理が理解しやすいので可読性が高い
    * 木の高さをkとした時, 
        * BFSは一度にリスト（あるいはキュー）に2^(k-1)個の要素が入る
        * DFSはk個で済む
        * メモリに2^(k-1)個のTreeNodeが乗り切らないときはDFSにした方が良い
            * TODO: メモリに乗り切らないってどのくらいのバイト数からなのだろう？？
    * BFSは階層ごとに処理ができる利点がある。DFSだとある階層のデータが揃うまでにほぼすべてのノードを訪れる必要がある。

## Code1-1(BFS)

```python
# solved 5:04
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        level_ordered_values = []
        is_right_to_left = False
        frontier = deque([(root)])
        while frontier:
            next_frontier = deque()
            values_at_this_level = []
            while frontier:
                node = frontier.popleft()
                values_at_this_level.append(node.val)
                if node.left is not None:
                    next_frontier.append(node.left)
                if node.right is not None:
                    next_frontier.append(node.right)
            if is_right_to_left:
                values_at_this_level = values_at_this_level[::-1]
            level_ordered_values.append(values_at_this_level)
            frontier = next_frontier
            is_right_to_left = not is_right_to_left
        return level_ordered_values

```

# Step2

## Code2-1(BFS)

* `level_ordered_values`を`level_zigzag_ordered_values`にしたのみ

```python
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        level_zigzag_ordered_values = []
        is_right_to_left = False
        frontier = deque([(root)])
        while frontier:
            next_frontier = deque()
            values_at_this_level = []
            while frontier:
                node = frontier.popleft()
                values_at_this_level.append(node.val)
                if node.left is not None:
                    next_frontier.append(node.left)
                if node.right is not None:
                    next_frontier.append(node.right)
            if is_right_to_left:
                values_at_this_level = values_at_this_level[::-1]
            level_zigzag_ordered_values.append(values_at_this_level)
            frontier = next_frontier
            is_right_to_left = not is_right_to_left
        return level_zigzag_ordered_values
        

```

# 他の人のコードやコメントを確認

* https://github.com/mamo3gr/arai60/pull/27/files
    * レベルごとの処理の部分で、先にvaluesだけ取得. その後次のレベルのノードを用意.
        * values取得のロジックが切り分けられるのは嬉しいけど、２回そのレベルを捜査する必要があるのがモヤつきはする
        * 好みの問題かなぁ
* https://github.com/Satorien/LeetCode/pull/27/files
    * depthを持っておいて、その偶奇を活用
    * reverseではなく, appendleftとappendの使い分け
* https://github.com/naoto-iwase/leetcode/pull/31/files
    * レベルごとの処理の部分で、先にそのレベルにあるノード分のintを格納できる配列を用意した後、left_to_rightかどうかに依存して、そのint配列に書き込むindexを決めている

# Step3

## Code3-1 (BFS)

```python
# 1st: 2:46
# 2nd: 計測忘れ
# 3rd: 2:01
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        frontier = deque([root])
        is_left_to_right = True
        level_order_values = []
        while frontier:
            next_frontier = deque()
            values_at_this_level = []
            while frontier:
                node = frontier.popleft()
                values_at_this_level.append(node.val)
                if node.left is not None:
                    next_frontier.append(node.left)
                if node.right is not None:
                    next_frontier.append(node.right)
            if not is_left_to_right:
                values_at_this_level = list(reversed(values_at_this_level))
            level_order_values.append(values_at_this_level)
            is_left_to_right = not is_left_to_right
            frontier = next_frontier
        return level_order_values

```