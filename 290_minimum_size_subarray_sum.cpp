#include <climits>
#include <vector>
using namespace std;
class Solution {
public:
  // NOTE: Time limit exceeded (18/21 passed)

  // int minSubArrayLen(int target, vector<int> &nums) {
  //   int minimum = 0;
  //   for(int i = 0; i < nums.size(); i++){
  //     int sum = 0;
  //     for(int j = i; j < nums.size(); j++){
  //       sum += nums[j];
  //       if(sum >= target){
  //         if(minimum == 0 || j - i + 1 < minimum) {
  //           minimum = j - i + 1;
  //         }
  //       }
  //     }
  //   }
  //   return minimum;
  // }

  int minSubArrayLen(int target, vector<int> &nums) {
    int left = 0;
    int right = 0;
    int sum = 0;
    int min = INT_MAX;
    for (; right < nums.size(); right++) {
      sum += nums[right];
      while (sum >= target) {
        int length = right - left + 1;
        if (length < min) {
          min = length;
        }
        sum -= nums[left];
        left++;
      }
    }
    return (min == INT_MAX) ? 0 : min;
  }
};
