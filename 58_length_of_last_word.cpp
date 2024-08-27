#include <string>
#include <iostream>
using namespace std;

class Solution
{
public:
    int lengthOfLastWord(string s)
    {
        int length = 0;
        for(int i = 0; i < s.size(); i++){
            if(s[i] != ' '){
                if(i > 0 && s[i-1] == ' '){
                    length = 0;
                }
                length++;
            }
        }
        return length;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    cout << s.lengthOfLastWord("luffy is still joyboy") << endl;
    return 0;
}
