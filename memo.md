# Step1

## アプローチ

* maximumdepthと同様に考えられそう
    * recursion
        * 左の部下には, 左の部下を頭として一番小さい深さを教えてもらう
        * 右の部下には, 右の部下を頭として一番小さい深さを教えてもらう
        * 自分は, 受け取った二つのうち小さい方+1が最小だと上司に伝える
    * bfs
        * 各レベルごとに見ていく
        * 子を持たないノードができたら終了
    * dfs
        * 子を持たないノードに到達した時に, minimum_depthを更新する
* 計算量は, O(N). ノード数をNとする
* recursionをする場合の最大再帰スタックはN

## Code1-1 (Recursion) - solved 4:56

```python
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1

        if root.left is None:
            return self.minDepth(root.right) + 1
        
        if root.right is None:
            return self.minDepth(root.left) + 1
        
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
        
```

## Code1-2 (DFS) - solved 2:40

```python
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        frontier = [(root, 1)]
        minimum_depth = float("inf")
        while frontier:
            node, depth = frontier.pop()
            if node.left is None and node.right is None:
                minimum_depth = min(minimum_depth, depth)
                continue
            if node.left is not None:
                frontier.append((node.left, depth + 1))
            if node.right is not None:
                frontier.append((node.right, depth + 1))
        return minimum_depth

```
    
## Code1-3 (BFS) - solved 2:42

```python
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        depth = 0
        frontier = deque()
        frontier.append(root)
        while frontier:
            num_cur_frontier = len(frontier)
            depth += 1
            for _ in range(num_cur_frontier):
                node = frontier.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left is not None:
                    frontier.append(node.left)
                if node.right is not None:
                    frontier.append(node.right)
        
        raise ValueError()
        
```

# 他の人のコードやコメント集を見る

今回からarai60完走者のを見ることにした

* 1 - https://github.com/mamo3gr/arai60/pull/20/files
    * BFS
        * BFSで`deque`を使わない方法をやっている.
            * 注目している主役がわかりやすい
        * BFSのエラー文をどうするか迷って空白にしたが, `something went wrong`くらいアバウトでもいいのか
            * `raise RuntimeError("You can not reach here. There is something wrong in the implementation")`
            * RuntimeErrorを使うのは考えに及ばなかった
    * DFS
        * `root.left`と`root.right`をループで回している
            * バイナリツリーじゃなくなった場合でも応用が効きそう
        * 変数`is_leaf`とかにif文の条件をまとめたら読みやすくなりそう
    * 再帰
        * `root.left`と`root.right`をループで回す方法を再帰でもやっている
* 2 - https://github.com/Satorien/LeetCode/pull/22/files
    * 帰りがけをstackにしたものがコメントで紹介されていた
        * https://github.com/potrue/leetcode/pull/22#discussion_r2112567800
        * 一般的にみんながstackで行うdfsは行きがけ
        * 一方で, 一般的にみんなが再帰で行うdfsは帰りがけ
* 3 - https://github.com/ryoooooory/LeetCode/pull/25/files
    * whileの中でループすることが決まっているので`while(true)`を使っていた
        * そうしたら`raise RuntimeError`をしなくてよくなる
* 4 - https://github.com/naoto-iwase/leetcode/pull/21/files
    * 再帰関数の終了処理と, そもそもの与えられた引数の確認が別なら内部関数で処理を分けるのが見やすそう
    * BFSのやり方についてのコメントがあった

* ちなみに, 多くの人は再帰=DFSという表記をしているが, 本PRでは, DFSはstackを使った再帰を表すこととする

```
あと、BFS をするのに
node_queue
num_node_in_level
で数を数えて、次のレベルに行くの、少しややこしいと思っています。データの整合性が取れているということは、読んでいる人からすると全部読み終わらないと分からないからです。書いている人は分かるわけですが。
つまり、一つの変数に、2つの違う種類のものを入れておいて、その境界を個数で管理しているわけですよね。
```