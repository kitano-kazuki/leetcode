# Step1

## アプローチ

* 再帰的に反転する動作を繰り返せばよさそう
* 自分の役目, 見るべきノードの左と右の子を入れ替える.
* 引き継ぎたいこと, 見るべきノード
* ループでもかける
* ノードの数が100なので再帰上限にはひっかからない
* 実装は重くないのでどっちも実装してみる
* O(N)

## Code1-1 (Recrusion)

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

```

## Code1-2 (loop)

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        frontier = [root]
        while frontier:
            next_frontier = []
            for node in frontier:
                node.left, node.right = node.right, node.left
                if node.left is not None:
                    next_frontier.append(node.left)
                if node.right is not None:
                    next_frontier.append(node.right)
            frontier = next_frontier
        
        return root

```

# Step2

## 他の人のコードを見る

* https://github.com/ryosuketc/leetcode_grind75/pull/6/files
    * 再帰の解法はほぼ同じ.
        * `root->left = invertTree(root->left);`としているが, 返り値を再活用するのがいいかどうか
        * 自分は, `invertTree`の帰り値は何かなと気にする手間が省けるので`invertTree(root.left)`だけ呼ぶのが好み
            * この場合は, 内部関数として別で帰り値を持たない関数を定義した方がわかりやすいかも
* https://github.com/Ryotaro25/leetcode_first60/pull/71
    * ループを使った解法は一緒
* https://github.com/huyfififi/coding-challenges/pull/6

# Step3

## Code3-2 (loop)

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        frontier = [root]
        while frontier:
            next_frontier = []
            for node in frontier:
                node.left, node.right = node.right, node.left
                if node.left is not None:
                    next_frontier.append(node.left)
                if node.right is not None:
                    next_frontier.append(node.right)
            frontier = next_frontier
        
        return root

```