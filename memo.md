# Step1

## アプローチ

* 再帰呼び出しでやる
    * ざっくり方針
        * 自分の左に対して、仕事を指示
        * 自分の右に対して、仕事を指示
        * 自分の左と右がそれぞれ正しいかどうかをみる仕事を与えられる
        * 左の結果と右の結果がただしいなら、上司に正しいと教える
    *  計算量
        * すべてのノードを訪れるのでO(N)
            * step数は10^4程度だとすると, 10^4 / 10^6 = 0.01 sec程度
        * メモリは再帰のスタック分必要
            * 最大で（左に偏り続ける木の場合で）10^4回の再帰が行われる可能性がある
* stackを使ったDFSでやる場合
    * pre-orderになる
    * 処理候補をstackに積むときに, 親の情報と自分が小さくあるべきか大きくあるべきかを伝える
* queをつかったBFSでやる場合
    * DFS同様に,処理候補をqueに入れるときに, 親の情報と自分が小さくあるべきかどうかを伝える
* DFSかBFSかは与えられた木の構造やパソコンのメモリ状況で変わる
    * DFSが適している状況
        * 同レベルのノード数が多すぎてメモリに乗らない時
            * 例えば、パソコンの残りメモリが8GBだとする
            * ノードを一回作成するたびに新たに消費されるバイト数 => 300 byteと見積もる
                * classの参照(PyTypeObject) = 8 bytes
                * attibuteの参照を集めたdictへの参照 296 bytes
                * attributeの参照先を新たにオブジェクトとして作る場合はそのオブジェクトのサイズ
            * 300 * x = 8 * 1024 * 1024 * 1024なので x = 3 * 10^7
            * 思ったよりも少なかった
    * BFSが適している状況
        * 与えられた木が左に偏りすぎていてノードの深さ分メモリに乗り切らないとBFSが良い

## Code1-1 (Recursion)

```python
# solved 10:01
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        def is_valid_bst_helper(node: TreeNode, minimum_val: int, maximum_val: int) -> bool:
            if not (minimum_val < node.val < maximum_val):
                return False

            is_left_subtree_valid = True
            if node.left is not None:
                is_left_subtree_valid = is_valid_bst_helper(node.left, minimum_val, node.val)

            is_right_subtree_valid = True
            if node.right is not None:
                is_right_subtree_valid = is_valid_bst_helper(node.right, node.val, maximum_val)

            return is_left_subtree_valid and is_right_subtree_valid

        return is_valid_bst_helper(root, float("-inf"), float("inf"))
```
## Code1-2 (DFS)

```python
# solved 1:34

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        node_to_visit = [(root, float("-inf"), float("inf"))]
        while node_to_visit:
            node, minimum_val, maximum_val = node_to_visit.pop()
            if not (minimum_val < node.val < maximum_val):
                return False
            if node.left is not None:
                node_to_visit.append((node.left, minimum_val, node.val))
            if node.right is not None:
                node_to_visit.append((node.right, node.val, maximum_val))
        return True
```

## Code1-1 (BFS)

```python
# solved 2:38
from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        frontier = deque([(root, float("-inf"), float("inf"))])
        while frontier:
            next_frontier = deque()
            while frontier:
                node, minimum_val, maximum_val = frontier.popleft()
                if not (minimum_val < node.val < maximum_val):
                    return False
                if node.left is not None:
                    next_frontier.append((node.left, minimum_val, node.val))
                if node.right is not None:
                    next_frontier.append((node.right, node.val, maximum_val))
            frontier = next_frontier
        return True

        
```