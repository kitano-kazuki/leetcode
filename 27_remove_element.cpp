#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int removeElement(vector<int> &nums, int val) {
    if(nums.size() == 0){
      return 0;
    }
    int left = 0;
    int right = nums.size() - 1;
    while(true){
      while(left <= nums.size() - 1 && nums[left] != val){
        left++;
      }
      while(right >= 0 && nums[right] == val){
        right--;
      }
      if(left > right){
        return left;
      }
      int temp = nums[left];
      nums[left] = nums[right];
      nums[right] = temp;
    }
  }
};
