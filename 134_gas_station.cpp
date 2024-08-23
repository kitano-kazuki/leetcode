#include <vector>

using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
      int total_surplus = 0;
      int surplus = 0;
      int start = 0;
      for(int i = 0; i < gas.size(); i++){
        total_surplus += gas[i] - cost[i];
        surplus += gas[i] - cost[i];
        if(surplus < 0){
          surplus = 0;
          start = i + 1;
        }
      }
      if(total_surplus >= 0){
        return start;
      }
      return -1;
        
    }
};
