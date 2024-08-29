#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution
{
public:
    string longestCommonPrefix(vector<string> &strs)
    {
        int i = 0;
        for (; i < strs[0].size(); i++)
        {
            char opt = strs[0][i];
            for (string str : strs)
            {
                if (i >= str.size() || str[i] != opt)
                {
                    return strs[0].substr(0, i);
                }
            }
        }
        return strs[0];
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    vector<string> strs = {"dog","racecar","car"};
    cout << s.longestCommonPrefix(strs) << endl;
    return 0;
}
