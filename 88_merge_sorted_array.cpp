#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
  void merge(vector<int> &nums1, int m, vector<int> &nums2, int n) {
    int idx = m + n - 1;
    int i1 = m - 1;
    int i2 = n - 1;
    while (i2 >= 0) {
      if (i1 < 0) {
        nums1[idx] = nums2[i2];
        i2--;
      } else if (nums1[i1] > nums2[i2]) {
        nums1[idx] = nums1[i1];
        i1--;
      } else {
        nums1[idx] = nums2[i2];
        i2--;
      }
      idx--;
    }
  }
};
