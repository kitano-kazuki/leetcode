#include <cstdlib>
#include <iterator>
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
  TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) {
    if(preorder.empty()){
      return nullptr;
    }
    int v = preorder[0];
    TreeNode* root = new TreeNode(v);
    int j = 0;
    for(; j < inorder.size(); j++){
      if(inorder[j] == v){
        break; 
      }
    }
    vector<int> a1;
    copy(preorder.begin() + 1, preorder.begin() + j + 1, back_inserter(a1));
    vector<int> a2;
    copy(inorder.begin(), inorder.begin() + j, back_inserter(a2));
    vector<int> b1;
    copy(preorder.begin() + j + 1, preorder.end(), back_inserter(b1));
    vector<int> b2;
    copy(inorder.begin() + j + 1, inorder.end(), back_inserter(b2));
    root->left = buildTree(a1, a2);
    root->right = buildTree(b1, b2);
    return root;
  }
};
