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