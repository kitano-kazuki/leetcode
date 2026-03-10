# Step1

## アプローチ

* 最も深い場所を知りたい
    * BFSかDFS
    * これは全てのノードを訪問する必要があるのでO(N)


## Code1-1 (DFS) - solved 3:52

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        node = root
        frontier = [(node, 1)]
        maximum_depth = 0
        while frontier:
            node, depth = frontier.pop()
            maximum_depth = max(maximum_depth, depth)
            if node.left is not None:
                frontier.append((node.left, depth + 1))
            if node.right is not None:
                frontier.append((node.right, depth + 1))
        
        return maximum_depth
            
```

## Code1-2 (Recursion) - solved 0:46

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_max_depth = self.maxDepth(root.left)
        right_max_depth = self.maxDepth(root.right)
        return max(left_max_depth, right_max_depth) + 1

```

## Code1-3 (BFS) - solved 2:12

```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        frontier = deque()
        frontier.append(root)
        depth = 0
        while frontier:
            num_cur_frontiers = len(frontier)
            depth += 1
            for _ in range(num_cur_frontiers):
                node = frontier.popleft()
                if node.left is not None:
                    frontier.append(node.left)
                if node.right is not None:
                    frontier.append(node.right)
        
        return depth

```

# 他の人のコードや調べたこと

* 1 - https://github.com/n6o/leetcode_arai60/pull/20/changes
    * 思いついた解法３種類全部一緒だった
    * 実装もほぼ一緒
* 2 - https://github.com/TakayaShirai/leetcode_practice/pull/21
    * 同様に解法３種類やっている
* 3 - https://github.com/Hiroto-Iizuka/coding_practice/pull/21
    * Pythonだと再帰に忌避感を持っていた方がいいかも
        * > 個人的にはPythonで再帰を書くことにかなり抵抗があるので、iterativeでもこの程度のコード量で済むならiterativeで書きたいと思いました。
* 4 - https://github.com/xbam326/leetcode/pull/23
* 5 - https://github.com/dxxsxsxkx/leetcode/pull/21


# Step2

## Code2-1 (DFDS)

```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        node = root
        frontier = [(node, 1)]
        maximum_depth = 0
        while frontier:
            node, depth = frontier.pop()
            if node is None:
                continue
            maximum_depth = max(maximum_depth, depth)
            frontier.append((node.left, depth + 1))
            frontier.append((node.right, depth + 1))
        
        return maximum_depth

```

## Code2-2 (Recursion)

```python
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

```

## Code2-3(BFS)

```python
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        frontier = deque()
        frontier.append(root)
        depth = 0
        while frontier:
            num_cur_frontiers = len(frontier)
            depth += 1
            for _ in range(num_cur_frontiers):
                node = frontier.popleft()
                if node is None:
                    continue
                frontier.append(node.left)
                frontier.append(node.right)
        
        return depth

```

# Step3