#include <algorithm>
#include <vector>

using namespace std;

class Solution {

public:
  vector<int> intersection(vector<int> &nums1, vector<int> &nums2) {
    vector<int> ans;
    for (int i = 0; i < nums1.size(); i++) {
      int target = nums1[i];
      for (int j = 0; j < nums2.size(); j++) {
        if (target == nums2[j]) {
          if (find(ans.begin(), ans.end(), target) == ans.end()) {
            ans.push_back(target);
          }
        }
      }
    }
    return ans;
  }
};
