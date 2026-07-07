# Step1

## アプローチ

* グラフが与えられる。あるノードをルートとした時の高さがhであるとする. 最小のhを与えるルートノードを全て見つけたい.
* ルートを0 ~ n-1まで動かして、それぞれについてBFSで高さを探る
    * 計算量
        * O(N^2)
        * 実行時間: 4 * 10^8 / 10^7 ~= 10 sec
        * C++ならTLEにならずに実行できそう
* 他の解法もないか考えてみたけど思いつかず

## Code1-1 (TLE)

* n=5000の場合で, TLEになった.

```cpp
#include <vector>
#include <unordered_map>


class Solution {
public:
  std::vector<int> findMinHeightTrees(int n, std::vector<std::vector<int>>& edges) {
    std::unordered_map<int, std::vector<int>> node_to_neighbors;
    for (const std::vector<int>& edge: edges) {
      int a = edge[0];
      int b = edge[1];
      node_to_neighbors[a].push_back(b);
      node_to_neighbors[b].push_back(a);
    }

    std::vector<int> min_height_roots;
    int min_height = std::numeric_limits<int>::max();
    for (int root = 0; root < n; root++) {
      int height = ExploreHeight(n, root, node_to_neighbors);
      if (height > min_height) {
        continue;
      }
      if (height == min_height) {
        min_height_roots.push_back(root);
        continue;
      }
      min_height = height;
      min_height_roots = {root};
    }
    return min_height_roots;
    }

private:
  int ExploreHeight(int n, int root, std::unordered_map<int, std::vector<int>>& node_to_neighbors) {
    std::vector<int> nodes{root};
    std::vector<bool> visited(n, false);
    int height = 0;
    while (!nodes.empty()) {
      std::vector<int> next_nodes;
      for (int node : nodes) {
        visited[node] = true;
        for (int neighbor_node : node_to_neighbors[node]) {
          if (visited[neighbor_node]) {
            continue;
          }
          next_nodes.push_back(neighbor_node);
        }
      }
      nodes = std::move(next_nodes);
      height++;
    }
    return height;
  }
};


```

# Step2

## 他の人のPRを見る

* https://github.com/huyfififi/coding-challenges/pull/63
    * > 自力で解けませんでした。C++ で 4 * 10^8 なら TLE にならないだろうと高を括ったところ、 TLE になりました。解法が思いつかず、下記の解法を読んで解きました。難しかったです。
    * 葉となるノードを削除していって、最後に残った一つか二つがmin_heightとなるrootになるらしい
    * あるいは, 最長経路の真ん中の二つという解き方もある


## Code2-2 (remove leaves)

```cpp
#include <set>
#include <unordered_map>
#include <vector>


class Solution {
public:
  std::vector<int> findMinHeightTrees(int n, std::vector<std::vector<int>>& edges) {
    if (n == 1) {
      return {0};
    }
    if (n == 2)  {
      return {0, 1};
    }

    std::unordered_map<int, std::set<int>> node_to_neighbors;
    for (const std::vector<int>& edge : edges) {
      int a = edge[0];
      int b = edge[1];
      node_to_neighbors[a].emplace(b);
      node_to_neighbors[b].emplace(a);
    }

    std::set<int> leaves;
    for (const auto& [node, neighbors] : node_to_neighbors) {
      if (neighbors.size() == 1) {
        leaves.emplace(node);
      }
    }

    while (node_to_neighbors.size() > 2) {
      std::set<int> next_leaves;
      for (int leaf : leaves) {
        int neighbor = *node_to_neighbors[leaf].begin();
        node_to_neighbors.erase(leaf);
        node_to_neighbors[neighbor].erase(leaf);
        if (node_to_neighbors[neighbor].size() == 1) {
          next_leaves.emplace(neighbor);
        }
      }
      leaves = next_leaves;
    }

    return std::vector<int>(leaves.begin(), leaves.end());
    }
};

```

# Step3

## Code3-1

```cpp
#include <unordered_map>
#include <set>
#include <vector>


class Solution {
public:
  std::vector<int> findMinHeightTrees(int n, std::vector<std::vector<int>>& edges) {
    if (n == 1) {
      return {0};
    }
    std::unordered_map<int, std::set<int>> node_to_neighbors;
    for (const std::vector<int>& edge: edges) {
      int a = edge[0];
      int b = edge[1];
      node_to_neighbors[a].emplace(b);
      node_to_neighbors[b].emplace(a);
    }

    std::vector<int> leaves;
    for (int i = 0; i < n; i++) {
      if (node_to_neighbors[i].size() == 1) {
        leaves.push_back(i);
      }
    }

    while (node_to_neighbors.size() > 2) {
      std::vector<int> next_leaves;
      for (int leaf : leaves) {
        int neighbor = *node_to_neighbors[leaf].begin();
        node_to_neighbors.erase(leaf);
        node_to_neighbors[neighbor].erase(leaf);
        if (node_to_neighbors[neighbor].size() == 1) {
          next_leaves.push_back(neighbor);
        }
      }
      leaves = next_leaves;
    }

    return leaves;

    }
};

```
