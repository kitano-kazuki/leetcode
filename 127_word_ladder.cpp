#include <algorithm>
#include <iostream>
#include <iterator>
#include <queue>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  int ladderLength(string beginWord, string endWord, vector<string> &wordList) {
    wordList.insert(wordList.begin(), beginWord);
    auto endIter = find(wordList.begin(), wordList.end(), endWord);
    if (endIter == wordList.end()) {
      return 0;
    }
    int endIdx = distance(wordList.begin(), endIter);
    queue<int> q;
    vector<int> visited;

    q.push(0);
    int depth = 0;
    while (!q.empty()) {
      depth++;
      int qLen = q.size();
      for (int i = 0; i < qLen; i++) {
        int target = q.front();
        q.pop();
        if (target == endIdx) {
          return depth;
        }
        visited.push_back(target);
        for (int j = 0; j < beginWord.length(); j++) {
          for (int k = 'a'; k <= 'z'; k++) {
            string cp = wordList[target];
            cp[j] = (char)k;
            auto iter = find(wordList.begin(), wordList.end(), cp);
            if (iter != wordList.end()) {
              int idx = distance(wordList.begin(), iter);
              if (find(visited.begin(), visited.end(), idx) == visited.end()) {
                q.push(idx);
              }
            }
          }
        }
      }
    }
    return 0;
  }
};

int main(int argc, char *argv[]) {
  Solution solution;
  string beginWord = "hit";
  string endWord = "cog";
  vector<string> wordList = {"hot", "dot", "dog", "lot", "log", "cog"};
  int res = solution.ladderLength(beginWord, endWord, wordList);
  cout << res << endl;
  return 0;
}
