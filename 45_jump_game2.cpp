#include <cstdint>
#include <vector>

// NOTE: 貪欲法が早いらしい
// できるだけ遠くにいけるにはどうしたらいいか
// → n回のjumpで行ける範囲の最大値を調べる。n-1回目のjumpで行ける範囲の上限に到達したらn回目のjumpを初めて先程の上限値までいく

using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
      int n = nums.size();
      vector<int> dp(n, INT32_MAX);
      dp[0] = 0;
      for(int i = 0; i < n; i++){
        for(int j = 0; j < nums[i]; j++){
          if(i + j + 1 > n - 1) {
            break;
          }
          dp[i + j + 1] = min(dp[i] + 1, dp[i + j + 1]);
        }
      }
      return dp[n - 1];
    }
};
