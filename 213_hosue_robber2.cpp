#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int rob(vector<int> &nums) {

    if (nums.size() == 1) {
      return nums[0];
    }
    if (nums.size() == 2) {
      return max(nums[0], nums[1]);
    }

    vector<int> dp(nums.size());
    vector<int> dp2(nums.size());

    dp[0] = nums[0];
    dp[1] = nums[0];

    for (int i = 2; i < nums.size() - 1; i++) { // dp[i] = max(nums[i] + dp[i - 2]), dp[i-1])
      dp[i] = max(nums[i] + dp[i-2], dp[i-1]);
      cout << "dp[" << i << "] : " << dp[i] << endl;
    }

    dp2[1] = nums[1];

    for (int i = 2; i < nums.size(); i++) { // dp[i] = max(nums[i] + dp[i - 2]), dp[i-1])
      dp2[i] = max(nums[i] + dp2[i-2], dp2[i-1]);
      cout << "dp2[" << i << "] : " << dp2[i] << endl;
    }

    return max(dp[nums.size() - 2], dp2[nums.size() - 1]);
  }
};
