# Step1

## アプローチ

* 長さnの配列`height`が与えられる
* 最も多く水をためられる時の水の量を返す
* 両端から始める. 横幅を縮めても高さが増えるなら, 高さが増える方向に横幅を縮める
    * `[3, 6, 1]`などの場合は, 更新のやり方によっては最大の水を捉えられない.
* 小さい方を常に進める

## Code1-1 (WA)

* `[3, 6, 1]`などの場合は, 更新のやり方によっては最大の水を捉えられない.

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxArea(std::vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int maximum_water = 0;
        while (left < right){
            maximum_water = std::max(maximum_water, (right - left) * std::min(height[left], height[right]));
            if (height[left] < height[left + 1]){
                left++;
                continue;
            }
            if (height[right] < height[right - 1]){
                right--;
                continue;
            }
            left++;
        }
        return maximum_water;
    }
};
```

## Code1-2


```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxArea(std::vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int maximum_water = 0;
        while (left < right){
            maximum_water = std::max(maximum_water, (right - left) * std::min(height[left], height[right]));
            if (height[left] <= height[right]){
                left++;
            } else {
                right--;
            }
        }
        return maximum_water;
    }
};
```

# Step2

## Code2-2

* 変更なし

```cpp
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxArea(std::vector<int>& height) {
        int left = 0;
        int right = height.size() - 1;
        int maximum_water = 0;
        while (left < right){
            maximum_water = std::max(maximum_water, (right - left) * std::min(height[left], height[right]));
            if (height[left] <= height[right]){
                left++;
            } else {
                right--;
            }
        }
        return maximum_water;
    }
};
```

## 他の人のPRを見る

* https://github.com/thonda28/leetcode/pull/16
    * SegmentTreeの実装をしている.
    * > たとえば、Max を返すような Segment Tree で、高さを Key としてその高さの座標を入れると、ある高さ以上の壁がどこにあるかを log n で知ることができます。(これだと両側やらないといけませんが。)
    * > Segment tree は区間内の最大値(最小値や和の場合も)を返せるデータ構造です。ここでは、ある高さ以上の壁のある場所を知りたいので、区間として、高さの方をとって、値として壁の位置を取ります。
* https://github.com/tom4649/Coding/pull/67

## Code2-3 (Segment Tree)

* 変数の命名について
    * クラスのメンバは`_`を後ろにつける
        * https://google.github.io/styleguide/cppguide.html#Variable_Names
            * > Data members of classes, both static and non-static, are named like ordinary nonmember variables, but with a trailing underscore
    * ストラクトのメンバは, `_`を後ろにつけない
        * https://google.github.io/styleguide/cppguide.html#Variable_Names
            * > Data members of structs, both static and non-static, are named like ordinary nonmember variables. They do not have the trailing underscores that data members in classes have.
* クラスとストラクトの使い分けについて
    * データを表すもの以外はクラスを使用
        * https://google.github.io/styleguide/cppguide.html#Structs_vs._Classes
            * > Use a struct only for passive objects that carry data; everything else is a class.
* クラス内での宣言の順番について
    * public -> protected -> privateでかつ, nested class or struct -> function -> member
        * https://google.github.io/styleguide/cppguide.html#Declaration_Order
            ```
            Group similar declarations together, placing public parts earlier.

            A class definition should usually start with a public: section, followed by protected:, then private:. Omit sections that would be empty.

            Within each section, prefer grouping similar kinds of declarations together, and prefer the following order:

            Types and type aliases (typedef, using, enum, nested structs and classes, and friend types)
            (Optionally, for structs only) non-static data members
            Factory functions
            Static constants
            Constructors and assignment operators
            Destructor
            All other functions (static and non-static member functions, and friend functions)
            All other data members (static and non-static)
            Do not put large method definitions inline in the class definition. Usually, only trivial or performance-critical, and very short, methods may be defined inline. See Defining Functions in Header Files for more details.
            ```
* 関数の命名について
    * パスカルケースで書く
        * https://google.github.io/styleguide/cppguide.html#Function_Names
            * > Ordinarily, functions follow PascalCase: start with a capital letter and have a capital letter for each new word.



```cpp
#include <vector>
#include <algorithm>
#include <functional>
#include <cstddef>
#include <limits>

