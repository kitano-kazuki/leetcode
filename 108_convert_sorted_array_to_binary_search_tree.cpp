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
  TreeNode *constructTree(vector<int> &nums, int start, int end) {
    if (start == end) {
      TreeNode *root = new TreeNode(nums[start]);
      return root;
    }
    if (start == end - 1) {
      TreeNode *root = new TreeNode(nums[end]);
      TreeNode *left = new TreeNode(nums[start]);
      root->left = left;
      return root;
    }
    int mid = (start + end) / 2;
    TreeNode *root = new TreeNode(nums[mid]);
    root->left = constructTree(nums, start, mid - 1);
    root->right = constructTree(nums, mid + 1, end);
    return root;
  }
  TreeNode *sortedArrayToBST(vector<int> &nums) {
    TreeNode* root = constructTree(nums, 0, nums.size() - 1);
    return root;
  }
};
