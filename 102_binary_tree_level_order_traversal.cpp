
#include <map>
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

#include <algorithm>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>

using namespace std;
class Solution {
public:
  vector<vector<int>> levelOrder(TreeNode *root) {
    queue<TreeNode *> q;
    map<TreeNode *, int> m;

    if (root == nullptr) {
      return vector<vector<int>>();
    }

    q.push(root);
    m[root] = 1;


    while (!q.empty()) {
      root = q.front();
      q.pop();
      TreeNode *left = root->left;
      if (left != nullptr) {
        q.push(left);
        m[left] = m[root] + 1;

      }
      TreeNode *right = root->right;
      if (right != nullptr) {
        q.push(right);
        m[right] = m[root] + 1;
      }
    }
    int maxM = 0;
    for(auto item : m){
      if (item.second > maxM){
        maxM = item.second;
      }
    }
    vector<vector<int>> ans(maxM, vector<int>());
    for (auto item : m) {
      int idx = item.second - 1;
      ans[idx].push_back(item.first->val);
    }
    return ans;
  }
};
