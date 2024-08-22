#include <vector>
#include <iostream>

#define DEBUG true

using namespace std;

class Solution
{
public:
    int candy(vector<int> &ratings)
    {
        int n = ratings.size();
        vector<int> distribution(n, 1);
        for (int i = 1; i < n; i++)
        {
            if (ratings[i] > ratings[i - 1])
            {
                distribution[i] = distribution[i - 1] + 1;
            }
        }
        for (int i = n - 2; i >= 0; i--)
        {
            if (ratings[i] > ratings[i + 1])
            {
                distribution[i] = max(distribution[i], distribution[i + 1] + 1);
            }
        }
        int answer = 0;
        for (int i = 0; i < n; i++)
        {
            answer += distribution[i];
        }
        return answer;
    }
};

main(int argc, char const *argv[])
{
    Solution s;
    vector<int> ratings = {1, 0, 2};
    int result = s.candy(ratings);
    cout << result << endl;
    return 0;
}
