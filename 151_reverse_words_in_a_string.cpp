#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution
{
public:
    string reverseWords(string s)
    {
        int n = s.size();
        string result;
        bool isFirst = true;
        int start = n - 1;
        int end = n - 1;
        while (end >= 0 && start >= 0)
        {
            while (end >= 0 && s[end] == ' ')
            {
                end--;
            }
            start = end;
            while (start >= 0 && s[start] != ' ')
            {
                start--;
            }
            if(end < 0){
                break;
            }
            if (isFirst)
            {
                result = s.substr(start + 1, end - start);
                isFirst = false;
            }
            else
            {
                result = result + " " + s.substr(start + 1, end - start);
            }
            end = start;
        }
        return result;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    cout << s.reverseWords("a good   example") << endl;
    return 0;
}
