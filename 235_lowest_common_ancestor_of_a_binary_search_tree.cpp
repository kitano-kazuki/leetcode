#include <cstddef>
#include <vector>

using namespace std;

struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
  TreeNode *lowestCommonAncestor(TreeNode *root, TreeNode *p, TreeNode *q) {
    if (root == NULL || root == p || root == q) return root;
    TreeNode* resLeft = lowestCommonAncestor(root->left, p, q);
    TreeNode* resRight = lowestCommonAncestor(root->right, p, q);
    if (resLeft != NULL && resRight != NULL) return root;
    if (resLeft != NULL) return resLeft;
    return resRight;
  }

};
