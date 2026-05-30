# Step1

## アプローチ

* 重みつき有向グラフ`graph`が与えられる
* `src1`, `src2`, `target`が与えられる
* `src1`からも`src2`からも`target`に到達可能である`graph`のサブグラフのうちで重みの合計値が最小となるものを出力したい. そのようなものが存在しない場合は-1
* ネットワークの配線工事みたいなイメージかな？？ あるいは道路の建設
* `src1`から`target`に行く最小のパスと`src2`から`target`に行く最小のパスを両方含むサブグラフを考えるだけでは, 最適とは言えない

---

```
A
|\
C-D
```
エッジが以下のようになっていて, `src1: A`, `src2: C`, `target: D`を考える
* A - C : 1  
* A - D : 3  
* C - D : 3  

AからDに至る最短と, CからDに至る最短からできるサブグラフの重みの合計は, 6

AからDに行く場合は, Cを経由するようにすると, 4

---

* `src1`から`src2`に行く道が短いなら`src1`から`target`に向かうより安上がり？
* でも, その場合でも`src1`から`target`または`src2`から`target`の道は絶対必要
* 駅(=target), 家1(src1), 家2(src2)を考える
    * 家1が駅のすぐ南, 家2が駅のすぐ北にあるなら, それぞれの家から道を引きたい
    * 家1が駅近で, 家2が駅から徒歩15分なら, 家2から家1までの道を引いてもいいし, 家2から直接に駅まで道を引いてもいい
        * マップ上での家の位置に依存しそう
* つまり, ダイクストラを3回やる
    * src1 -> target
    * src2 -> target
    * src1 -> src2
* ダイクストラを考える
    * 未探索集合の中から, コストが一番低いものを取り出す
    * そこからつながっているエッジ分のコストを更新する
    * O(VE)??
        * Vは頂点, Eはエッジの数
    * 今回の問題の制約だとO(N^2)になる？？
        * 10^10 / 10^6 ~= 10^4 secかかりそう
    * ダイクストラをもう少し効率的にやりたいし, そのような方法があったはず
    * 思いつかないので一旦TLEしそうだけど実装して, Step2で詳細を考えよう
* ここまで27:42


## Code1-1-1 (1度目の提出WA)

* 44:01
* src1からtargetに至る道中で, src2からtargetに至る道に合流する場合を捉えられていない


```python
import heapq
import dataclasses


@dataclasses.dataclass
class Edge:
    src: int
    dest: int
    weight: int


class Solution:
    def min_cost_from_src_to_target(self, src: int, target: int, node_to_edges: dict[int, list[Edge]], num_nodes: int) -> int:
        if src == target:
            return 0
        
        # src-node間コストを保存
        node_to_cost = {}
        cost_and_node = []
        for node in range(num_nodes):
            if node == src:
                node_to_cost[src] = 0
                heapq.heappush(cost_and_node, (0, src))
            else:
                node_to_cost[node] = float("inf")
                heapq.heappush(cost_and_node, (float("inf"), node))

        visited = set()

        while len(visited) < num_nodes:
            cost, node = heapq.heappop(cost_and_node)
            if node in visited:
                continue
            visited.add(node)
            for edge in node_to_edges[node]:
                cost_dest = cost + edge.weight
                if cost_dest < node_to_cost[edge.dest]:
                    node_to_cost[edge.dest] = cost_dest
                    heapq.heappush(cost_and_node, (cost_dest, edge.dest))
        
        return node_to_cost[target]

    def construct_node_to_edges(self, edges: list[list[int]], num_nodes: int) -> dict[int, list[Edge]]:
        node_to_edges = {node : [] for node in range(num_nodes)}
        for src, dest, weight in edges:
            node_to_edges[src].append(Edge(src, dest, weight))
        return node_to_edges


    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

        node_to_edges = self.construct_node_to_edges(edges, n)

        cost_src1_dest = self.min_cost_from_src_to_target(src1, dest, node_to_edges, n)
        cost_src2_dest = self.min_cost_from_src_to_target(src2, dest, node_to_edges, n)
        cost_src1_src2 = self.min_cost_from_src_to_target(src1, src2, node_to_edges, n)
        cost_src2_src1 = self.min_cost_from_src_to_target(src2, src1, node_to_edges, n)


        min_weight = min(
            cost_src1_dest + cost_src2_dest, 
            cost_src1_src2 + cost_src2_dest,
            cost_src2_src1 + cost_src1_dest)
        
        if min_weight == float("inf"):
            return -1
        return min_weight
        
```

## Code1-1-2 (２度目の提出WA)

* さらに, 11:40
* 中間ノードのすべての場合を試したがTLEになってしまった

