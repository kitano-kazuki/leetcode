# Step1

## アプローチ (10:29)

* 同じ位置のものを順番に見ていけばいい
* 再帰を使うのが一番考え方としてはやりやすい
    * 与えられた部分をマージした結果のノードを返す
    * 部下にやってもらいたいものは, 自分が見ているところの左と右
    * 再帰の回数は, Nodeの一番深いところまで行く時が最大
        * 10^4
        * defaultの再帰上限には引っかかる
        * デバッグはしにくい
        * 関数呼び出しのオーバーヘッドがかかる
            * 10ns / 1呼び出し くらい？？
            * 例えば, 10^4回再帰を呼び出す場合は,
                * 10^4 * 10 = 10^5 ns = 10^2 ms = 0.1 s
                * くらい？？
* DFSを使うとどうなるかな
    * 訪れるノードを二つのスタックで管理する
        * それぞれのスタックがそれぞれの木の訪れるノードを保持
        * pre-orderでマージしていく
* BFSでもできるかな
* BFSとDFSを使うか, 再帰を使うか
    * BFS, DFS
        * 再帰の呼び出しがない分今回の問題設定では0.1sだけ早くなりそう
        * デバッグはしやすそう
    * 再帰
        * 実装が直感的
        * コード量が減る
    * 時間計算量はともにO(N)
    * 空間計算量もともにO(N)

## Code1-1 (recursion) - solved 8:33

```python
from typing import Optional
from copy import deepcopy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def mergeTrees_helper(node1: Optional[TreeNode], node2: Optional[TreeNode]) -> Optional[TreeNode]:
            if node1 is None:
                return deepcopy(node2)
            if node2 is None:
                return deepcopy(node1)
            
            merged_node = TreeNode(val=node1.val + node2.val)
            merged_tree_left = mergeTrees_helper(node1.left, node2.left)
            merged_tree_right = mergeTrees_helper(node1.right, node2.right)
            merged_node.left = merged_tree_left
            merged_node.right = merged_tree_right
            return merged_node

        return mergeTrees_helper(root1, root2)

```

## Code1-2 (DFS) - solved 21:41

```python
from typing import Optional
from copy import deepcopy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return deepcopy(root2)
        if root2 is None:
            return deepcopy(root1)

        merged_dummy_head = TreeNode()
        tree1_frontier = [root1]
        tree2_frontier = [root2]
        merge_instructions = [(merged_dummy_head, "left")]
        while tree1_frontier and tree2_frontier:
            node1 = tree1_frontier.pop()
            node2 = tree2_frontier.pop()
            target, creation_side = merge_instructions.pop()
            if node1 is None and node2 is None:
                continue
            if creation_side == "left":
                if node1 is None:
                    target.left = deepcopy(node2)
                    continue
                if node2 is None:
                    target.left = deepcopy(node1)
                    continue
                merged_node = TreeNode(node1.val + node2.val) 
                target.left = merged_node
            elif creation_side == "right":
                if node1 is None:
                    target.right = deepcopy(node2)
                    continue
                if node2 is None:
                    target.right = deepcopy(node1)
                    continue
                merged_node = TreeNode(node1.val + node2.val) 
                target.right = merged_node
            else:
                raise ValueError("creation side should be either right or left")
            tree1_frontier.append(node1.left)
            tree2_frontier.append(node2.left)
            merge_instructions.append((merged_node, "left"))
            tree1_frontier.append(node1.right)
            tree2_frontier.append(node2.right)
            merge_instructions.append((merged_node, "right"))

        return merged_dummy_head.left

```

## Code1-3 (BFS) - solved 8:27

