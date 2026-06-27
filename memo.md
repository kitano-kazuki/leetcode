# Step1

## アプローチ

* 与えられた行列の要素を螺旋状に出力する
* 方向と範囲を指定して, 繰り返し出力を行えばよさそう

## Code1-1

```cpp
#include <vector>

enum Position {Top, Right, Bottom, Left};


class Solution {
public:
  std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix) {
    std::vector<int> spiral;
    append_line_to_spiral(Top, 0, matrix[0].size() - 1, matrix.size() - 1, 0, matrix, spiral);
    return spiral;
  }

  void append_line_to_spiral(
      Position position,
      int top,
      int right,
      int bottom,
      int left,
      std::vector<std::vector<int>>& matrix,
      std::vector<int>& spiral
    ){
      if (top > bottom || left > right){
        return;
      }
      if (position == Top){
        for (int i = left; i <= right; i++){
          spiral.push_back(matrix[top][i]);
        }
        append_line_to_spiral(Right, top + 1, right, bottom, left, matrix, spiral);
        return;
      }
      if (position == Right){
        for (int j = top; j <= bottom; j++){
          spiral.push_back(matrix[j][right]);
        }
        append_line_to_spiral(Bottom, top, right - 1, bottom, left, matrix, spiral);
        return;
      }
      if (position == Bottom){
        for (int i = right; i >= left; i--){
          spiral.push_back(matrix[bottom][i]);
        }
        append_line_to_spiral(Left, top, right, bottom - 1, left, matrix, spiral);
        return;
      }
      if (position == Left){
        for (int j = bottom; j >= top; j--){
          spiral.push_back(matrix[j][left]);
        }
        append_line_to_spiral(Top, top, right, bottom, left + 1, matrix, spiral);
        return;
      }
    }
};

```

# Step2

## Code2-1

* 変更なし

```cpp
#include <vector>

enum Position {Top, Right, Bottom, Left};


class Solution {
public:
  std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix) {
    std::vector<int> spiral;
    append_line_to_spiral(Top, 0, matrix[0].size() - 1, matrix.size() - 1, 0, matrix, spiral);
    return spiral;
  }

  void append_line_to_spiral(
      Position position,
      int top,
      int right,
      int bottom,
      int left,
      std::vector<std::vector<int>>& matrix,
      std::vector<int>& spiral
    ){
      if (top > bottom || left > right){
        return;
      }
      if (position == Top){
        for (int i = left; i <= right; i++){
          spiral.push_back(matrix[top][i]);
        }
        append_line_to_spiral(Right, top + 1, right, bottom, left, matrix, spiral);
        return;
      }
      if (position == Right){
        for (int j = top; j <= bottom; j++){
          spiral.push_back(matrix[j][right]);
        }
        append_line_to_spiral(Bottom, top, right - 1, bottom, left, matrix, spiral);
        return;
      }
      if (position == Bottom){
        for (int i = right; i >= left; i--){
          spiral.push_back(matrix[bottom][i]);
        }
        append_line_to_spiral(Left, top, right, bottom - 1, left, matrix, spiral);
        return;
      }
      if (position == Left){
        for (int j = bottom; j >= top; j--){
          spiral.push_back(matrix[j][left]);
        }
        append_line_to_spiral(Top, top, right, bottom, left + 1, matrix, spiral);
        return;
      }
    }
};
```

## 他の人のPRを見る

* https://github.com/huyfififi/coding-challenges/pull/53
    * `delta_row`と`delta_col`を持っておいて, 値をそのデルタの方向に進めていく. 配列外あるいはすでに訪れたところだった場合は, 方向を90度変える.

### Code2-2 (go and rotate)

```cpp
#include <utility>
#include <vector>


class Solution {
public:
  std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix) {
    int m = matrix.size();
    int n = matrix[0].size();
    int num_elements = m * n;

    std::vector<int> spiral;
    std::vector<std::vector<bool>> visited(m, std::vector<bool>(n, false));

    int row = 0;
    int col = 0;
    int dr = 0;
    int dc = 1;

    for (int i = 0; i < num_elements; i++){
      spiral.push_back(matrix[row][col]);
      visited[row][col] = true;

      bool is_next_in_range = (0 <= row + dr and row + dr < m) and (0 <= col + dc and col + dc < n);
      if (!is_next_in_range || visited[row + dr][col + dc]){
        int temp = dc;
        dc = -dr;
        dr = temp;
      }

      row = row + dr;
      col = col + dc;

    }

    return spiral;
  }

};

```

# Step3

## Code3-1

```cpp
#include <utility>
#include <vector>


class Solution {
public:
  std::vector<int> spiralOrder(std::vector<std::vector<int>>& matrix) {
    int num_rows = matrix.size();
    int num_cols = matrix[0].size();

    int top = 0;
    int bottom = num_rows - 1;
    int left = 0;
    int right = num_cols - 1;

    std::vector<int> spiral;
    while (top <= bottom && left <= right){
      for (int c = left; c <= right; c++){
        spiral.push_back(matrix[top][c]);
      }
      top++;

      for (int r = top; r <= bottom; r++){
        spiral.push_back(matrix[r][right]);
      }
      right--;

      if (top <= bottom){
        for (int c = right; c >= left; c--){
          spiral.push_back(matrix[bottom][c]);
        }
        bottom--;
      }

      if (left <= right){
        for (int r = bottom; r >= top; r--){
          spiral.push_back(matrix[r][left]);
        }
        left++;
      }
    }

    return spiral;
  }

};

```
