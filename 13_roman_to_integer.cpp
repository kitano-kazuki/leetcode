#include <vector>
#include <string>
#include <iostream>


using namespace std;

class Solution
{
public:
    int romanToInt(string s)
    {
        char before;
        int num = 0;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == 'I')
            {
                num += 1;
            }
            else if (s[i] == 'V')
            {
                if (before == 'I')
                {
                    num += 3;
                }
                else
                {

                    num += 5;
                }
            }
            else if (s[i] == 'X')
            {
                if(before == 'I'){
                    num += 8;
                }
                else
                {
                    num += 10;
                }
            }
            else if (s[i] == 'L')
            {
                if(before == 'X'){
                    num += 30;
                }
                else{
                    num += 50;
                }
            }
            else if (s[i] == 'C')
            {
                if(before == 'X'){
                    num += 80;
                }
                else{
                    num += 100;
                }
            }
            else if (s[i] == 'D')
            {
                if(before == 'C'){
                    num += 300;
                }
                else{
                    num += 500;
                }
            }
            else if (s[i] == 'M')
            {
                if(before == 'C'){
                    num += 800;
                }
                else{
                    num += 1000;
                }
            }
            before = s[i];
        }
        return num;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    int res = s.romanToInt("MCMXCIV");
    cout << res << endl;
    return 0;
}
