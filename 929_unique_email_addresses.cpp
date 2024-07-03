#include <algorithm>
#include <iostream>
#include <set>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
  // NOTE: My solution

  // int numUniqueEmails(vector<string> &emails) {
  //   set<string> uniqueAddresses;
  //   for (string email : emails) {
  //     int atPos = email.find('@');
  //     string localName = email.substr(0, atPos);
  //     string domainName = email.substr(atPos + 1);
  //     cout << "===" << email << "===" << endl;
  //     int plusPos = localName.find('+');
  //     if (plusPos != string::npos) {
  //       localName = localName.substr(0, plusPos);
  //     }
  //     auto iter = remove(localName.begin(), localName.end(), '.');
  //     localName.erase(iter, localName.end());
  //     cout << localName << endl;
  //     uniqueAddresses.insert(localName + "@" + domainName);
  //   }
  //   return uniqueAddresses.size();
  // }
  
  // NOTE: Good Solution
  int numUniqueEmails(vector<string> &emails) {
    unordered_set<string> us;
    for(string &email: emails){
      string cleanEmail = "";
      for(char c : email){
        if(c == '@' || c == '+') break;
        if(c == '.') continue;
        cleanEmail += c;
      }
      us.insert(cleanEmail + email.substr(email.find('@')));
    }
    return us.size();
  }
};
