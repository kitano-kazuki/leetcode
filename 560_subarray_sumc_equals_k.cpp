#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int subarraySum(vector<int> &nums, int k) {
    int n = nums.size();
    int prefix[n];

    prefix[0] = nums[0];

    for (int i = 0; i < n; i++) {
      prefix[i] = prefix[i - 1] + nums[i];
    }

    unordered_map<int, int> mp;
    int ans = 0;

    for (int i = 1; i < n; i++) {
      if (prefix[i] == k) {
        ans++;
      }
      if (mp.find(prefix[i] - k) != mp.end()) {
        ans += mp[prefix[i] - k];
      }

      mp[prefix[i]]++;
    }
    return ans;
  };
};

  int main(int argc, char *argv[]) {

    vector<int> nums;
    int n;
    int k;

    cin >> k;

    while (cin >> n) {
      nums.push_back(n);
    }

    Solution solution;
    int result = solution.subarraySum(nums, k);
    cout << result << endl;
    return 0;
  }
