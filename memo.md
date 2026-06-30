# Step1

## アプローチ

* digitsが与えられた時にそれでできる英字の組み合わせをすべて列挙する
* 再帰的に処理していきたい
* 自分の仕事は、`digit`から作れる文字列全てを作って、部下の作った文字列の先頭に加えること
* 部下への仕事の引き継ぎでは、次に処理するべき`digit`の位置を教える.
* 計算量は、表せる文字列の種類分だからO(3^N)
* N <= 4より、実行時間は81 / 10^7 ~= 10^-5程度

## Code1-1

```cpp
#include <string>
#include <unordered_map>
#include <vector>


const std::unordered_map<char, std::vector<char>> DIGIT_TO_LETTERS = {
  {'2', {'a', 'b', 'c'}},
  {'3', {'d', 'e', 'f'}},
  {'4', {'g', 'h', 'i'}},
  {'5', {'j', 'k', 'l'}},
  {'6', {'m', 'n', 'o'}},
  {'7', {'p', 'q', 'r', 's'}},
  {'8', {'t', 'u', 'v'}},
  {'9', {'w', 'x', 'y', 'z'}}
};


class Solution {
public:
  std::vector<std::string> letterCombinations(std::string digits) {
    return LetterCombinations(digits, 0);
    }

private:
    std::vector<std::string> LetterCombinations(const std::string& digits, int i) {
      if (i == digits.size()) {
        return {""};
      }
      std::vector<std::string> combinations;
      std::vector<std::string> child_combinations = LetterCombinations(digits, i + 1);
      for (char letter : DIGIT_TO_LETTERS.at(digits[i])) {
        for (std::string child_combination : child_combinations) {
          combinations.push_back(letter + child_combination);
        }
      }
      return combinations;
    }

};


```

# Step2

## Code2-1

* `push_back`は`vector`の中に新しい要素をコピーして作る操作
    * https://cpprefjp.github.io/reference/vector/vector/push_back.html
* 右辺値と左辺値について
    * https://cpprefjp.github.io/lang/cpp11/rvalue_ref_and_move_semantics.html

```cpp

#include <string>
#include <unordered_map>
#include <vector>


const std::unordered_map<char, std::vector<char>> DIGIT_TO_LETTERS = {
  {'2', {'a', 'b', 'c'}},
  {'3', {'d', 'e', 'f'}},
  {'4', {'g', 'h', 'i'}},
  {'5', {'j', 'k', 'l'}},
  {'6', {'m', 'n', 'o'}},
  {'7', {'p', 'q', 'r', 's'}},
  {'8', {'t', 'u', 'v'}},
  {'9', {'w', 'x', 'y', 'z'}}
};


class Solution {
public:
  std::vector<std::string> letterCombinations(std::string digits) {
    std::vector<std::string> result;
    std::string processing_string = "";
    GenerateLetterCombinations(digits, 0, processing_string, result);
    return result;
    }

private:
  void GenerateLetterCombinations(const std::string& digits, int index, std::string& processing_string, std::vector<std::string>& result) {
    if (index == digits.size()) {
      result.push_back(processing_string);
      return;
    }
    for (const char& letter : DIGIT_TO_LETTERS.at(digits[index])) {
      processing_string.push_back(letter);
      GenerateLetterCombinations(digits, index + 1, processing_string, result);
      processing_string.pop_back();
    }
  }

};
```


## 他の人のPRを見る

* https://github.com/tom4649/Coding/pull/71
    * step3はbacktrackで行っている。メモリの効率性を考えるとbacktrackが解法として良さそう。
* https://github.com/huyfififi/coding-challenges/pull/60
    * cppでの再帰的なやり方の代わりにwhileループを使ってiterativeに実装している。

# Step3

## Code3-1

```cpp
#include <string>
#include <unordered_map>
#include <vector>


const std::unordered_map<char, std::vector<char>> DIGIT_TO_LETTERS = {
  {'2', {'a', 'b', 'c'}},
  {'3', {'d', 'e', 'f'}},
  {'4', {'g', 'h', 'i'}},
  {'5', {'j', 'k', 'l'}},
  {'6', {'m', 'n', 'o'}},
  {'7', {'p', 'q', 'r', 's'}},
  {'8', {'t', 'u', 'v'}},
  {'9', {'w', 'x', 'y', 'z'}}
};


class Solution {
public:
  std::vector<std::string> letterCombinations(std::string digits) {
    std::vector<std::string> result;
    std::string processing_string = "";
    GenerateLetterCombinations(digits, 0, processing_string, result);
    return result;
    }

private:
  void GenerateLetterCombinations(const std::string& digits, int index, std::string& processing_string, std::vector<std::string>& result) {
    if (index == digits.size()) {
      result.push_back(processing_string);
      return;
    }
    for (const char& letter : DIGIT_TO_LETTERS.at(digits[index])) {
      processing_string.push_back(letter);
      GenerateLetterCombinations(digits,index + 1, processing_string, result);
      processing_string.pop_back();
    }


  }

};

```
