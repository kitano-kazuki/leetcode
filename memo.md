# Step1

## アプローチ

* 二分探索木をある値vを境にして二つに分ける.
* 値の重複はないとみなすのが普通？？
    * 問題の制約に全部値は違うってかいてあった
* 一番単純な方法は, 全部のノードを見て再構成する方法
    * この方法だともとの構造を崩す可能性がある
    * 構造的には, v以下のノードはどこかのサブツリーとして存在するから削除する形で手に入れたい
* ノード数がどっちの方が多くなりそうかあらかじめわかると嬉しい
    * v以下を削除
    * vより大きいものを削除
    * で2pathでやるのが楽かなぁ
* v以下の削除で仕事の引き継ぎを考える
    * 今見ているノードの値
        * vより大きい
            * 今見ているノードと右の子孫は生き残る
            * 左側に対して削除依頼
        * v以下
            * 自分自身と左の子孫は削除される.
            * 右の子孫のうち, はじめてvより大きくなるものを手にいれるようお願いする

## Code1-1

```python
import copy
import collections
import sys

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def split_b_s_t(self, root: TreeNode, v: int) -> TreeNode:

        # vより大きい二分探索木
        copied_root1 = copy.deepcopy(root)
        larger_tree = self._delete_less_than_or_equal(copied_root1, v)

        # v以下の二分探索木
        copied_root2 = copy.deepcopy(root)
        smaller_tree = self._delete_more_than(copied_root2, v)

        if self._count_num_nodes(larger_tree) >= self._count_num_nodes(smaller_tree):
            return larger_tree
        else:
            return smaller_tree

    def _delete_less_than_or_equal(self, root: TreeNode | None, v: int) -> TreeNode | None:
        if root is None:
            return None

        if root.val > v:
            root.left = self._delete_less_than_or_equal(root.left, v)
            return root
        
        return self._delete_less_than_or_equal(root.right, v)

    def _delete_more_than(self, root: TreeNode | None, v: int) -> TreeNode | None:
        if root is None:
            return None

        if root.val <= v:
            root.right = self._delete_more_than(root.right, v)
            return root
        
        return self._delete_more_than(root.left, v)
        
    def _count_num_nodes(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        
        return 1 + self._count_num_nodes(root.left) + self._count_num_nodes(root.right)

```    

# Step2

## Code2-1

* `deepcopy`した結果は直後ですぐ使っているから, 変数として保存せずにそのまま引数で渡した方が見やすいと思った

```python
import copy

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def split_b_s_t(self, root: TreeNode, v: int) -> TreeNode:

        larger_tree = self._delete_less_than_or_equal(copy.deepcopy(root), v)
        smaller_tree = self._delete_more_than(copy.deepcopy(root), v)

        if self._count_num_nodes(larger_tree) >= self._count_num_nodes(smaller_tree):
            return larger_tree
        else:
            return smaller_tree

    def _delete_less_than_or_equal(self, root: TreeNode | None, v: int) -> TreeNode | None:
        if root is None:
            return None

        if root.val > v:
            root.left = self._delete_less_than_or_equal(root.left, v)
            return root
        
        return self._delete_less_than_or_equal(root.right, v)

    def _delete_more_than(self, root: TreeNode | None, v: int) -> TreeNode | None:
        if root is None:
            return None

        if root.val <= v:
            root.right = self._delete_more_than(root.right, v)
            return root
        
        return self._delete_more_than(root.left, v)
        
    def _count_num_nodes(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        
        return 1 + self._count_num_nodes(root.left) + self._count_num_nodes(root.right)



```
