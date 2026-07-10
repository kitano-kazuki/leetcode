# Step1

## 問題設定

* 長さ`m`の文字列`s`と長さ`n`の文字列`t`が与えられる.
* `t`に含まれる全ての文字を含む最小の`s`の部分文字列を見つける.

## アプローチ

* `left`と`right`でwindowを決めることにする
* window内に`t`の文字が全て含まれていないなら, `right`を右に動かす.
* window内に`t`の文字が全て含まれているなら, より小さいwindowを試したいから, `left`を右に動かす.
* 計算量
    * O(M + N)

## Code1-1

```cpp
#include <limits>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>


class Solution {
public:
  std::string minWindow(std::string s, std::string t) {
    if (s.size() < t.size()) {
      return "";
    }

    std::unordered_map<char, int> char_to_count_in_t;
    for (char c : t) {
      char_to_count_in_t[c]++;
    }

    std::unordered_map<char, int> char_to_count_in_window;
    int left = 0;
    int right = 0;
    int min_window_left = -1;
    int min_window_right = -1;
    int min_window_size = std::numeric_limits<int>::max();
    while (true) {
      if (CheckWindowValidity(char_to_count_in_window, char_to_count_in_t) > 0) {
        if (right - left < min_window_size) {
          min_window_size = right - left;
          min_window_left = left;
          min_window_right = right;
        }
        char_to_count_in_window[s[left]]--;
        left++;
        continue;
      } else if (right < s.size()){
        char_to_count_in_window[s[right]]++;
        right++;
        continue;
      }
      if (min_window_left != -1) {
        return s.substr(min_window_left, min_window_size);
      } else {
        return "";
      }
    }
  }

private:
  // 1 -> window contains more or equal number of chars in t
  // -1 -> window lacks char(s) in t
  int CheckWindowValidity(const std::unordered_map<char, int>& char_to_count_in_window, const std::unordered_map<char, int>& char_to_count_in_t) {
    for (auto [char_in_t, count] : char_to_count_in_t) {
      if (char_to_count_in_window.find(char_in_t) == char_to_count_in_window.end()) {
        return -1;
      }
      if (char_to_count_in_window.at(char_in_t) < count) {
        return -1;
      }
    }
    return 1;
  }
};

```

# Step2

## Code2-1

* 変更なし

```cpp
#include <limits>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>


class Solution {
public:
  std::string minWindow(std::string s, std::string t) {
    if (s.size() < t.size()) {
      return "";
    }

    std::unordered_map<char, int> char_to_count_in_t;
    for (char c : t) {
      char_to_count_in_t[c]++;
    }

    std::unordered_map<char, int> char_to_count_in_window;
    int left = 0;
    int right = 0;
    int min_window_left = -1;
    int min_window_right = -1;
    int min_window_size = std::numeric_limits<int>::max();
    while (true) {
      if (CheckWindowValidity(char_to_count_in_window, char_to_count_in_t) > 0) {
        if (right - left < min_window_size) {
          min_window_size = right - left;
          min_window_left = left;
          min_window_right = right;
        }
        char_to_count_in_window[s[left]]--;
        left++;
        continue;
      } else if (right < s.size()){
        char_to_count_in_window[s[right]]++;
        right++;
        continue;
      }
      if (min_window_left != -1) {
        return s.substr(min_window_left, min_window_size);
      } else {
        return "";
      }
    }
  }

private:
  // 1 -> window contains more or equal number of chars in t
  // -1 -> window lacks char(s) in t
  int CheckWindowValidity(const std::unordered_map<char, int>& char_to_count_in_window, const std::unordered_map<char, int>& char_to_count_in_t) {
    for (auto [char_in_t, count] : char_to_count_in_t) {
      if (char_to_count_in_window.find(char_in_t) == char_to_count_in_window.end()) {
        return -1;
      }
      if (char_to_count_in_window.at(char_in_t) < count) {
        return -1;
      }
    }
    return 1;
  }
};


```

## 他の人のPRをみる

* https://github.com/tom4649/Coding/pull/127
    * `right`を`for`文で回している
    * `right`の位置ごとに, `window`内の個数が規定よりも多ければ`left`を動かすようにする
* https://github.com/hayashi-ay/leetcode/pull/73
    * `t`に含まれる文字ごとに数を記録している辞書を再利用
    * 辞書のカウントがマイナスの時は、ウィンドウ内にtよりも多くの個数文字が含まれている
    * 辞書とは別に、ウィンドウ内で使っているt中の文字の数を保存

## Code2-2 (One Dictionary)

```cpp
#include <limits>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>


class Solution {
public:
  std::string minWindow(std::string s, std::string t) {
    if (s.size() < t.size()) {
      return "";
    }

    std::unordered_map<char, int>  char_to_count;
    for (char c : t) {
      char_to_count[c]++;
    }

    int left = 0;
    int num_used = 0;
    int min_window_left = 0;
    int min_window_size = std::numeric_limits<int>::max();
    for (int right = 0; right < s.size(); right++) {
      if (char_to_count.find(s[right]) != char_to_count.end()) {
        if (char_to_count[s[right]] > 0) {
          num_used++;
        }
        char_to_count[s[right]]--;
      }

      while (num_used == t.size()) {
        int window_size = right - left + 1;
        if (window_size < min_window_size) {
          min_window_left = left;
          min_window_size = window_size;
        }
        if (char_to_count.find(s[left]) != char_to_count.end()) {
          char_to_count[s[left]]++;
          if (char_to_count[s[left]] > 0) {
            num_used--;
          }
        }
        left++;
      }
    }

    if (min_window_size == std::numeric_limits<int>::max()) {
      return "";
    }
    return s.substr(min_window_left, min_window_size);

  }

};

```


# Step3

## Code3-2 (One Dictionary)

```cpp
#include <limits>
#include <numeric>
#include <string>
#include <unordered_map>
#include <vector>


class Solution {
public:
  std::string minWindow(std::string s, std::string t) {
    if (s.size() < t.size()) {
      return "";
    }

    std::unordered_map<char, int> char_to_count;
    for (char c : t) {
      char_to_count[c]++;
    }

    int left = 0;
    int min_window_left = -1;
    int min_window_size = std::numeric_limits<int>::max();
    int num_used = 0;
    for (int right = 0; right < s.size(); right++) {
      if (char_to_count.find(s[right]) == char_to_count.end()) {
        continue;
      }
      if (char_to_count[s[right]] > 0) {
        num_used++;
      }
      char_to_count[s[right]]--;

      if (num_used < t.size()) {
        continue;
      }

      while (num_used == t.size()) {
        int window_size = right - left + 1;
        if (window_size < min_window_size) {
          min_window_left = left;
          min_window_size = window_size;
        }
        if (char_to_count.find(s[left]) == char_to_count.end()) {
          left++;
          continue;
        }
        char_to_count[s[left]]++;
        if (char_to_count[s[left]] > 0) {
          num_used--;
        }
        left++;
      }
    }

      if (min_window_size == std::numeric_limits<int>::max()) {
        return "";
      }
      return s.substr(min_window_left, min_window_size);
  }

};

```
