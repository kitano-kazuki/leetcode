#include <vector>

using namespace std;

class Solution {
public:
    bool canJump(vector<int>& nums) {
      int n = nums.size();
      vector<int> dp(n, 0);
      dp[0] = 1;
      for(int i = 0; i< nums.size(); i++){
        if(dp[i] > 0){
          for(int j = 0; j < nums[i]; j++){
            if((i + j + 1) > n - 1){
              break;
            }
            dp[i + j + 1]++;
          }
        }
      }
      if(dp[n - 1] > 0){
        return true;
      }
      return false;
    }
};
