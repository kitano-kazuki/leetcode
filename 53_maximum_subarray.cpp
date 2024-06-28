#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int maxSubArray(vector<int> &nums) {
    int size = nums.size();
    vector<int> dp(size);
    dp[0] = nums[0];
    for (int i = 1; i < size; i++) {
      dp[i] = max(dp[i - 1] + nums[i], nums[i]);
    }
    return *max_element(dp.begin(), dp.end());
  }
};

int main(int argc, char *argv[]) {
  vector<int> nums{-2, 1, -3, 4, -1, 2, 1, -5, 4};
  Solution solution;
  int res = solution.maxSubArray(nums);
  cout << res << endl;
  return 0;
}
