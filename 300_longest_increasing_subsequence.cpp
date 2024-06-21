#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 1);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < i; ++j)
                if (nums[i] > nums[j] && dp[i] < dp[j] + 1)
                    dp[i] = dp[j] + 1;
        return *max_element(dp.begin(), dp.end());
    }
};

int main(int argc, char *argv[]) {

  vector<int> nums;
  int n;
  while (cin >> n) {
    nums.push_back(n);
  }

  Solution solution;
  int result = solution.lengthOfLIS(nums);
  cout << result << endl;
  return 0;
}