```python
import heapq
import dataclasses


@dataclasses.dataclass
class Edge:
    src: int
    dest: int
    weight: int


class Solution:
    def min_cost_from_src_to_target(self, src: int, target: int, node_to_edges: dict[int, list[Edge]], num_nodes: int) -> int:
        
        # src-node間コストを保存
        node_to_cost = {}
        cost_and_node = []
        for node in range(num_nodes):
            if node == src:
                node_to_cost[src] = 0
                heapq.heappush(cost_and_node, (0, src))
            else:
                node_to_cost[node] = float("inf")
                heapq.heappush(cost_and_node, (float("inf"), node))

        if src == target:
            return node_to_cost

        visited = set()

        while len(visited) < num_nodes:
            cost, node = heapq.heappop(cost_and_node)
            if node in visited:
                continue
            visited.add(node)
            for edge in node_to_edges[node]:
                cost_dest = cost + edge.weight
                if cost_dest < node_to_cost[edge.dest]:
                    node_to_cost[edge.dest] = cost_dest
                    heapq.heappush(cost_and_node, (cost_dest, edge.dest))
        
        return node_to_cost

    def construct_node_to_edges(self, edges: list[list[int]], num_nodes: int) -> dict[int, list[Edge]]:
        node_to_edges = {node : [] for node in range(num_nodes)}
        for src, dest, weight in edges:
            for i, edge in enumerate(node_to_edges[src]):
                node_to_edges[src].append(Edge(src, dest, weight))
        return node_to_edges


    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

        node_to_edges = self.construct_node_to_edges(edges, n)

        min_weight = float("inf")
        node_to_cost1 = self.min_cost_from_src_to_target(src1, dest,node_to_edges, n)
        node_to_cost2 = self.min_cost_from_src_to_target(src2, dest, node_to_edges, n)

        min_weight = float("inf")
        for mid in range(n):
            node_to_cost3 = self.min_cost_from_src_to_target(mid, dest, node_to_edges, n)
            weight = node_to_cost1[mid] + node_to_cost2[mid] + node_to_cost3[dest]
            min_weight = min(min_weight, weight)

        if min_weight == float("inf"):
            return -1
        return min_weight
        
```
# Step2

## leetcodeの解法を見る

* 解き方の大まかな方針（ダイクストラを３回）は同じ
* `mid`ノードから`dest`までをdijkstraするのではなく, `dest`から`mid`までをdijkstraすると, 全体のdijkstraの回数を3回にすることができる

## Code2-1

* 上記の変更を加えてやっとAC

```python
import heapq
import dataclasses


@dataclasses.dataclass
class Edge:
    src: int
    dest: int
    weight: int


class Solution:
    def min_cost_from_src(self, src: int, node_to_edges: dict[int, list[Edge]], num_nodes: int) -> int:
        
        # src-node間コストを保存
        node_to_cost = {}
        cost_and_node = []
        for node in range(num_nodes):
            if node == src:
                node_to_cost[src] = 0
                heapq.heappush(cost_and_node, (0, src))
            else:
                node_to_cost[node] = float("inf")
                heapq.heappush(cost_and_node, (float("inf"), node))

        visited = set()

        while len(visited) < num_nodes:
            cost, node = heapq.heappop(cost_and_node)
            if node in visited:
                continue
            visited.add(node)
            for edge in node_to_edges[node]:
                cost_dest = cost + edge.weight
                if cost_dest < node_to_cost[edge.dest]:
                    node_to_cost[edge.dest] = cost_dest
                    heapq.heappush(cost_and_node, (cost_dest, edge.dest))
        
        return node_to_cost

    def construct_node_to_edges(self, edges: list[list[int]], num_nodes: int) -> dict[int, list[Edge]]:
        node_to_edges = {node : [] for node in range(num_nodes)}
        for src, dest, weight in edges:
            node_to_edges[src].append(Edge(src, dest, weight))
        return node_to_edges


    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

        node_to_edges = self.construct_node_to_edges(edges, n)
        node_to_cost1 = self.min_cost_from_src(src1, node_to_edges, n)
        node_to_cost2 = self.min_cost_from_src(src2, node_to_edges, n)

        reversed_edges = [[d, s, w] for s, d, w in edges]
        reversed_node_to_edges = self.construct_node_to_edges(reversed_edges, n)
        node_to_cost3 = self.min_cost_from_src(dest, reversed_node_to_edges, n)

        min_weight = float("inf")
        for mid in range(n):
            min_weight = min(
                min_weight,
                node_to_cost1[mid] + node_to_cost2[mid] + node_to_cost3[mid]
            )

        if min_weight == float("inf"):
            return -1
        return min_weight
        
```

# Step3

## Code3-1

* 1st: 19:51
* 2nd: 7:32
* 3rd: 5:01

```python
import heapq


class Solution:
    def _construct_edge_matrix(self, edges: list[list[int]], n: int) -> list[list[int]]:
        edge_matrix = [[] for _ in range(n)]
        for s, d, w in edges:
            edge_matrix[s].append((d, w))
        return edge_matrix

    def _min_cost_map(self, src: int, edge_matrix: list[list[int]], n: int) -> dict[int, int]:
        cost_map = {i: float("inf") for i in range(n)}
        cost_map[src] = 0
        cost_and_node = [(0, src)]
        visited = [False] * n
        while cost_and_node:
            cost, node = heapq.heappop(cost_and_node)
            if visited[node]:
                continue
            visited[node] = True
            for dest, weight in edge_matrix[node]:
                if cost + weight > cost_map[dest]:
                    continue
                cost_map[dest] = cost + weight
                heapq.heappush(cost_and_node, (cost + weight, dest))
        return cost_map

    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        edge_matrix = self._construct_edge_matrix(edges, n)
        cost_map1 = self._min_cost_map(src1, edge_matrix, n)
        cost_map2 = self._min_cost_map(src2, edge_matrix, n)

        r_edges = [[d, s, w] for s, d, w in edges]
        r_edge_matrix = self._construct_edge_matrix(r_edges, n)
        cost_map_dest = self._min_cost_map(dest, r_edge_matrix, n)

        min_weight = float("inf")
        for mid in range(n):
            min_weight = min(
                min_weight,
                cost_map1[mid] + cost_map2[mid] + cost_map_dest[mid]
            )
        
        if min_weight == float("inf"):
            return -1
        return min_weight

```
