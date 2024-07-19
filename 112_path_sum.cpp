struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

#include <vector>

using namespace std;

class Solution {
public:
  bool hasPathSum(TreeNode *root, int targetSum) {
    if (root == nullptr){
      return false;
    }
    int val = root->val;
    int nextTargetSum = targetSum - val;
    if (nextTargetSum == 0 && root->left == nullptr && root->right == nullptr){
      return true;
    }
    return hasPathSum(root->left, nextTargetSum) || hasPathSum(root->right, nextTargetSum);
  }
};
