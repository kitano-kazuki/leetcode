# Step1

## アプローチ

* preorderの方でrootに該当するもの(=x)がわかる
* inorderの方のxの位置(=i)がわかれば, inorder[:i]がrootより左側にあるもの, inorder[i+1:]がrootより右側にあるもの
* 再帰的に役割を分担したい.
    * 左範囲と右範囲, root値が渡される
    * rootのノードを作ってそれを上司に伝える
    * 左側の部下 => root値とそのrootを基準にした左範囲と右範囲を渡す
    * 右側の部下 => 同上
* 数字がユニークであるという特徴が前提
* 計算量は, 全てのノードを作るのでO(N)
* スタックの最大数はN(=3000)

## Code1-1 (Recursion)

```python
# solved: 26:45


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not len(preorder) == len(inorder):
            raise ValueError("the length of the given two list are not equal.")
        value_to_preorder_index = {}
        value_to_inorder_index = {}
        for i in range(len(preorder)):
            value_to_preorder_index[preorder[i]] = i
            value_to_inorder_index[inorder[i]] = i
        
        def build_tree_helper(
            preorder_left_inclusive: int, 
            preorder_right_inclusive: int, 
            inorder_left_inclusive: int, 
            inorder_right_inclusive: int
        ) -> TreeNode | None:
            if not (preorder_left_inclusive <= preorder_right_inclusive):
                return None
            root_value = preorder[preorder_left_inclusive]
            if root_value not in inorder:
                raise KeyError(f"{root_value} is not found in the given inorder list.")
            root_pos_in_inorder = value_to_inorder_index[root_value]
            num_left_nodes = root_pos_in_inorder - inorder_left_inclusive
            root_node = TreeNode(root_value)
            left_tree = build_tree_helper(
                preorder_left_inclusive + 1,
                preorder_left_inclusive + num_left_nodes,
                inorder_left_inclusive,
                root_pos_in_inorder - 1
            )
            right_tree = build_tree_helper(
                preorder_left_inclusive + num_left_nodes + 1,
                preorder_right_inclusive,
                root_pos_in_inorder + 1,
                inorder_right_inclusive
            )
            root_node.left = left_tree
            root_node.right = right_tree
            return root_node

        return build_tree_helper(0, len(preorder) - 1, 0, len(inorder) - 1)
```

# Step2

`if root_value not in inorder:`としてしまっていたので`if root_value not in value_to_inorder_index:`に変更

## Code2-1 (Recursion)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not len(preorder) == len(inorder):
            raise ValueError("the length of the given two list are not equal.")
        value_to_preorder_index = {}
        value_to_inorder_index = {}
        for i in range(len(preorder)):
            value_to_preorder_index[preorder[i]] = i
            value_to_inorder_index[inorder[i]] = i
        
        def build_tree_helper(
            preorder_left_inclusive: int, 
            preorder_right_inclusive: int, 
            inorder_left_inclusive: int, 
            inorder_right_inclusive: int
        ) -> TreeNode | None:
            if not (preorder_left_inclusive <= preorder_right_inclusive):
                return None
            root_value = preorder[preorder_left_inclusive]
            if root_value not in value_to_inorder_index:
                raise KeyError(f"{root_value} is not found in the given inorder list.")
            root_pos_in_inorder = value_to_inorder_index[root_value]
            num_left_nodes = root_pos_in_inorder - inorder_left_inclusive
            left_tree = build_tree_helper(
                preorder_left_inclusive + 1,
                preorder_left_inclusive + num_left_nodes,
                inorder_left_inclusive,
                root_pos_in_inorder - 1
            )
            right_tree = build_tree_helper(
                preorder_left_inclusive + num_left_nodes + 1,
                preorder_right_inclusive,
                root_pos_in_inorder + 1,
                inorder_right_inclusive
            )
            root_node = TreeNode(root_value)
            root_node.left = left_tree
            root_node.right = right_tree
            return root_node

        return build_tree_helper(0, len(preorder) - 1, 0, len(inorder) - 1)

