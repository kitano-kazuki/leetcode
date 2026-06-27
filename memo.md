# Step1

## アプローチ

* 与えられた文字列`s`中で, 最も長い回文を返す.
* 文字列の長さを`N`とする.
* ある部分を中心に左と右に伸ばしていくとする
    * 計算量: O(N^2)
    * 実行時間: 10^3 * 10^3 / 10^7 ~= 0.1 sec

## Code1-1

```cpp
#include <string>

class Solution {
public:
  std::string longestPalindrome(std::string s) {
    if (s.size() == 1){
      return s;
    }

    int longest_length = 0;
    int longest_palindrome_start = 1;
    for (int i = 0; i < s.size() - 1; i++){
      const auto& [odd_left, odd_right] = longest_palindrome_from(s, i, i);
      int odd_length = odd_right - odd_left - 1;

      const auto& [even_left, even_right] = longest_palindrome_from(s, i, i + 1);
      int even_length = even_right - even_left - 1;

      if (odd_length <= longest_length and even_length <= longest_length){
        continue;
      }

      if (odd_length >= even_length){
        longest_palindrome_start = odd_left + 1;
        longest_length = odd_length;
      } else {
        longest_palindrome_start = even_left + 1;
        longest_length = even_length;
      }
    }

    return s.substr(longest_palindrome_start, longest_length);
  }

private:
    std::pair<int,int> longest_palindrome_from(std::string& s, int left_start, int right_start){
      int left = left_start;
      int right = right_start;
      while (left >= 0 && right < s.size() && s[left] == s[right]){
        left--;
        right++;
      }
      return {left, right};
    }

};

```

# Step2

## Code2-1

* `Palindrome`構造体を用意して可読性をあげた.

```cpp
#include <string>

struct Palindrome {
  int start_pos;
  int length;

  Palindrome(int start_pos, int length) : start_pos(start_pos), length(length){};
};

class Solution {
public:
  std::string longestPalindrome(std::string s) {
    if (s.size() == 1){
      return s;
    }

    Palindrome longest_palindrome = Palindrome(0, 1);
    for (int i = 0; i < s.size() - 1; i++){
      const Palindrome& odd_palindrome = longest_palindrome_from(s, i, i);

      const Palindrome& even_palindrome = longest_palindrome_from(s, i, i + 1);

      if (odd_palindrome.length <= longest_palindrome.length and even_palindrome.length <= longest_palindrome.length){
        continue;
      }

      if (odd_palindrome.length >= even_palindrome.length){
        longest_palindrome = std::move(odd_palindrome);
      } else {
        longest_palindrome = std::move(even_palindrome);
      }
    }

    return s.substr(longest_palindrome.start_pos, longest_palindrome.length);
  }

private:
    Palindrome longest_palindrome_from(std::string& s, int left_start, int right_start){
      int left = left_start;
      int right = right_start;
      while (left >= 0 && right < s.size() && s[left] == s[right]){
        left--;
        right++;
      }
      return Palindrome{left + 1, right - left - 1};
    }

};

```

# Step3

## Code3-1

```cpp
#include <string>


struct Palindrome {
  int start;
  int length;

  Palindrome() : start(0), length(1){};
  Palindrome(int start, int length) : start(start), length(length){};
};


class Solution {
public:
  std::string longestPalindrome(std::string s) {
      if (s.empty() || s.size() == 1){
        return s;
      }

      Palindrome longest_palindrome = Palindrome{};
      for (int i = 0; i < s.size() - 1; i++){
        const Palindrome& odd_palindrome = longest_palindrome_from(s, i, i);
        const Palindrome& even_palindrome = longest_palindrome_from(s, i, i+ 1);

        if (odd_palindrome.length <= longest_palindrome.length && even_palindrome.length <= longest_palindrome.length){
          continue;
        }
        if (odd_palindrome.length >= even_palindrome.length){
          longest_palindrome = std::move(odd_palindrome);
        } else {
          longest_palindrome = std::move(even_palindrome);
        }
      }

      return s.substr(longest_palindrome.start, longest_palindrome.length);

    }

private:
    Palindrome longest_palindrome_from(std::string& s, int left_start, int right_start){
      if (s[left_start] != s[right_start]){
        return Palindrome{left_start, 0};
      }

      int left = left_start;
      int right = right_start;
      while (0 <= left and right < s.size() and s[left] == s[right]){
        left--;
        right++;
      }
      return Palindrome{left + 1, right - left - 1};
    }
};

```
