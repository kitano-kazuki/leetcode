#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        if(numRows == 1){
            return s;
        }
        string answer = "";
        vector<vector<char>> result;
        for(int i = 0; i < numRows; i++){
            vector<char> v;
            result.push_back(v);
        }
        int row = 0;
        bool isDown = true;
        for(int i = 0; i < s.size(); i++){
            result[row].push_back(s[i]);
            if(isDown){
                if(row == numRows - 1){
                    row--;
                    isDown = false;
                }else{
                    row++;
                }
            }else{
                if(row == 0){
                    row++;
                    isDown = true;
                }else{
                    row--;
                }
            }
        }

        for(int i = 0; i < numRows; i++){
            for(int j = 0; j < result[i].size(); j++){
                answer += result[i][j];
            }
        }
        return answer;
    }
};

int main(int argc, char const *argv[])
{
    Solution s;
    cout << s.convert("PAYPALISHIRING", 3) << endl;
    return 0;
}
