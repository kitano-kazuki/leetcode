# Step1

## アプローチ

* `board`が与えられて、その中に目当ての`word`があるかどうかを判定する。
* 最も単純な方法
    * `word`中の今見ている文字の場所を記録しておく
    * `board`中のp今見ている場所も記録しておく
    * 上記二つが一致していたら、隣接するセルのうち、まだ訪れていない部分について、同様に確かめる
    * 計算量/実行時間
        * GridをM * Nとする。
        * 確かめたい文字列の長さをLとする。
        * 今回はm, nともに <= 6である
        * L <= 15である
        * 探索する必要のある経路の数
            * M * N * 4 * 3^(L - 1)
        * 実行時間
            * 6 * 6 * 4 * 3^14 / 10^7 ~= 10^2 sec
    * ギリギリ終わらないくらいな気がする.
        * Pythonだったら余裕で無理かな
    * 他に方法も思いつかないのでこれで実装

## Code1-1

* TLEになるかと思ったがACだった.

```cpp
#include <utility>
#include <vector>
#include <string>
#include <set>


const std::vector<std::pair<int, int>> DIRECTIONS = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

class Solution {
public:
    bool exist(std::vector<std::vector<char>>& board, std::string word) {
      if (board.empty()) {
        return false;
      }
      for (int row = 0; row < board.size(); row++) {
        for (int col = 0; col < board[0].size(); col++) {
          std::set<std::pair<int, int>> visited;
          if (explore(board, row, col, word, 0, visited)) {
            return true;
          }
        }
      }
      return false;
    }

private:
    bool explore(const std::vector<std::vector<char>>& board, int row, int col, const std::string& word, int word_i, std::set<std::pair<int, int>>& visited) {
      if (word_i == word.size()) {
        return true;
      }
      if (!(0 <= row && row < board.size()) || !(0 <= col && col < board[0].size())) {
        return false;
      }
      if (visited.find(std::make_pair(row, col)) != visited.end()) {
        return false;
      }
      if (board[row][col] != word[word_i]) {
        return false;
      }
      visited.emplace(std::make_pair(row, col));
      for (const auto& [dr, dc] : DIRECTIONS) {
        int next_row = row + dr;
        int next_col = col + dc;
        if (explore(board, next_row, next_col, word, word_i + 1, visited)) {
          return true;
        }
      }
      visited.erase(std::make_pair(row, col));
      return false;
    }

};

```

# Step2

## Code2-1

* `pair`の構築にlist_initializerを使うように変更


```cpp
#include <utility>
#include <vector>
#include <string>
#include <set>


const std::vector<std::pair<int, int>> DIRECTIONS = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

class Solution {
public:
    bool exist(std::vector<std::vector<char>>& board, std::string word) {
      if (board.empty()) {
        return false;
      }
      for (int row = 0; row < board.size(); row++) {
        for (int col = 0; col < board[0].size(); col++) {
          std::set<std::pair<int, int>> visited;
          if (explore(board, row, col, word, 0, visited)) {
            return true;
          }
        }
      }
      return false;
    }

private:
    bool explore(const std::vector<std::vector<char>>& board, int row, int col, const std::string& word, int word_i, std::set<std::pair<int, int>>& visited) {
      if (word_i == word.size()) {
        return true;
      }
      if (!(0 <= row && row < board.size()) || !(0 <= col && col < board[0].size())) {
        return false;
      }
      if (board[row][col] != word[word_i]) {
        return false;
      }
      if (visited.find({row, col}) != visited.end()) {
        return false;
      }
      visited.emplace(row, col);
      for (const auto& [dr, dc] : DIRECTIONS) {
        int next_row = row + dr;
        int next_col = col + dc;
        if (explore(board, next_row, next_col, word, word_i + 1, visited)) {
          return true;
        }
      }
      visited.erase({row, col});
      return false;
    }

};

```

## 他の人のPRを見る

* https://github.com/huyfififi/coding-challenges/pull/61
    * 最初の計算量の見積もりや方針の立て方はだいたい一緒だった.
    * 実行時間に関しても100secくらいかかりそうと考えている。
    * 自分のコードでは`exist`のなかでループ中に`visited`を都度定義している.
        * これは無駄が多い
        * `explore`は呼び出しが終わると`visited`を(falseだった場合)元の状態に戻すので, 最初に一度だけ定義すれば十分.
    * 二つの定数倍の効率化を行っていた
        * ボード中の文字数が探したい`word`の文字数よりも少なければ`false`を直ちに返す.
        * 先頭からよりも末尾から捜査した方が効率的になりそうなら文字列をひっくり返す
* https://github.com/thonda28/leetcode/pull/14
    * `visited`を持つ代わりに, `board`に`#`を代入している
        * 空間計算量をおさえることができる
        * `board[row][col] != word[i]`となるので, 訪れている場所は弾かれる
        * ただ初見でパッと見た時はわかりにくいかも
    * `iterative`にやる方法も実装している

# Step3

## Code3-1

```cpp
#include <utility>
#include <vector>
#include <string>
#include <set>


const std::vector<std::pair<int, int>> DIRECTIONS = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

class Solution {
public:
    bool exist(std::vector<std::vector<char>>& board, std::string word) {
      std::set<std::pair<int, int>> visited;
      for (int row = 0; row < board.size(); row++) {
        for (int col = 0; col < board[0].size(); col++) {
          if (explore(board, row, col, word, 0, visited)) {
            return true;
          }
        }
      }
      return false;
    }

private:
    bool explore(
        const std::vector<std::vector<char>>& board,
        int row,
        int col,
        const std::string& word,
        int word_i,
        std::set<std::pair<int, int>>& visited
    ) {
      if (word_i == word.size()) {
        return true;
      }
      if (!(0 <= row && row < board.size() && 0 <= col & col < board[0].size())) {
        return false;
      }
      if (visited.find({row, col}) != visited.end()) {
        return false;
      }
      if (board[row][col] != word[word_i]) {
        return false;
      }

      visited.emplace(row, col);
      for (const auto& [dr, dc] : DIRECTIONS) {
        int next_row = row + dr;
        int next_col = col + dc;
        if (explore(board, next_row, next_col, word, word_i + 1, visited)) {
          return true;
        }
      }
      visited.erase({row, col});

      return false;
    }

};

```