// 区間の最大を求めるSeg木
class SegmentTree {

public:
  SegmentTree(const std::vector<int>& array, const std::function<int(int, int)>& operation, int default_value) : array_(array), tree_(4 * array.size()),  operation_(operation), default_value_(default_value) {
    BuildImplementation(1, 0, array_.size() - 1);
  }

  void Update(int array_i, int new_value){
    UpdateImplementation(1, 0, array_.size() - 1, array_i, new_value);
  }

  int Query(int query_left, int query_right) const {
    return QueryImplementation(1, 0, array_.size() - 1, query_left, query_right);
  }

private:
  void BuildImplementation(int node_i, int left, int right){
    if (left == right){
      tree_[node_i] = array_[left];
      return;
    }
    int mid = left + (right - left) / 2;
    BuildImplementation(node_i * 2, left, mid);
    BuildImplementation(node_i * 2 + 1, mid + 1, right);
    tree_[node_i] = operation_(tree_[node_i * 2], tree_[node_i * 2 + 1]);
  }

  void UpdateImplementation(int node_i, int left, int right, int array_i, int new_value){
    if (left == right){
      array_[array_i] = new_value;
      tree_[node_i] = new_value;
      return;
    }
    int mid = left + (right - left) / 2;
    if (left <= array_i and array_i <= mid){
      UpdateImplementation(node_i * 2, left, mid, array_i, new_value);
    } else {
      UpdateImplementation(node_i * 2 + 1, mid + 1, right, array_i, new_value);
    }
    tree_[node_i] = operation_(tree_[node_i * 2], tree_[node_i * 2 + 1]);
  }

  int QueryImplementation(int node_i, int left, int right, int query_left, int query_right) const {
    if (right < query_left || query_right < left) {
      return default_value_;
    }
    if (left == query_left && right == query_right) {
      return tree_[node_i];
    }
    int mid = left + (right - left) / 2;
    if (query_right <= mid) {
      return QueryImplementation(node_i * 2, left, mid, query_left, query_right);
    }
    if (mid + 1 <= query_left) {
      return QueryImplementation(node_i * 2 + 1, mid + 1, right, query_left, query_right);
    }
    int left_max = QueryImplementation(node_i * 2, left, mid, query_left, mid);
    int right_max = QueryImplementation(node_i * 2 + 1, mid + 1, right, mid + 1, query_right);
    return operation_(left_max, right_max);
  }

  std::vector<int> array_;
  std::vector<int> tree_; // 1-based
  std::function<int(int, int)> operation_;
  int default_value_;
};

class Solution {
public:
    int maxArea(std::vector<int>& height) {
      int max_height = *std::max_element(height.begin(), height.end());
      std::vector<int> indices_for_min_tree(max_height + 1, std::numeric_limits<int>::max());
      std::vector<int> indices_for_max_tree(max_height + 1, std::numeric_limits<int>::min());
      for (int i = 0; i < height.size(); i++) {
        indices_for_min_tree[height[i]] = std::min(indices_for_min_tree[height[i]], i);
        indices_for_max_tree[height[i]] = std::max(indices_for_max_tree[height[i]], i);
      }

      SegmentTree min_segment_tree(indices_for_min_tree, [](int a, int b){return std::min(a, b);}, std::numeric_limits<int>::max());
      SegmentTree max_segment_tree(indices_for_max_tree, [](int a, int b){return std::max(a, b);}, std::numeric_limits<int>::min());

      int max_area = 0;
      for (int i = 0; i < height.size(); i++) {
        int h = height[i];

        int left = min_segment_tree.Query(h, max_height);
        int left_area = std::numeric_limits<int>::min();
        if (left < i) {
          left_area = (i - left) * h;
        }

        int right = max_segment_tree.Query(h, max_height);
        int right_area = std::numeric_limits<int>::min();
        if (i < right) {
          right_area = (right - i) * h;
        }

        max_area = std::max({max_area, left_area, right_area});
      }

      return max_area;

    }
};

```

# Step3

## Code3-2

```cpp
#include <vector>
#include <algorithm>


class Solution {
public:
    int maxArea(std::vector<int>& height) {
      int left = 0;
      int right = height.size() - 1;
      int max_area = 0;
      while (left < right) {
        max_area = std::max(max_area, (right - left) * std::min(height[left], height[right]));
        if (height[left] <= height[right]) {
          left++;
        } else {
          right--;
        }
      }

      return max_area;

    }
};

```
