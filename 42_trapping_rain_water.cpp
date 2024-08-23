#include <vector>
#include <iostream>


using namespace std;

class Solution
{
public:
    int trap(vector<int> &height)
    {
        int n = height.size();
        if (n == 1)
        {
            return 0;
        }
        int capacity = 0;
        int left = 0;
        int right = 1;

        while (right < n)
        {
            int minus = 0;
            while (height[left] > height[right] && height[left] >= 0)
            {
                if (right == n - 1)
                {
                    height[left]--;
                    right = left + 1;
                    minus = 0;
                    continue;
                }
                minus += height[right];
                right++;
            }
            capacity += height[left] * (right - left - 1) - minus;
            left = right;
            right = left + 1;
        }
        return capacity;
    }
}
;

int main(int argc, char const *argv[])
{
    Solution s;
    vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
    int result = s.trap(height);
    cout << result << endl;
    return 0;
}
