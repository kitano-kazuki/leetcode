#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> topKFrequent(vector<int> &nums, int k) {
    // key: num, val: count
    map<int, int> dp;

    for (int i = 0; i < nums.size(); i++) {
      dp[nums[i]] += 1;
    }

    vector<pair<int,int>> p;
    for(auto item : dp){
      p.push_back(pair<int,int>(item.second, item.first));
    }
    sort(p.rbegin(), p.rend());

    vector<int> answer;
    for(int i = 0; i < k; i++){
      answer.push_back(p[i].second);
    }

    return answer;


  }
};
