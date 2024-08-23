#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution
{
public:
    vector<string> five = {"V", "L", "D"};
    vector<string> one = {"I", "X", "C", "M"};
    string intToRoman(int num)
    {
        string s = "";
        int count = 0;
        while (num > 0)
        {
            int digit = num % 10;
            num /= 10;
            if (digit == 4)
            {
                s = one[count] + five[count] + s;
            }
            else if (digit == 9)
            {
                s = one[count] + one[count + 1] + s;
            }
            else
            {
                string temp = "";
                if (digit >= 5)
                {
                    temp = five[count];
                    digit -= 5;
                }
                for (; digit > 0; digit--)
                {
                    temp += one[count];
                }
                s = temp + s;
            }
            count++;
        }
        return s;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    cout << s.intToRoman(1994) << endl;
    return 0;
}
