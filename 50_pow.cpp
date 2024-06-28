#include <unordered_map>
class Solution {
public:
  double calcPow(double x, long n, std::unordered_map<long, double> &mem) {
    auto findRes = mem.find(n);
    if (findRes != mem.end()) {
      return findRes->second;
    }
    if (n == 0){
      return 1.0;
    }
    if (n == 1){
      return x;
    }
    unsigned int halfN = n / 2;
    unsigned int remainN = n % 2;
    double result = calcPow(x, halfN, mem) * calcPow(x, halfN, mem) *
                    (remainN == 0 ? 1 : x);
    mem[n] = result;
    return result;
  }
  double myPow(double x, int n) {
    std::unordered_map<long,double> mem;
    long nl = (long) n;
    double res = n > 0 ? calcPow(x, nl, mem) : 1 / calcPow(x, -nl, mem);
    return res;
  }
};

int main(int argc, char *argv[]) {
  double x = 2;
  double n = 5;
  Solution solution;
  solution.myPow(x, n);
  return 0;
}
