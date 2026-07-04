# Step1

## アプローチ

* 上から順番に右から見た時に見えるものを知りたい.
* 右側の子だけ見ればいいかと思ったが, 右側の子がいない時は左側の子が採用される.
* レベルごとにBFSをして, 一番右のものを知るのが良さそう.

## Code1-1

```cpp
#include <vector>
#include <utility>

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
  std::vector<int> rightSideView(TreeNode* root) {
    if (root == nullptr){
      return std::vector<int>();
    }

    std::vector<int> most_right_values;

    std::vector<TreeNode*> nodes;
    nodes.push_back(root);

    while (!nodes.empty()){
      most_right_values.push_back(nodes.back()->val);
      std::vector<TreeNode*> next_nodes;
      for (const TreeNode* node : nodes){
        if (node->left != nullptr){
          next_nodes.push_back(node->left);
        }
        if (node->right != nullptr){
          next_nodes.push_back(node->right);
        }
      }
      nodes = std::move(next_nodes);
    }

    return most_right_values;

    }
};


```

# Step2

## Code2-1

*  変更なし

```cpp


#include <vector>
#include <utility>

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
  std::vector<int> rightSideView(TreeNode* root) {
    if (root == nullptr){
      return std::vector<int>();
    }

    std::vector<int> most_right_values;

    std::vector<TreeNode*> nodes;
    nodes.push_back(root);

    while (!nodes.empty()){
      most_right_values.push_back(nodes.back()->val);
      std::vector<TreeNode*> next_nodes;
      for (const TreeNode* node : nodes){
        if (node->left != nullptr){
          next_nodes.push_back(node->left);
        }
        if (node->right != nullptr){
          next_nodes.push_back(node->right);
        }
      }
      nodes = std::move(next_nodes);
    }

    return most_right_values;

    }
};


```

## 他の人のPRを見る

* https://github.com/huyfififi/coding-challenges/pull/55
    * 方針は一緒.

# Step3

## Code3-1

```cpp


#include <vector>
#include <utility>

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
  std::vector<int> rightSideView(TreeNode* root) {
    if (root == nullptr){
      return std::vector<int>{};
    }

    std::vector<int> rightmost_values;
    std::vector<TreeNode*> nodes{root};

    while (!nodes.empty()){
      rightmost_values.push_back(nodes.back()->val);
      std::vector<TreeNode*> next_nodes;
      for (const TreeNode* node : nodes){
        if (node->left != nullptr){
          next_nodes.push_back(node->left);
        }
        if (node->right != nullptr){
          next_nodes.push_back(node->right);
        }
      }
      nodes = std::move(next_nodes);
    }
    return rightmost_values;
  }
};

```
