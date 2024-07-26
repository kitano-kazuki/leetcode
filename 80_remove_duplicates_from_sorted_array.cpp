#include <vector>

using namespace std;

class Solution {
public:
  int removeDuplicates(vector<int> &nums) {
    int idx = 1;
    int count = 0;
    for (int i = 1; i < nums.size(); i++) {
      if (nums[i] == nums[i - 1]) {
        count++;
      } else {
        count = 0;
      }
      if (count < 2) {
        nums[idx] = nums[i];
        idx++;
      }
    }

    return idx;
  }
};
