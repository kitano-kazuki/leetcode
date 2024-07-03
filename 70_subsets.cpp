#include <iterator>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
  vector<vector<int>> prependAll(vector<vector<int>> set, int value) {
    for (vector<int> &pattern : set) {
      pattern.insert(pattern.begin(), value);
    }
    return set;
  }

  vector<vector<int>> calcSubsets(vector<int> &nums, int index) {
    if(index == nums.size() - 1){
      vector<vector<int>> res;
      vector<int> pattern;
      vector<int> empty;
      pattern.push_back(nums[index]);
      res.push_back(pattern);
      res.push_back(empty);
      return res;
    }
    vector<vector<int>> subsets1 = calcSubsets(nums, index + 1);
    vector<vector<int>> subsets2 = prependAll(subsets1, nums[index]);
    vector<vector<int>> result(subsets1);
    result.insert(result.end(), subsets2.begin(), subsets2.end());
    return result;
  }

  vector<vector<int>> subsets(vector<int> &nums) {
    return calcSubsets(nums, 0);
  }
};

int main (int argc, char *argv[]) {
  vector<int> nums = {1, 2, 3};
  Solution solution;
  auto res = solution.subsets(nums);
  return 0;
}