```

# 他の人のコードやコメントを確認

* https://github.com/mamo3gr/arai60/pull/28/files
    * stackを使ったDFS
    * Spanクラスをdataclassとして定義
* https://github.com/Satorien/LeetCode/pull/29/files
    * stackを使ったDFS
* https://github.com/naoto-iwase/leetcode/pull/34/files
    * queueを使ったBFS
    * BFSで訪れる順番がそのままin-orderの際の順番であることを利用して, whileによるqueueの処理の外側にpre_order_indexを保持 -> 一個要素を処理するたびにこれをインクリメント
* コメント集
    * preorderを順番に見ながら作っていく方法
        * https://discord.com/channels/1084280443945353267/1247673286503039020/1302320188351320135
    * inorderを順番に見ながら作っていく方法
        * https://discord.com/channels/1084280443945353267/1247673286503039020/1300957861614063616


## Code2-2 (Preorder)

```python
import dataclasses


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


@dataclasses.dataclass
class Range:
    left_index_inclusive: int
    right_index_inclusive: int

    def contains_in_range(self, index: int) -> bool:
        return self.left_index_inclusive <= index <= self.right_index_inclusive

    def get_range_right(self) -> int:
        return self.right_index_inclusive
    
    def get_range_left(self) -> int:
        return self.left_index_inclusive


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None
        if len(preorder) != len(inorder):
            return None

        node_value_to_inorder_index = {}
        for i in range(len(inorder)):
            node_value_to_inorder_index[inorder[i]] = i

        dummy = TreeNode()

        # stores 
        # 1.nodes which may have child nodes, 
        # 2.index ranges in inorder-array where left child value exist, 
        # 3.index ranges in inorder-array where right child value exist
        INVALID_RANGE = Range(-1, -1)
        stack = [(dummy, Range(0, len(inorder) - 1), INVALID_RANGE)]

        preorder_index = 0
        while preorder_index < len(preorder):
            node_value = preorder[preorder_index]
            parent_node, left_child_range, right_child_range = stack[-1]
            node_value_index_in_inorder = node_value_to_inorder_index[node_value]
            is_left_child = left_child_range.contains_in_range(node_value_index_in_inorder)
            is_right_child = right_child_range.contains_in_range(node_value_index_in_inorder)
            if not is_left_child and not is_right_child:
                stack.pop()
                continue
            node = TreeNode(node_value)
            if is_left_child:
                parent_node.left = node
                stack.append((node, 
                             Range(left_child_range.get_range_left(), node_value_index_in_inorder - 1),
                             Range(node_value_index_in_inorder + 1, left_child_range.get_range_right())))
                preorder_index += 1
                continue
            if is_right_child:
                parent_node.right = node
                stack.append((node, 
                             Range(right_child_range.get_range_left(), node_value_index_in_inorder - 1),
                             Range(node_value_index_in_inorder + 1, right_child_range.get_range_right())))
                preorder_index += 1
                continue

        return dummy.left
```

## Code2-3 (Inorder)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None
        if len(preorder) != len(inorder):
            return None

        node_value_to_preorder_index = {}
        for i in range(len(preorder)):
            node_value_to_preorder_index[preorder[i]] = i

        stack = []  # contains all nodes whose .right has not been decided yet
        for node_value in inorder:
            node = TreeNode(node_value)
            preorder_index = node_value_to_preorder_index[node_value]
            node.left = self._gather_decendants(preorder_index, stack, node_value_to_preorder_index)
            stack.append(node)
        return self._gather_decendants(float("-inf"), stack, node_value_to_preorder_index)

    def _gather_decendants(self, preorder_index, stack,node_value_to_preorder_index):
        child = None
        while stack:
            node = stack[-1]
            if node_value_to_preorder_index[node.val] < preorder_index:
                break
            stack.pop()
            node.right = child
            child = node
        return child

```