# Step1

## アプローチ

* 今まで見た値と自分が見るべきノードを渡される
* 自分が見るノードが葉だったら, 足したものがtargetになるかかくにん
* そうじゃなかったら足したものと次見るノードを引き継ぐ
* 関数による再帰呼び出しでも, stackを使ったDFSでもいけそう
* BFSでもできそう
* 関数呼び出しの木の深さ分行われるから, 最悪の場合で5000

## Code1-1 (Recursion)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum
        next_targetSum = targetSum - root.val
        return self.hasPathSum(root.left, next_targetSum) or self.hasPathSum(root.right, next_targetSum)

```

## Code1-2 (DFS)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False
        frontier = [(root, targetSum)]
        while frontier:
            node, target = frontier.pop()
            if node.left is None and node.right is None:
                if node.val == target:
                    return True
                continue
            if node.left is not None:
                frontier.append((node.left, target - node.val))
            if node.right is not None:
                frontier.append((node.right, target - node.val))
        return False

        

```

## Code1-3 (BFS)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False
        
        frontier = [(root, targetSum)]
        while frontier:
            next_frontier = []
            while frontier:
                node, target = frontier.pop()
                if node.left is None and node.right is None:
                    if node.val == target:
                        return True
                    continue
                if node.left is not None:
                    next_frontier.append((node.left, target - node.val))
                if node.right is not None:
                    next_frontier.append((node.right, target - node.val))
            frontier = next_frontier
        
        return False


```

# Step2

## Code2-1 (Recursion)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False
        is_leaf = root.left is None and root.right is None
        if is_leaf and root.val == targetSum:
            return True
        next_targetSum = targetSum - root.val
        return self.hasPathSum(root.left, next_targetSum) or self.hasPathSum(root.right, next_targetSum)

```

## Code2-2 (DFS)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False
        node_to_visit = [(root, 0)]
        while node_to_visit:
            node, pathsum_before_this_node = node_to_visit.pop()
            is_leaf = node.left is None and node.right is None
            if is_leaf and pathsum_before_this_node + node.val == targetSum:
                return True
            if node.left is not None:
                node_to_visit.append((node.left, pathsum_before_this_node + node.val))
            if node.right is not None:
                node_to_visit.append((node.right, pathsum_before_this_node + node.val))
        return False

``` 

## Code2-3 (BFS)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root is None:
            return False
        
        frontier = [(root, 0)]
        while frontier:
            next_frontier = []
            while frontier:
                node, pathsum_before_this_node = frontier.pop()
                is_leaf = node.left is None and node.right is None
                if is_leaf and pathsum_before_this_node + node.val == targetSum:
                    return True
                if node.left is not None:
                    next_frontier.append((node.left, pathsum_before_this_node + node.val))
                if node.right is not None:
                    next_frontier.append((node.right, pathsum_before_this_node + node.val))
            frontier = next_frontier
        
        return False

```