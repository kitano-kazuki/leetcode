#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    void addPattern(vector<int> &nums, int idx,  vector<vector<int>> &ans){
      if (idx == nums.size()){
        return;
      }

      vector<vector<int>> refAns = ans;
      ans.clear();
      int numInsert = nums[idx];
      for (vector<int> pattern : refAns){
          for(int i = 0; i <= pattern.size(); i++){
          auto copy = pattern;
            auto insertPos = copy.begin() + i;
            copy.insert(insertPos, numInsert);
            ans.push_back(copy);
          }
      }

      return addPattern(nums, idx + 1, ans);
    }

    vector<vector<int>> permute(vector<int>& nums) {
      vector<vector<int>> ans = {{nums[0]}};
      addPattern(nums, 1, ans);
      return ans;
        
    }
};

int main (int argc, char *argv[]) {
  vector<int> nums;
  int n;
  while(cin >> n)  {
    nums.push_back(n);
  }

  Solution solution;
  vector<vector<int>> result = solution.permute(nums);
  for (int i = 0; i < result.size(); i++){
    cout << "[";
    for (int j = 0; j < result[i].size(); j++){
      cout << result[i][j] << ",";
    }
    cout << "],";
  }
  return 0;
}
