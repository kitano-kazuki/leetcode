#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
  void countIsland(vector<vector<char>> &grid, int r, int c, int &count,
                   bool isFirstCall) {
    if (r < 0 || c < 0 || r >= grid.size() || c >= grid[0].size()) {
      return;
    }
    if (grid[r][c] == 0) {
      return;
    }
    if (grid[r][c] == '1') {
      if (isFirstCall){
        count++;
      }
      grid[r][c] = '0';
      countIsland(grid, r - 1, c, count, false);
      countIsland(grid, r, c - 1, count, false);
      countIsland(grid, r, c + 1, count, false);
      countIsland(grid, r + 1, c, count, false);
    }
  }

  int numIslands(vector<vector<char>> &grid) {
    int count = 0;
    for (int r = 0; r < grid.size(); r++) {
      for (int c = 0; c < grid[0].size(); c++) {
        countIsland(grid, r, c, count, true);
      }
    }
    return count;
  }
};
