# Step1

## アプローチ

* ノードとエッジが与えられて, 繋がっている塊の数を返せばいい
    * グラフ理論で言うところの, 森？かな
* Union-Findを使って, エッジごとに更新をしていけば, 各ノードのグループを表す親ノードを得られる
    * エッジの個数 E
    * ノードの個数 N
    * １回のUnionにかかる最悪計算量
        * O(logN)かな. 逆アッカーマンとかあったけど, あまり詳しく覚えていない.
    * 最後に, すべてのノードをみて, 親番号の種類を確認する O(N)
    * トータルで, O(ElogN + N)?
    * step数としては, 5 * 10^3 * 10 + 2 * 10^3 = 10^4くらい
    * 実行時間は, 10^7 step / secで見積もると, 0.001秒くらいか
* DFSやBFSを使って全部見ることもできそう
    * 最初のノードを適当にとって辿る
    * 辿り切ったら, まだ見ていないとこから一個適当にとって同様の手順を繰り返す
    * 全てのノードを見るので, O(N)
    * だけど, まだ見ていないところから一個取るのがO(1)でできる？？
        * visitedとかを使えば結局訪れるのはたかだか1回だからO(N)で良さそう


## Code1-1 (Union Find)

```python
from typing import List


class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.rank = [0] * size
    
    def find(self, idx):
        if self.parents[idx] != idx:
            self.parents[idx] = self.find(self.parents[idx])
        return self.parents[idx]
    
    def union(self, idx1, idx2):
        parent1 = self.find(idx1)
        parent2 = self.find(idx2)
        if parent1 == parent2:
            return
        
        if self.rank[parent1] < self.rank[parent2]:
            self.parents[parent1] = parent2
            return
        elif self.rank[parent2] < self.rank[parent1]:
            self.parents[parent2] = parent1
            return
        else:
            self.parents[parent2] = parent1
            self.rank[parent1] += 1
            return
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        
        num_components = 0
        seen_parents = set()
        for i in range(n):
            parent = uf.find(i)
            if parent in seen_parents:
                continue
            seen_parents.add(parent)
            num_components += 1
        
        return num_components
            
```

## Code1-2 (DFS)

* 繋がっているノードを確認するのにO(N)かかるから計算量の見積もりがアプローチで考えたものと違くなりそう
* 各ノードに対して, 
    * 繋がっているノードを確認 O(N)
* O(N^2)かな
* でも, 繋がっているノードをdictとして持つようにしたら, 繋がっているノードの確認はO(1)でよくなる
    * ただ, 結局すべてのノードが辺で結ばれていたら, 繋がっているノードはN - 1個になるのでO(N^2)は免れないか？？
* いや, 今回の場合は, 一度訪れられたノードに再び行くことはないから, O(N)
* エッジの前処理も含めたらO(N + E)

```python
from typing import List

class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def create_adjacent_matrix():
            adjacent_matrix = [[False] * n for _ in range(n)]
            for edge in edges:
                node1 = edge[0]
                node2 = edge[1]
                adjacent_matrix[node1][node2] = True
                adjacent_matrix[node2][node1] = True
            return adjacent_matrix
        
        def visit_all_connected_nodes(cur_node, adj_matrix, visited):
            if visited[cur_node]:
                return
            visited[cur_node] = True
            for next_node in range(n):
                if cur_node == next_node:
                    continue
                if not adj_matrix[cur_node][next_node]:
                    continue
                visit_all_connected_nodes(next_node, adj_matrix, visited)
            return

        visited = [False] * n
        adj_matrix = create_adjacent_matrix()
        num_components = 0
        for i in range(n):
            if visited[i]:
                continue
            num_components += 1
            visit_all_connected_nodes(i, adj_matrix, visited)
        return num_components

```

# 他の人のコードを確認

* 1 - https://github.com/mamo3gr/arai60/pull/56
    * 言語: Python
    * DFSとUnionFindの両方を実装
    * DFS: DFSでスタックを使用し, 辺は隣接行列ではなくて辞書として用意
    * UnionFind: 実装はほぼ自分のものと一致. 違いとしては`rank`じゃなくて`size`を使用している
* 2 - https://github.com/Hiroto-Iizuka/coding_practice/pull/19
    * 言語: Python
    * 1とほぼ同様
* 3 - https://github.com/TakayaShirai/leetcode_practice/pull/19
    * 言語: Swift
    * 手作業の様子を考えているのがいいと思った
    * 実行時間が図られているのも良い
    * 1, 2と同様
* 4 - https://github.com/xbam326/leetcode/pull/21
    * 言語: Python
    * 1, 2, 3と同様
* 5 - https://github.com/dxxsxsxkx/leetcode/pull/19
    * 言語: C++
    * 辞書ではなく, 二次元配列で辺のつながりを表現. adjacency_list[i] = (nodeiにつながるノードのリスト)
    * あとは1,2,3,4と同様

# 調べたこと

* UnionFindの計算量
    * 最適化なしだったら, O(N)
    * rankやsizeによって木の高さを制限したら, O(logN)
    * Path Compression + rankにしたら, O(α(N))で, これはほぼ定数時間と見ていい


# Step2

## Code2-1 (DFS)

* 再帰をスタックで行うようにした
* 辞書として辺を登録した

```python
from typing import List
from collections import defaultdict

class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        node_to_neighbors = defaultdict(set)
        for edge in edges:
            node_to_neighbors[edge[0]].add(edge[1])
            node_to_neighbors[edge[1]].add(edge[0])

        visited = [False] * n

        def visit_connected_nodes(init_node):
            frontier = [init_node]
            while frontier:
                node = frontier.pop()
                if visited[node]:
                    continue
                visited[node] = True
                for neighbor_node in node_to_neighbors[node]:
                    if not visited[neighbor_node]:
                        frontier.append(neighbor_node)
            return

        num_components = 0
        for i in range(n):
            if visited[i]:
                continue
            num_components += 1
            visit_connected_nodes(i)
        return num_components

```

## Code2-2 (Union Find)

```python
from typing import List


class UnionFind:
    def __init__(self, size):
        self.parents = [i for i in range(size)]
        self.rank = [0] * size
    
    def find(self, idx):
        if self.parents[idx] != idx:
            self.parents[idx] = self.find(self.parents[idx])
        return self.parents[idx]
    
    def union(self, idx1, idx2):
        parent1 = self.find(idx1)
        parent2 = self.find(idx2)
        if parent1 == parent2:
            return
        
        if self.rank[parent1] < self.rank[parent2]:
            self.parents[parent1] = parent2
            return
        elif self.rank[parent2] < self.rank[parent1]:
            self.parents[parent2] = parent1
            return
        else:
            self.parents[parent2] = parent1
            self.rank[parent1] += 1
            return
        

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        for edge in edges:
            uf.union(edge[0], edge[1])
        
        num_components = 0
        seen_parents = set()
        for i in range(n):
            parent = uf.find(i)
            if parent in seen_parents:
                continue
            seen_parents.add(parent)
            num_components += 1
        
        return num_components

``` 