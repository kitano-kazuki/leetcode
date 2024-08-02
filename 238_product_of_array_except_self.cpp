#include <vector>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
      int n = nums.size();
      vector<int> ans(n, 1);
      int cur = 1;
      for(int i = 0; i < n; i++){
        ans[i] *= cur;
        cur *= nums[i];
      }
      cur = 1;
      for(int i = n- 1; i >= 0; i--){
        ans[i] *= cur;
        cur *= nums[i];
      }
        
      return ans;
    }
};
