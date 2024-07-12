#include <cstdint>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> kSmallestPairs(vector<int> &nums1, vector<int> &nums2,
                                     int k) {

    vector<vector<int>> ans;

    unordered_map<int, int> m;
    for (int i = 0; i < nums1.size(); i++) {
      m[nums1[i]] = 0;
    }

    int c = 0;

    int p = 0;

    int minIdx = 0;
    int minIdx2 = 0;
    while (true) {
      vector<int> pair;
      int min = INT32_MAX;
      for (int i = 0; i <= p; i++) {
        if(i >= nums1.size()){
          continue;
        }
        if(m[i] >= nums2.size()){
          continue;
        }
        int i2 = m[i];
        int sum = nums1[i] + nums2[i2];
        if (sum < min) {
          min = sum;
          minIdx = i;
          minIdx2 = i2;
        }
      }
      if(min == INT32_MAX){
        break;
      }
      pair.push_back(nums1[minIdx]);
      pair.push_back(nums2[minIdx2]);
      ans.push_back(pair);
      c++;
      m[minIdx] += 1;
      if (minIdx2 == 0) {
        p++;
      }
      if(c == k){
        return ans;
      }
    }
    return ans;
  }
};
