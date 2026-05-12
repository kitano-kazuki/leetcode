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

# Step3

## 他の人のコード

### olsen-blue : https://github.com/olsen-blue/Arai60/pull/48

* 元の問題文がPRの説明に記載されている. 元のleetcodeの問題では, タプルとして`(v以下の値からなるツリーの根, vより大きい値からなるツリーの値)`を返す
* 解法１はトップダウンによる再帰
    * 今見ている根がv以下なら, 根とその左の子孫は全員v以下.
        * 右側の子孫をv以下のツリーとvより大きいツリーにわける
        * 今の根にv以下のツリーの根をつなげる
    * 今見ている根がvより大きいなら, 根とその右の子孫は全員vより大きい.
        * 左側の子孫をv以下のツリーとvより大きいツリーに分ける
        * 今の根にvより大きいツリーの根をつける
* 解法２はボトムアップによる再帰
    * 訪れたノードから順番に処理をしていく
        * トップダウンはpost-order的な順番だが, ボトムアップはpre-order的な順番
        * 今までのv以下のツリーとvより大きいツリーの末端が引き継がれている
        * 今見ているノードがv以下だったら, 引き継がれているv以下のツリー末端の右に今見ている根とその左の子孫を追加
        * 今見ているノードを今見ている根の右川とする
    * 処理を理解するのに時間がかかった

### naoto-iwase : https://github.com/naoto-iwase/leetcode/pull/48

* lintcode版を解いている
* 自分と同様に最後に`count_nodes`関数を呼び出して, サイズが小さい方のツリーを返している
* 自分は小さい方のツリー, 大きい方のツリーでそれぞれ再帰用の関数で2pathにしたが, このコードでは, (lower, higher)のタプルとして返す単一の再帰関数を実装
    * 2 pathの方がよみやすいと自分は感じた.

### mamo3gr : https://github.com/mamo3gr/arai60/pull/58

* naoto-iwaseと同様

## 他の人のコメント

* https://github.com/goto-untrapped/Arai60/pull/54#discussion_r1778944205
    * > 「自分で手作業でできる」「人間にやり方を説明して代わりにやってもらえる」「機械にやり方を説明して代わりにやってもらえる(おおまかに、これがコードが書けること)」の順で難しくなっていくので、より簡単なのができないのだとたぶん書けないのです。
* https://github.com/t9a-dev/LeetCode_arai60/pull/47/files#r2824014277
    * > もしかすると、上の再帰と合わせてワンパスにして欲しいのかもしれないと思いましたが、私は過剰な最適化と感じます。
* https://github.com/Satorien/LeetCode/pull/60#discussion_r2728540010
    * > ワンパスでやるならば、split_bst_helper がサイズも返すようにすればいいんですが……。 まあ、速度は速くなるかもしれませんが、複雑さに見合わない気がしますね。

# Step4

## Code4-1

```python
import copy


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def split_b_s_t(self, root: TreeNode, v: int) -> TreeNode:

        def split_bst_helper(root: TreeNode | None) -> tuple[TreeNode | None, TreeNode | None]:
            if root is None:
                return None, None
            
            if root.val <= v:
                sub_smaller_root, sub_larger_root = split_bst_helper(root.right)
                root.right = sub_smaller_root
                return [root, sub_larger_root]
            else:
                sub_smaller_root, sub_larger_root = split_bst_helper(root.left)
                root.left = sub_larger_root
                return [sub_smaller_root, root]
        
        return split_bst_helper(copy.deepcopy(root))

```

