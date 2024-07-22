#include <algorithm>
#include <cstdint>
#include <vector>

using namespace std;

class Solution {
public:
  int maxProfit(vector<int> &prices) {
    int n = prices.size();
    vector<int> dp(n);
    int buy = prices[0];
    int sell = prices[0];
    int minimum = prices[0];
    dp[0] = 0;
    for (int i = 1; i < n; i++) {
      if(prices[i] < buy){
        if(dp[i-1] == 0){
          buy = prices[i];
          sell = prices[i];
          dp[i] = 0;
        }
        minimum = min(minimum,prices[i]);
        dp[i] = dp[i - 1];
      }

      if (prices[i] > sell) {
        dp[i] = dp[i-1] - sell + prices[i];
        sell = prices[i];
      }

      if(prices[i] - minimum > dp[i]){
        dp[i] = prices[i] - minimum;
        buy = minimum;
        sell = prices[i];
      }

    }
    auto iter = max_element(dp.begin(), dp.end());
    return *iter;
  }

};
