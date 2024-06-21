#include <cstdio>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  void combination(vector<int> &candidate, int target, vector<int> &curComb, int curIdx, int curSum ,vector<vector<int>> &ans){
    if (curSum == target){
      ans.push_back(curComb);
      return;
    } else if (curSum > target){
      return;
    }

    for (int i = curIdx; i < candidate.size(); i++){
      curComb.push_back(candidate[i]);
      curSum += candidate[i];
      combination(candidate, target, curComb, i, curSum, ans);
      curSum -= candidate[i];
      curComb.pop_back();
    }
    

  }
  vector<vector<int>> combinationSum(vector<int> &candidates, int target) {
    vector<vector<int>> ans;
    vector<int> curComb;
    combination(candidates, target, curComb, 0, 0, ans);
    return ans;
  }
};

int main(int argc, char *argv[]) {
  int target;
  vector<int> candidates;

  cin >> target;

  int n;
  while (cin >> n) {
    candidates.push_back(n);
  }

  Solution solution;

  vector<vector<int>> result = solution.combinationSum(candidates, target);

  for (int i = 0; i < result.size(); i++){
    cout << "combination: " << i << endl;
    for (int j = 0; j < result[i].size(); j++){
      cout << result[i][j] << ",";
    }
    cout << endl;
  }

  return 0;
}
