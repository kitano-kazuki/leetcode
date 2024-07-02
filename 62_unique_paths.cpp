#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
  int combination(int n, int r, vector<vector<int>> &memo) {
    if (memo[n][r] != -1) {
      return memo[n][r];
    }

    if(n == r){
      memo[n][r] = 1;
      return 1;
    }

    if (r == 1) {
      memo[n][r] = n;
      return n;
    }

    int result = combination(n - 1, r, memo) + combination(n - 1, r - 1, memo);
    memo[n][r] = result;
    return result;
  }
  int uniquePaths(int m, int n) {
    int col = min(m - 1, n - 1);
    if (col == 0){
      return 1;
    }
    vector<vector<int>> memo(m + n - 1, vector<int>(col + 1, -1));
    int result = combination(m + n - 2, col, memo);
    return result;
  }
};

int main(int argc, char *argv[]) {
  Solution solution;
  int res = solution.uniquePaths(3, 7);
  cout << res << endl;
  return 0;
}
