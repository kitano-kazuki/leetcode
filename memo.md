# Step1

## アプローチ

* 二分探索木が与えられる. `k`番目に小さい数を返す.
* in-orderで操作した順番が小さい順の順番になる.
* loopでも再帰でも解けるが, 最初は考えやすい再帰で実装する.

## Code1-1 (Recursion)

```cpp
#include <functional>
#include <vector>


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
      std::vector<int> nums;

      std::function<void(TreeNode*)> AppendNodesInOrder = [&](TreeNode* node) -> void {
        if (node->left != nullptr) {
          AppendNodesInOrder(node->left);
        }
        nums.push_back(node->val);
        if (node->right != nullptr) {
          AppendNodesInOrder(node->right);
        }
      };

      AppendNodesInOrder(root);
      return nums[k - 1];
    };
};

```

# Step2

## Code2-2 (Iterative)

* ループでも実装してみる.


```cpp
#include <stack>
#include <vector>


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
      NodeInformation root_information(root, State::Unvisited);
      std::stack<NodeInformation> node_infos({root_information});
      int order = 0;
      while (!node_infos.empty()) {
        NodeInformation node_information = node_infos.top();
        node_infos.pop();
        TreeNode* node = node_information._node;
        State state = node_information._state;
        if (state == State::Unvisited) {
          node_infos.push(NodeInformation(node, State::Visited));
          if (node->left != nullptr) {
            node_infos.push(NodeInformation(node->left, State::Unvisited));
          }
        } else if (state == State::Visited) {
          order++;
          if (order == k) {
            return node->val;
          }
          if (node->right != nullptr) {
            node_infos.push(NodeInformation(node->right, State::Unvisited));
          }
        }
      }

      return -1;
    };

private:
    enum class State {
      Unvisited,
      Visited
    };

    struct NodeInformation {
      public:
        NodeInformation(TreeNode* node, State state) : _node(node), _state(state) {};

        TreeNode* _node;
        State _state;
    };
};

```

# Step3

## Code3-1 (Recursion)

```cpp
#include <functional>
#include <vector>


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
      std::vector<int> nums;
      std::function<void(TreeNode*)> AppendNodesInOrder = [&](TreeNode* node) -> void {
        if (node->left != nullptr) {
          AppendNodesInOrder(node->left);
        }
        nums.push_back(node->val);
        if (node->right != nullptr) {
          AppendNodesInOrder(node->right);
        }
      };
      AppendNodesInOrder(root);
      return nums[k - 1];
    };

};

```
