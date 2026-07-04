# Step1

## アプローチ

* 二分木が与えられて、そのパスで最も長いものを探す
    * rootは通る必要がない
* 各ノードに人を立たせている状況を想像する
* 自分自身を経由点にするか, 自分自身を含まないか
* 自分自身を経由点にする場合
    * 自分の左の子孫に対して, 「あなたを端点とする最も長いパスを教えて」と聞く
    * 右に対しても同様
* 自分自身を含まない場合, 
    * 自分の左の子孫に対して, 「あなたのサブツリーで最も長いパスを教えて」と聞く
* 上司には, 
    * 自分を端点とする最も長いパス
    * 自分のサブツリーで最も長いパスを引き継ぐ
        * これは, 自分自身を経由点にする場合も含む

## Code1-1

* AC: 12:50
* `left_subtree_length`とかの命名は変だからなんとかしたい

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter_helper(root: TreeNode | None) -> tuple[int, int]:
            if root.left is None and root.right is None:
                return 0, 0
            
            left_tail_length = -1
            left_subtree_length = -1
            if root.left is not None:
                left_tail_length, left_subtree_length = diameter_helper(root.left)

            right_tail_length = -1
            right_subtree_length = -1
            if root.right is not None:
                right_tail_length, right_subtree_length = diameter_helper(root.right)

            return (
                max(left_tail_length, right_tail_length) + 1,
                max(
                    left_subtree_length,
                    right_subtree_length,
                    left_tail_length + right_tail_length + 2
                )
            )

        tail_length, subtree_length = diameter_helper(root)
        return max(tail_length, subtree_length)
        
```

# Step2

## Code2-1 (recursion)

* 再帰のベースケースを葉ノードの場合からNoneの場合に変更

```python
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter_helper(root: TreeNode | None) -> tuple[int, int]:
            if root is None:
                return 0, 0

            left_height, left_diameter = diameter_helper(root.left)
            right_height, right_diameter = diameter_helper(root.right)

            height = max(left_height, right_height) + 1
            diameter = max(
                left_diameter,
                right_diameter,
                left_height + right_height
                )

            return height, diameter

        return diameter_helper(root)[1]

```

## Code2-2 (loop)

* post-orderにしないと解けなさそう
* `BOTH_RESOLVED`のノードをポップしたとき, stackの一番上には, そのノードの親が来ている
    * 親は`LEFT_RESOLVED`または`BOTH_RESOLVED`状態
    * `LEFT_RESOLVED`状態の親は, まだ右側を探索していない
    * `BOTH_RESOLVED`状態の親は, （popされたとき）右側が探索し終わっている

```python
import enum
import dataclasses


class VisitState(enum.Enum):
    BOTH_UNRESOLVED = 0
    LEFT_RESOLVED = 1
    BOTH_RESOLVED = 2

@dataclasses.dataclass
class NodeInfo:
    node: TreeNode
    left_height: int | None
    right_height: int | None
    state: VisitState

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0
        infos = [NodeInfo(root, None, None, VisitState.BOTH_UNRESOLVED)]
        while infos:
            if infos[-1].state == VisitState.BOTH_UNRESOLVED:
                infos[-1].state = VisitState.LEFT_RESOLVED
                node = infos[-1].node
                if node.left is not None:
                    infos.append(NodeInfo(node.left, None, None, VisitState.BOTH_UNRESOLVED))
                continue
            elif infos[-1].state == VisitState.LEFT_RESOLVED:
                infos[-1].state = VisitState.BOTH_RESOLVED
                node = infos[-1].node
                if node.right is not None:
                    infos.append(NodeInfo(node.right, None, None, VisitState.BOTH_UNRESOLVED))
                continue
            elif infos[-1].state == VisitState.BOTH_RESOLVED:
                info = infos.pop()
                if info.left_height is None:
                    info.left_height = 0
                if info.right_height is None:
                    info.right_height = 0
                diameter = info.left_height + info.right_height
                max_diameter = max(max_diameter, diameter)

                if infos:
                    parent_info = infos[-1]
                    height = max(info.left_height, info.right_height) + 1
                    if parent_info.state == VisitState.LEFT_RESOLVED:
                        parent_info.left_height = height
                    elif parent_info.state == VisitState.BOTH_RESOLVED:
                        parent_info.right_height = height
        
        return max_diameter

```

## 他の人のPRを見る

* https://github.com/docto-rin/leetcode/pull/71
* https://github.com/naoto-iwase/leetcode/pull/71        
    * `iterative`でもコードを書いていた
    * リストの参照を持たせておくことで, 親のノード(を含む一連のstack要素)に対して情報を書き込むことができる

# Step3

## Code3-2 (loop)

* 8:52
* 6:36
* 5:42
* ちなみに, informationが不加算名詞なのは知りつつもあえてリストであることをわかりやくしたくてsをつけている

```python
import dataclasses
        
        
@dataclasses.dataclass
class DFSInfo:
    node: TreeNode | None
    left_height: int = 0
    right_height: int = 0
    left_visited: bool = False
    right_visited: bool = False


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        max_diameter = 0

        informations = [DFSInfo(root)]
        while informations:
            info = informations[-1]
            if not info.left_visited and not info.right_visited:
                info.left_visited = True
                if info.node.left is not None:
                    informations.append(DFSInfo(info.node.left))
                    continue
            elif info.left_visited and not info.right_visited:
                info.right_visited = True
                if info.node.right is not None:
                    informations.append(DFSInfo(info.node.right))
                continue
            elif info.left_visited and info.right_visited:
                informations.pop()
                max_diameter = max(max_diameter, info.left_height + info.right_height)

                if informations:
                    parent_info = informations[-1]
                    height_from_parent = max(info.left_height, info.right_height) + 1

                    if parent_info.left_visited and not parent_info.right_visited:
                        parent_info.left_height = height_from_parent
                    elif parent_info.left_visited and parent_info.right_visited:
                        parent_info.right_height = height_from_parent
        
        return max_diameter
        
```
