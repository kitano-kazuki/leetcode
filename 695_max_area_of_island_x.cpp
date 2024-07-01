#include <algorithm>
#include <map>
#include <vector>

using namespace std;

class Solution {
public:
  int maxAreaOfIsland(vector<vector<int>> &grid) {

    int rows = grid.size();
    int cols = grid[0].size();

    map<int, int> data;
    vector<int> idxes;
    int maxArea = 0;

    for (int r = 0; r < rows; r++) {

      auto copyData = data;
      data.clear();
      for (int c = 0; c < cols; c++) {
        if (grid[r][c] == 1) {
          idxes.push_back(c);
          if (c == cols - 1 || grid[r][c + 1] == 0) {
            int curArea = idxes.size();
            for (int idx : idxes) {
              if (copyData.find(idx) != copyData.end()) {
                curArea += copyData[idx];
                break;
              }
            }
            for (int idx : idxes) {
              data[idx] = curArea;
            }
            idxes.clear();
          }
        }
      }
      for (auto item : data) {
        maxArea = max(maxArea, item.second);
      }
    }
    return maxArea;
  }
};
