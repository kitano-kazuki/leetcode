# Step1

## アプローチ

* 問題の理解
    * 横に無限に続く広大な土地がある.
    * 障害物を置く(query 1)ことができる
    * 特定のサイズの棒が, 0~xにおけるかを知ることができる(query 2)
* 手作業でやるなら, queryごとに
    * 0を起点に棒をおけるか
    * 1を起点に...
    * のように確かめる
* あるいは分割された区間を保存しておく？？
* ヒント1を見る
     * `d[x]`がxの次のobstacleまでの距離
     * あるx以降におけるかどうかはわかる
     * おけなかったら`d[d[x]]`を見ればいいのか
     * でもだとしても、クエリの個数（置かれている障害物の個数）分の処理は必要
     * 1クエリあたりの処理時間は
        * 15 * 10^4 / 10^6 ~= 10^-2 sec
    * クエリは全部で15 * 10^4くる可能性がある
* ヒント2, 3をみる
    * segment treeを使うらしい
    * d[0], d[1] ... d[x - sz]までの最大値が欲しいからか
* 18:16. ヒントを結局全部見てしまったけど、方針は把握した

## Code1-1 (WA: TLE)

* 更新をするたびに`0..p`をすべて書き換えているので, TLEになった
* 1:37:19

```python
import dataclasses

MAXIMUM_X = 5 * 10**4


@dataclasses.dataclass
class Node:
    begin: int = -1
    end: int = -1
    value: int = -1

# d[i]: 座標i以降に出現する最初の障害物までの距離
# dの区間最大値を取得するSeg木
class SegmentTree:
    def __init__(self, n):
        self.n = n
        # nodes[i](1-index-based)に対して
        # 親: nodes[i // 2]
        # 左子: nodes[i * 2]
        # 右子: nodes[i * 2 + 1]
        self.nodes = [None] * 4 * n
        self._init_nodes(1, 0, n)

    def _init_nodes(self, node_i: int, begin: int, end: int) -> None:
        self.nodes[node_i] = Node(begin, end, self.n + 1)
        if end - begin == 1:
            return
        mid = (begin + end) // 2
        self._init_nodes(node_i * 2, begin, mid)
        self._init_nodes(node_i * 2 + 1, mid, end)
        return

    def _intersection_range(self, begin1: int, end1: int, begin2: int, end2: int) -> tuple[int, int] | None:
        if end1 <= begin2 or end2 <= begin1:
            return None
        return max(begin1, begin2), min(end1, end2)

    # 座標pの障害物でnodesを更新
    def _update(self, node_i: int, p: int, begin: int, end: int):
        node = self.nodes[node_i]

        if node.end - node.begin == 1:
            node.value = min(node.value, p - node.begin)
            return
        
        mid_in_node = (node.begin + node.end) // 2
        query_left = self._intersection_range(node.begin, mid_in_node, begin, end)
        query_right = self._intersection_range(mid_in_node, node.end, begin, end)

        assert query_left is not None or query_right is not None

        left_max = float("-inf")
        if query_left is not None:
            self._update(node_i * 2, p, query_left[0], query_left[1])
        right_max = float("-inf")
        if query_right is not None:
            self._update(node_i * 2 + 1, p, query_right[0], query_right[1])

        node.value = max(
            self.nodes[node_i * 2].value,
            self.nodes[node_i * 2 + 1].value,
            
        )

        return

    def place(self, p: int):
        self._update(1, p, 0, p)

    def _query(self, node_i: int, begin: int, end: int) -> int:
        node = self.nodes[node_i]

        if begin == node.begin and end == node.end:
            return node.value
        
        mid_in_node = (node.begin + node.end) // 2
        query_left = self._intersection_range(node.begin, mid_in_node, begin, end)
        query_right = self._intersection_range(mid_in_node, node.end, begin, end)

        assert query_left is not None or query_right is not None

        left_max = float("-inf")
        if query_left is not None:
            left_max = self._query(node_i * 2, query_left[0], query_left[1])
        right_max = float("-inf")
        if query_right is not None:
            right_max = self._query(node_i * 2 + 1, query_right[0], query_right[1])

        return max(left_max, right_max)

    def query(self, begin: int, end: int) -> int:
        return self._query(1, begin, end)


class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        segment_tree = SegmentTree(MAXIMUM_X + 1)
        result = []
        for query in queries:
            if query[0] == 1:
                segment_tree.place(query[1])
            else:
                x = query[1]
                size = query[2]
                if x < size:
                    result.append(False)
                    continue
                max_distance = segment_tree.query(0, x - size + 1)
                result.append(max_distance >= size)
        return result

```

## Code1-2

```python
```



# Step2

## Code2-1

# Step3

## Code3-1
