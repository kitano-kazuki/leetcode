# Step1

## アプローチ

* あるノードへのreferenceが与えられた時に, そのグラフのdeep copyを行う
* シフト制でやることを考える
    * 渡されたノードをコピ-する
    * 渡されたノードに隣接するノードをコピーするように部下に指示する
    * もし, 隣接するノードがすでにコピーされていたら, それを再利用してしまう（指示は出さない）
* O(NE)
    * Nはノード数
    * Eはノードから出ているエッジの数の平均
    * Eは最大でN-1なので
    * O(N^2)としていい
    * 実行時間は, 10^4 / 10^6 ~= 10^-2 sec程度
* ここまで7:00

## Code1-1

* AC: 4:59

```python
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        val_to_cloned_node = {}
        def clone_graph_helper(node: Node) -> Node:
            if node.val in val_to_cloned_node:
                return val_to_cloned_node[node.val]
            
            cloned_node = Node(node.val)
            val_to_cloned_node[node.val] = cloned_node
            for adjacent_node in node.neighbors:
                copied_adjacent_node = clone_graph_helper(adjacent_node)
                cloned_node.neighbors.append(copied_adjacent_node)
            
            return cloned_node
        
        return clone_graph_helper(node)
        
```

# Step2

## Code2-1

* 変更なし

```python
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        val_to_cloned_node = {}
        def clone_graph_helper(node: Node) -> Node:
            if node.val in val_to_cloned_node:
                return val_to_cloned_node[node.val]
            
            cloned_node = Node(node.val)
            val_to_cloned_node[node.val] = cloned_node
            for adjacent_node in node.neighbors:
                copied_adjacent_node = clone_graph_helper(adjacent_node)
                cloned_node.neighbors.append(copied_adjacent_node)
            
            return cloned_node
        
        return clone_graph_helper(node)
        
```

## 他の人のPRを見る

* https://github.com/tom4649/Coding/pull/65
* https://github.com/huyfififi/coding-challenges/pull/32
    * iterativeでloopを使って解く方法も行っている

## Code2-2 (iterative)

```python
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        node_to_copied = {node: Node(node.val)}
        neighbor_unresolved = [node]

        while neighbor_unresolved:
            unresolved = neighbor_unresolved.pop()
            unresolved_copy = node_to_copied[unresolved]
            for neighbor in unresolved.neighbors:
                if neighbor in node_to_copied:
                    copied_neighbor = node_to_copied[neighbor]
                    unresolved_copy.neighbors.append(copied_neighbor)
                    continue
                copied_neighbor = Node(neighbor.val)
                unresolved_copy.neighbors.append(copied_neighbor)
                node_to_copied[neighbor] = copied_neighbor
                neighbor_unresolved.append(neighbor)
        
        return node_to_copied[node]
        
```

# Step3

## Code3-2 (iterative)

```python
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        original_to_copied = {node: Node(node.val)}
        neighbor_unresolved = [node]

        while neighbor_unresolved:
            original = neighbor_unresolved.pop()
            copied = original_to_copied[original]
            for neighbor_original in original.neighbors:
                if neighbor_original not in original_to_copied:
                    original_to_copied[neighbor_original] = Node(neighbor_original.val)
                    neighbor_unresolved.append(neighbor_original)
                copied.neighbors.append(original_to_copied[neighbor_original])
        
        return original_to_copied[node]
   
```