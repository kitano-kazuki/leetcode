
#include <queue>
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int maxDepth(TreeNode *root) {
    if (root == nullptr) {
      return 0;
    }

    int depth = 0;
    queue<TreeNode *> q;
    q.push(root);

    while (!q.empty()) {
      int n = q.size();
      for (int i = 0; i < n; i++) {
        root = q.front();
        q.pop();
        if (root->left != nullptr)
          q.push(root->left);
        if (root->right != nullptr)
          q.push(root->right);
      }
      depth++;
    }
    return depth;
  }
};
