# Step1

## アプローチ

* `s`と`p`が与えられる.
* `s`の中で`p`のアナグラムの開始位置となるインデックスを全て見つける
* アプローチ1
    * `p`のアナグラムを全て計算しておいて, `s`の各位置ごとに`p`の文字数だけ部分文字列を取得l. それが`p`のアナグラム集合に含まれるかを確認する.
* アプローチ2
    * `p`に含まれる文字の種類と数を記録しておく
    * 幅`p.size()`のwindowを右にずらしていく中で, `p`に含まれる文字の種類と数と, window内に含まれる文字の種類と数が一致する場所を探す
* 計算量を考える
    * `s.size() = N`, `p.size() = M`とする
    * アプローチ1の計算量
        * `p`のアナグラムの集合の構築に, O(M! * M)
        * `s`の各位置ごとに, 部分文字列を取得してハッシュを計算するので, `s`中のすべての位置を確認すると, O(N * M)
        * トータルで, O(M! * M + N * M)
        * 実行時間は (3 * 10^4)! / 10^7 なのでとてつもなく遅い
    * アプローチ2の計算量
        * 余分に含まれているものの個数, 足りていないものの個数を記録しておくとする.
        * 各回では, 更新するごとに, 上記二つが空になっているかをみればいい
        * 計算量はO(M + N)
        * 実行時間は 3 * 10^4 * 2 / 10^7 ~= 10^-2 secくらい

## Code1-1

```cpp
#include <vector>
#include <unordered_map>
#include <cstdlib>


class Solution {
public:
  std::vector<int> findAnagrams(std::string s, std::string p) {
    if (s.size() < p.size()) {
      return {};
    }
    std::unordered_map<char, int> letter_to_count_in_p;
    for (const char& c : p) {
      letter_to_count_in_p[c] += 1;
    }

    std::unordered_map<char, int> letter_to_count_in_window;
    for (int i = 0; i < p.size(); i++) {
      letter_to_count_in_window[s[i]] += 1;
    }

    int num_incorrects = 0;
    for (const auto& [letter, count] : letter_to_count_in_p) {
      num_incorrects += std::abs(count - letter_to_count_in_window[letter]);
    }
    for (const auto& [letter, count] : letter_to_count_in_window) {
      if (letter_to_count_in_p.find(letter) == letter_to_count_in_p.end()) {
        num_incorrects += count;
      }
    }

    std::vector<int> anagram_start_indices;
    if (num_incorrects == 0) {
      anagram_start_indices.push_back(0);
    }

    for (int left = 1; left + p.size() - 1 < s.size(); left++) {
      int right = left + p.size() - 1;
      const char& letter_to_remove = s[left - 1];
      if (letter_to_count_in_window[letter_to_remove] > letter_to_count_in_p[letter_to_remove]) {
        num_incorrects -= 1;
      } else {
        num_incorrects += 1;
      }
      letter_to_count_in_window[letter_to_remove] -= 1;

      const char& letter_to_add = s[right];
      if (letter_to_count_in_window[letter_to_add] < letter_to_count_in_p[letter_to_add]) {
        num_incorrects -= 1;
      } else {
        num_incorrects += 1;
      }
      letter_to_count_in_window[letter_to_add] += 1;

      if (num_incorrects == 0) {
        anagram_start_indices.push_back(left);
      }

    }
    return anagram_start_indices;

  }
};

```

# Step2

## 他の人のPRを見る

* https://github.com/huyfififi/coding-challenges/pull/62
    * `p`や`s`は英語小文字のみなので、長さ26の配列を用意すれば十分だった。

## Code2-2

```cpp
#include <vector>
#include <string>



class Solution {
public:
  std::vector<int> findAnagrams(std::string s, std::string p) {
    if (s.size() < p.size()) {
      return {};
    }
    int num_alphabets = 26;
    std::vector<int> char_count_in_p(num_alphabets, 0);
    std::vector<int> char_count_in_window(num_alphabets, 0);
    for (int i = 0; i < p.size(); i++) {
      char_count_in_p[p[i] - 'a'] += 1;
      char_count_in_window[s[i] - 'a'] += 1;
    }

    std::vector<int> start_indices;
    for (int left = 0; left + p.size() <= s.size(); left++) {
      if (char_count_in_window == char_count_in_p) {
        start_indices.push_back((left));
      }
      char_count_in_window[s[left] - 'a'] -= 1;
      int right = left + p.size();
      if (right < s.size()) {
        char_count_in_window[s[right] - 'a'] += 1;
      }
    }
    return start_indices;

    }
};
```


# Step3

## Code3-1

```cpp
#include <vector>
#include <string>

const int NUM_ALPHABETS(26);

class Solution {
public:
  std::vector<int> findAnagrams(std::string s, std::string p) {
    if (s.size() < p.size()) {
      return {};
    }
    std::vector<int> char_count_in_p(NUM_ALPHABETS, 0);
    std::vector<int> char_count_in_window(NUM_ALPHABETS, 0);

    for (int i = 0; i < p.size(); i++) {
      char_count_in_p[p[i] - 'a'] += 1;
      char_count_in_window[s[i] - 'a'] += 1;
    }

    std::vector<int> start_indices;
    for (int left = 0; left + p.size() <= s.size(); left++) {
      if (char_count_in_window == char_count_in_p) {
        start_indices.push_back(left);
      }
      char_count_in_window[s[left] - 'a'] -= 1;
      int right = left + p.size();
      if (right < s.size()) {
        char_count_in_window[s[right] - 'a'] += 1;
      }
    }
    return start_indices;

    }
};

```
