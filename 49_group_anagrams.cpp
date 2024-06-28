
#include <algorithm>
#include <iterator>
#include <unordered_map>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
      unordered_map<string, vector<string>> anagrams;

      for (string str : strs){
        string copy = str;
        sort(copy.begin(), copy.end());
        vector<string> anagram = anagrams[copy];
        anagram.push_back(str);
        anagrams[copy] = anagram;
      }

      vector<vector<string>> result;
      for (auto i = anagrams.begin(); i != anagrams.end(); i++){
        result.push_back(i->second);
      }
      return result;
    }
};

int main (int argc, char *argv[]) {
  vector<string> strs{"eat","tea","tan","ate","nat","bat"};
  // string str;
  // while(cin >> str)  {
  //   strs.push_back(str);
  // }

  Solution solution;
  vector<vector<string>> result = solution.groupAnagrams(strs);
  return 0;
}
