# Step1

## アプローチ

* 与えられた二つのノードに共通する先祖を返す
* 2 <= ノード数 <= 10^5
* 下から上に辿ることはできない
* 与えられたノードが見つかるまでにたどってきたパスを残しておく
* それぞれのパスを後ろから見て一致するか?
    * O(num_nodes_in_path^2)かかる最悪の場合で
* でもパスの長さは, たかだかO(logN)
    * ってことはこの方法でもいけそう
* 6:27

## Code1-1

* AC: 26:16
* backtrackingっぽくやろうとしたところで手こずった

```python
class Solution:
    def get_nodes_upto(self, root: TreeNode, target: TreeNode) -> list[TreeNode]:
        def dfs(node: TreeNode, path: list[TreeNode]):
            path.append(node)

            if node is target:
                return path

            if node.left is None and node.right is None:
                path.pop()
                return None

            path_leftward = None
            if node.left is not None:
                path_leftward = dfs(node.left, path)

            path_rightward = None
            if node.right is not None:
                path_rightward = dfs(node.right, path)

            if path_leftward is None and path_rightward is None:
                path.pop()
                return None
            if path_leftward is not None:
                return path_leftward
            if path_rightward is not None:
                return path_rightward
        
        return dfs(root, [])


    def find_first_common_backward(self, path1: list[TreeNode], path2: list[TreeNode]) -> TreeNode | None:
        for node1 in path1[::-1]:
            for node2 in path2[::-1]:
                if node1 is node2:
                    return node1
        return None


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = self.get_nodes_upto(root, p)
        path2 = self.get_nodes_upto(root, q)
        return self.find_first_common_backward(path1, path2)

```


# Step2

## Code2-1 (Common Node in Path)

* backtrack的にやるよりも, get_nodes_from_target_to_rootを子分にもやらせてつなぎ合わせるみたいにした方がわかりやすそう

```python
class Solution:
    def get_nodes_from_target_to_root(self, root: TreeNode, target: TreeNode) -> list[TreeNode]:

        if root is target:
            return [root]

        path_leftward = None
        if root.left is not None:
            path_leftward = self.get_nodes_from_target_to_root(root.left, target)

        path_rightward = None
        if root.right is not None:
            path_rightward = self.get_nodes_from_target_to_root(root.right, target)

        if path_leftward is None and path_rightward is None:
            return None
        if path_leftward is not None:
            path_leftward.append(root)
            return path_leftward
        if path_rightward is not None:
            path_rightward.append(root)
            return path_rightward


    def find_first_common(self, path1: list[TreeNode], path2: list[TreeNode]) -> TreeNode | None:
        for node1 in path1:
            for node2 in path2:
                if node1 is node2:
                    return node1
        return None


    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path1 = self.get_nodes_from_target_to_root(root, p)
        path2 = self.get_nodes_from_target_to_root(root, q)
        return self.find_first_common_backward(path1, path2)

```

## Code2-2 (Check existance)

* Code*-1以外の方法もないか考える
* Lowest Common Ancestor(LCA)の左と右にそれぞれ`p`, `q`が存在する.
    * ただし, LCA自身が`p`や`q`ではないとする
* つまり, 存在するかどうかを見ればいい気がする
* 存在するかどうかじゃなくて, 何個存在するかわかったほうがいいかも
* 左と右に1こずつ存在する
    * 現在のノードがLCA
* 左(右)に2個存在する
    * 起点を左(右)の子にして再帰的に考える
* 左に1個存在する, 右には存在しない (このとき今のノードが`p`や`q`なはず)
    * 今のノードがLCA
* BSTになっているから, ノードを辿れなくても存在がわかる!!
* O(logN)でできそう
    * たかだか木の高さしか見る必要がない

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while True:
            left = 0
            right = 0
            for target in [p, q]:
                if target.val < node.val:
                    left += 1
                elif target.val > node.val:
                    right += 1
            
            if left == 1 and right == 1:
                return node
            if (left == 1 and right == 0) or (left == 0 and right == 1):
                return node
            if left == 2:
                node = node.left
            else:  # right == 2
                node = node.right

```

# Step3

## Code3-2 (Check existance)

* 1:36
* 1:17
* 1:02

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        while True:
            left = 0
            right = 0
            for target in [p, q]:
                if target.val < node.val:
                    left += 1
                elif node.val < target.val:
                    right += 1
            
            if left == 1 and right == 1:
                return node
            if (left == 1 and right == 0) or (left == 0 and right == 1):
                return node
            if left == 2:
                node = node.left
            else:
                node = node.right

```
