#include <cstddef>
#include <optional>
#include <utility>
#include <vector>
#include <iostream>

using namespace std;
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  // NOTE: Cannot do it with simple recursive(must have add comparison with
  // previous values)

  // std::optional<std::pair<int, int>> isValidBSTInner(TreeNode *root) {
  //   if (root->left == nullptr && root->right == nullptr) {
  //     return std::pair<int, int>(root->val, root->val);
  //   }
  //   if (root->left == nullptr) {
  //     if (root->val < root->right->val) {
  //       auto res = isValidBSTInner(root->right);
  //       return std::pair<int, int>(root->val, res.value().second);
  //     }
  //     return std::nullopt;
  //   }
  //   if (root->right == nullptr) {
  //     if (root->left->val < root->val) {
  //       auto res = isValidBSTInner(root->left);
  //       return std::pair<int, int>(res.value().first, root->val);
  //     }
  //     return {};
  //   }
  //   if (root->left->val < root->val && root->val < root->right->val) {
  //     auto res1 = isValidBSTInner(root->left);
  //     auto res2 = isValidBSTInner(root->right);
  //     if (res2.value().first < res1.value().second) {
  //       return {};
  //     }
  //     return std::pair<int, int>(res1.value().first, res2.value().second);
  //   }
  //   return {};
  // }
  //
  // bool isValidBST(TreeNode *root) {
  //   auto res = isValidBSTInner(root);
  //   if (res.has_value()) {
  //     return true;
  //   }
  //   return false;
  // }
  //
  //

  bool isInorder(vector<int>& list){
    int prev = list[0];
    for(int i = 1; i < list.size(); i++){
      if(prev < list[i]){
        prev = list[i];
        continue;
      }
      return false;
    }
    return true;
  }

  bool isValidBST(TreeNode *root) {
    vector<int> list;
    std::vector<TreeNode *> stack;
    while (root != nullptr || !stack.empty()) {
      while (root != nullptr) {
        stack.push_back(root);
        root = root->left;
      }
      root = stack.back();
      stack.pop_back();
      list.push_back(root->val);
      root = root->right;
    }

    return isInorder(list);
    
  }
};
