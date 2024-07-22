#include <vector>

using namespace std;
class Solution {
public:
  int maxProfit(vector<int> &prices) {
    int left = 0;
    int right = 0;
    int profit = 0;

    while (true) {
      while (left != prices.size() - 1 && prices[left] >= prices[left + 1]) {
        left++;
      }
      if (left == prices.size() - 1) {
        return profit;
      }
      right = left + 1;
      while (right != prices.size() - 1 && prices[right] <= prices[right + 1]) {
        right++;
      }
      profit += prices[right] - prices[left];
      if (right == prices.size() - 1) {
        return profit;
      }
      left = right + 1;
    }
  }
};
