#include <random>
#include <unordered_map>
#include <vector>

using namespace std;

class RandomizedSet {
public:
  unordered_map<int, int> m;
  vector<int> v;

  RandomizedSet() {}

  bool search(int val) {
    auto iter = m.find(val);
    if (iter != m.end() && iter->second != -1) {
      return true;
    }
    return false;
  }

  bool insert(int val) {
    if (search(val)) {
      return false;
    }
    v.push_back(val);
    m[val] = v.size() - 1;
    return true;
  }

  bool remove(int val) {
    if (!search(val)) {
      return false;
    }
    auto iter = m.find(val);
    int idx = iter->second;
    int lastVal = v.back();
    v[idx] = lastVal;
    m[lastVal] = idx;
    m[val] = -1;
    v.pop_back();
    return true;
  }

  int getRandom() {
    std::mt19937 mt{std::random_device{}()};
    std::uniform_int_distribution<int> dist(0, v.size() - 1);
    int randn = dist(mt);
    return v[randn];
  }
};
