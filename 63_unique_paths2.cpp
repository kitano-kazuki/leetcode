#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int uniquePathsWithObstacles(vector<vector<int>> &obstacleGrid) {
    int rows = obstacleGrid.size();
    int cols = obstacleGrid[0].size();
    vector<vector<int>> patterns(rows, vector<int>(cols, 0));


    for (int r = 0; r < rows; r++) {
      for (int c = 0; c < cols; c++) {
        if(r == 0 && c == 0){
          patterns[r][c] = obstacleGrid[r][c] == 1 ? 0 : 1;
          continue;
        }
        if (obstacleGrid[r][c] == 1) {
          patterns[r][c] = 0;
          continue;
        }

        int first = 0;
        int second = 0;

        if (c > 0) {
          first = patterns[r][c - 1];
        }
        if (r > 0) {
          second = patterns[r - 1][c];
        }

        patterns[r][c] = first + second;
      }
    }
    return patterns[rows - 1][cols - 1];
  }
};

int main(int argc, char *argv[]) {
  vector<vector<int>> obstacleGrid(3, vector<int>(3, 0));
  Solution solution;
  int res = solution.uniquePathsWithObstacles(obstacleGrid);
  cout << res << endl;
  return 0;
}