```python
from typing import Optional
from collections import deque
from copy import deepcopy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return deepcopy(root2)
        if root2 is None:
            return deepcopy(root1)

        dummy_merged_root = TreeNode()
        frontier = deque([(root1, root2, dummy_merged_root, "left")])
        while frontier:
            next_frontier = deque()
            while frontier:
                node1, node2, target_node, creation_side = frontier.popleft()
                if node1 is None and node2 is None:
                    continue
                if node1 is None:
                    if creation_side == "left":
                        target_node.left = deepcopy(node2)
                        continue
                    if creation_side == "right":
                        target_node.right = deepcopy(node2)
                        continue
                if node2 is None:
                    if creation_side == "left":
                        target_node.left = deepcopy(node1)
                        continue
                    if creation_side == "right":
                        target_node.right = deepcopy(node1)
                        continue
                merged_node = TreeNode(node1.val + node2.val)
                if creation_side == "left":
                    target_node.left = merged_node
                elif creation_side == "right":
                    target_node.right = merged_node
                next_frontier.append((node1.left, node2.left, merged_node, "left"))
                next_frontier.append((node1.right, node2.right, merged_node, "right"))
            frontier = next_frontier
        return dummy_merged_root.left
                
```

# Step2

## 他の人のコード

* mamo3gr(https://github.com/mamo3gr/arai60/pull/22/files)
    * BFSを用いて回答(step2).
    * キューに入れる段階で新しいノードを作成, 処理の中でキューに入っていたノードのvalを書き換え
        * 自分は, キューに, 新しいノードをつけるターゲットとその方向を入れた解法
    * step3ではDFSも使用しているが, こちらも先に新しいノードを作成してスタックに追加

* Satorien(https://github.com/Satorien/LeetCode/pull/23/files)
    * rightとleftがnilの場合も考慮した, rightやleftを手に入れる関数を別で用意する方法が紹介されていた.
        * https://discord.com/channels/1084280443945353267/1262688866326941718/1297934906189549599
    * メインの解法としては再帰を使用.
    * stackを使う方法は最初にノードを作成しておいて, あとで書き換える方式(mamo3grと同じ)

* りょう(https://github.com/ryoooooory/LeetCode/pull/26/files)

* tokuhirat(https://github.com/tokuhirat/LeetCode/pull/23/files)
    * 再帰

# コメント集

* https://github.com/tarinaihitori/leetcode/pull/23#discussion_r1920919690
    * > これも別に良いコードではないですが、C++ だとどこに書き込むかをスタックに積むことができるので、少し簡単になるのです。それを擬似的に Python で表現してみました

## 調べたこと

### 関数呼び出しのオーバーヘッド

https://github.com/ksaito0629/leetcode_arai60/pull/4#discussion_r2787261329
> 関数呼び出しのオーバーヘッドは Python では何秒くらいでしょうか。(たぶん100ナノ秒にはならないくらいの桁感でしょうが、調べてみてください。)
                    
https://github.com/dorxyxki/arai60/pull/7#discussion_r2838988934
> 手元の比較: 20 ns ほどのオーバーヘッド

## Code2-1 (recursion)

```python
from typing import Optional
from copy import deepcopy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return deepcopy(root2)
        if root2 is None:
            return deepcopy(root1)
        
        merged_node = TreeNode(val=root1.val + root2.val)
        merged_node.left = self.mergeTrees(root1.left, root2.left)
        merged_node.right = self.mergeTrees(root1.right, root2.right)
        return merged_node

```

## Code2-2 (dfs)

```python
from typing import Optional
from copy import deepcopy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return deepcopy(root2)
        if root2 is None:
            return deepcopy(root1)

        def get_merged_val(node1, node2):
            val = 0
            if node1 is not None:
                val += node1.val
            if node2 is not None:
                val += node2.val
            return val

        def get_left(node):
            if node is None:
                return None
            return node.left

        def get_right(node):
            if node is None:
                return None
            return node.right
                
        
        merged_root = TreeNode()
        frontier = [(root1, root2, merged_root)]
        while frontier:
            node1, node2, merged_node = frontier.pop()
            merged_node.val = get_merged_val(node1, node2)

            node1_left = get_left(node1)
            node2_left = get_left(node2)
            if node1_left is not None or node2_left is not None:
                merged_node.left = TreeNode()
                frontier.append((node1_left, node2_left, merged_node.left))

            node1_right = get_right(node1)
            node2_right = get_right(node2)
            if node1_right is not None or node2_right is not None:
                merged_node.right = TreeNode()
                frontier.append((node1_right, node2_right, merged_node.right))
            
        return merged_root

```

## Code2-3 (bfs)

```python
from typing import Optional
from copy import deepcopy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return deepcopy(root2)
        if root2 is None:
            return deepcopy(root1)

        def get_merged_val(node1, node2):
            val = 0
            if node1 is not None:
                val += node1.val
            if node2 is not None:
                val += node2.val
            return val
        
        def get_left(node):
            if node is None:
                return None
            return node.left

        def get_right(node):
            if node is None:
                return None
            return node.right

        merged_root = TreeNode()
        frontier = [(root1, root2, merged_root)]
        while frontier:
            next_frontier = []
            while frontier:
                node1, node2, merged_node = frontier.pop()
                merged_node.val = get_merged_val(node1, node2)

                node1_left, node2_left = get_left(node1), get_left(node2)
                if node1_left is not None or node2_left is not None:
                    merged_node.left = TreeNode()
                    next_frontier.append((node1_left, node2_left, merged_node.left))
                node1_right, node2_right = get_right(node1), get_right(node2)
                if node1_right is not None or node2_right is not None:
                    merged_node.right = TreeNode()
                    next_frontier.append((node1_right, node2_right, merged_node.right))
            frontier = next_frontier
        return merged_root
                    
```

# Step3

## Code3-1 (recursion)

```python
# 1st: 1:30
# 2nd: 1:20
from typing import Optional
from copy import deepcopy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return deepcopy(root2)
        if root2 is None:
            return deepcopy(root1)
        
        merged_root = TreeNode(root1.val + root2.val)
        merged_root.left = self.mergeTrees(root1.left, root2.left)
        merged_root.right = self.mergeTrees(root1.right, root2.right)
        return merged_root

```

## Code3-2 (dfs)

```python
# 1st: 3:28
# 2nd: 3:20
from typing import Optional
from copy import deepcopy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return deepcopy(root2)
        if root2 is None:
            return deepcopy(root1)

        def get_merged_val(node1, node2):
            val = 0
            if node1 is not None:
                val += node1.val
            if node2 is not None:
                val += node2.val
            return val
        
        def get_left(node):
            if node is None:
                return None
            return node.left
        
        def get_right(node):
            if node is None:
                return None
            return node.right
        
        merged_root = TreeNode()
        frontier = [(root1, root2, merged_root)]
        while frontier:
            node1, node2, merged_node = frontier.pop()
            merged_node.val = get_merged_val(node1, node2)
            node1_left, node2_left = get_left(node1), get_left(node2)
            if node1_left is not None or node2_left is not None:
                merged_node.left = TreeNode()
                frontier.append((node1_left, node2_left, merged_node.left))
            node1_right, node2_right = get_right(node1), get_right(node2)
            if node1_right is not None or node2_right is not None:
                merged_node.right = TreeNode()
                frontier.append((node1_right, node2_right, merged_node.right))
        return merged_root

```

## Code3-3 (bfs)

```python
# 1st: 4:05
from typing import Optional
from copy import deepcopy


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None and root2 is None:
            return None
        if root1 is None:
            return deepcopy(root2)
        if root2 is None:
            return deepcopy(root1)

        def get_merged_val(node1, node2):
            val = 0
            if node1 is not None:
                val += node1.val
            if node2 is not None:
                val += node2.val
            return val

        def get_left(node):
            if node is None:
                return None
            return node.left

        def get_right(node):
            if node is None:
                return None
            return node.right
        
        merged_root = TreeNode()
        frontier = [(root1, root2, merged_root)]
        while frontier:
            next_frontier = []
            while frontier:
                node1, node2, merged_node = frontier.pop()
                merged_node.val = get_merged_val(node1, node2)
                node1_left, node2_left = get_left(node1), get_left(node2)
                if node1_left is not None or node2_left is not None:
                    merged_node.left = TreeNode()
                    next_frontier.append((node1_left, node2_left, merged_node.left))
                node1_right, node2_right = get_right(node1), get_right(node2)
                if node1_right is not None or node2_right is not None:
                    merged_node.right = TreeNode()
                    next_frontier.append((node1_right, node2_right, merged_node.right))
            frontier = next_frontier
        return merged_root

```