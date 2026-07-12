# Step1

## 問題文

```
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
```

## アプローチ

* 自分より高さの高い棒が自分の右にいつ出てくるかを調べる
    * その間については, ``自分の高さ - 棒の高さ`分の水をためられる
* 同様に、 自分の高さ以上の棒が自分の左にいつ出てくるかを調べる
* この方法で重複は生まれない
* 計算量
    * O(N)
    * 実行時間: 10^4 / 10^7 ~= 10^-3 sec

## Code1-1 (Monotonous Increasing Stack)

* 39minかかった
* 本当は, monotonous increasing stackでの構築中に水の面積を数えたかったが、途中でわからなくなってしまったのでunordered_mapを使うやり方にした.

```cpp
#include <stack>
#include <unordered_map>
#include <vector>


class Solution {
public:
    int trap(std::vector<int>& height) {
      std::unordered_map<int, int> leftward_higher_or_equal;
      std::unordered_map<int, int> rightward_higher;
      construct_next_higher_map(height, leftward_higher_or_equal, rightward_higher);

      int water_area = 0;

      int index = 0;
      while (index < height.size()) {
        int right_higher_index = rightward_higher[index];
        if (right_higher_index == height.size()) {
          break;
        }
        for (int i = index + 1; i < right_higher_index; i++) {
          water_area += height[index] - height[i];
        }
        index = right_higher_index;
      }

      index = height.size() - 1;
      while (index >= 0) {
        int left_higher_or_equal_index = leftward_higher_or_equal[index];
        if (left_higher_or_equal_index == -1) {
          break;
        }
        for (int i = index - 1; i > left_higher_or_equal_index; i--) {
          water_area += height[index] - height[i];
        }
        index = left_higher_or_equal_index;
      }

      return water_area;
    }

private:
    void construct_next_higher_map(const std::vector<int>& height, std::unordered_map<int, int>& leftward_higher_or_equal, std::unordered_map<int, int>& rightward_higher) {
      std::stack<int> higher_heights;
      
      for (int index = 0; index < height.size(); index++) {
        while (!higher_heights.empty() && height[index] > height[higher_heights.top()]) {
          higher_heights.pop();
        }
        if (higher_heights.empty()) {
          leftward_higher_or_equal[index] = -1;
        } else {
          leftward_higher_or_equal[index]  = higher_heights.top();
        }
        higher_heights.push(index);
      }

      higher_heights = std::stack<int>();
      
      for (int index = height.size() - 1; index >= 0; index--) {
        while (!higher_heights.empty() && height[index] >= height[higher_heights.top()]) {
          higher_heights.pop();
        }
        if (higher_heights.empty()) {
          rightward_higher[index] = height.size();
        } else {
          rightward_higher[index] = higher_heights.top();
        }
        higher_heights.push(index);
      }
    }

};


```

# Step2

## 他の人のPRをみる

* https://github.com/tom4649/Coding/pull/124
* https://github.com/yamashita-ki/codingTest/pull/6/changes


## Code2-2 (Two Pointer)

* 棒`i`について考える
    * 棒`i`の上にたまる水の量は, 
        * 棒`i`より左側の最大の棒の高さ
        * 棒`i`より右側の最大の棒の高さ
        * 上記二つのうちの小さい方の棒`j`から, 棒`i`の高さを引いたもの
        * 棒`j`の高さが, 棒`i`よりも小さかったら水はたまらない

```cpp
#include <vector>


class Solution {
public:
    int trap(std::vector<int>& height) {
      int left = 0;
      int right = height.size() - 1;

      int max_leftward_height = 0;
      int max_rightward_height = 0;

      int trapped_water = 0;
      while (left <= right) {
        if (max_leftward_height <= max_rightward_height) {
          trapped_water += std::max(max_leftward_height - height[left], 0);
          max_leftward_height = std::max(max_leftward_height, height[left]);
          left++;
        } else {
          trapped_water += std::max(max_rightward_height - height[right], 0);
          max_rightward_height = std::max(max_rightward_height, height[right]);
          right--;
        }
      }

      return trapped_water;
    }
};

```


## Code2-3 (Monotonic Stack with One Path)

* 棒`i`について考える. 棒`i`の高さを`h_i`とする.
    * 棒`i`を右端とした時に, 左側にどれだけ水がたまるか
    * 棒`i`より左側で最初に登場する高さが棒`i`より低い棒を棒`j`とする
    * 棒`j`より左側で最初に登場する高さが棒`j`より高い棒を棒`k`とする
    * 棒`k`から棒`i`の間は, `min(h_i, h_k)`分の水を貯めるキャパがある
    * もれなく重複なく考えるためには, 棒`j`より高い部分に溜まった水だけを各段階で加えるようにすればいい

```cpp
#include <stack>
#include <vector>


class Solution {
public:
    int trap(std::vector<int>& height) {
      int trapped_water = 0;
      std::stack<int> leftward_smaller_indices;

      for (int i = 0; i < height.size(); i++) {
        while (!leftward_smaller_indices.empty() && height[i] > height[leftward_smaller_indices.top()]) {
          int bottom = leftward_smaller_indices.top();
          leftward_smaller_indices.pop();

          if (leftward_smaller_indices.empty()) {
            break;
          }

          int left = leftward_smaller_indices.top();
          int width = i - left - 1;
          trapped_water += width * (std::min(height[left], height[i]) - height[bottom]);
        }
        leftward_smaller_indices.push(i);
      }

      return trapped_water;
    }
};

```


# Step3

## Code3-2 (Two Pointer)

```cpp
#include <vector>


class Solution {
public:
    int trap(std::vector<int>& height) {
      int left = 0;
      int right = height.size() - 1;

      int leftward_max_height = 0;
      int rightward_max_height = 0;

      int trapped_water = 0;
      while (left <= right) {
        if (leftward_max_height <= rightward_max_height) {
          trapped_water += std::max(leftward_max_height - height[left], 0);
          leftward_max_height = std::max(leftward_max_height, height[left]);
          left++;
        } else {
          trapped_water += std::max(rightward_max_height - height[right], 0);
          rightward_max_height = std::max(rightward_max_height, height[right]);
          right--;
        }
      }
      return trapped_water;
    }
};

```
