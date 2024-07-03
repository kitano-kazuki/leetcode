#include <iterator>
#include <unordered_map>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int robMemo(vector<int>& nums, unordered_map<int,int> &memo, int index) {
      if(nums.empty()){
        return 0;
      }
      if(nums.size() == 1){
        return nums[0];
      }

      if(memo.find(index) != memo.end()){
        return memo[index];
      }
      vector<int> nums1, nums2;
      if(nums.begin() + 2 <= nums.end()){
        copy(nums.begin() + 2, nums.end(), back_inserter(nums1));
      }
      if(nums.begin() + 1 <= nums.end()){
        copy(nums.begin() + 1, nums.end(), back_inserter(nums2));
      }
      int first = nums[0] + robMemo(nums1, memo, index + 2);
      int second = robMemo(nums2, memo, index + 1);
      int res = max(first, second);
      memo[index] = res;
      return res;
    }

    int rob(vector<int> &nums){
      unordered_map<int,int> memo;
      int res = robMemo(nums, memo, 0);
      return res;
    }
};
