# Step1

## アプローチ

* `nums`の要素を二つに分けて, それらの和が等しくできるなら`True`, そうでないなら`False`を返す
* すべてのパターンを試すとすると絶対に1secでは終わらない
    * パターン数: `200C100`
* 合計値が奇数だと`False`
* 合計値が偶数でも`5,3`みたいなものは`False`
* 合計が`total / 2`となる組み合わせが存在すればいい
* わからなかったので, ヒントを確認した
    * DPを使って, 特定の和になるパターンが存在するかを見る
* 作りたい値`x`について
    * `x - num`を作れるか判定する
* `x - num`の候補は, 最大の場合で, 100通り
* それぞれについて, `nums`の長さ分パターンを見る
* `nums.size() == N`
* `nums[i] <= M`
* 計算量: O(N * M)
* 実行時間: 100 * 200 / 10^7 ~= 10^-3 sec

## Code1-1

* DPの構成方法がわからなくて調べた
* `nums`中のあるインデックス`i`までを使って作れるかどうか調べるのを繰り返すとする
* `i - 1`までを使って作れるかどうかは調べられているものとする
* 各数字について, `nums[i]`を引いた値が作れるなら`i`までの数字を使って作れることになる

```cpp
#include <numeric>
#include <set>
#include <vector>
#include <optional>

using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
      int total = accumulate(nums.begin(), nums.end(), 0);
      if (total % 2 == 1){
        return false;
      }
      int target = total / 2;

      vector<bool> makables(target + 1, false);
      makables[0] = true;

      for (int num : nums){
        for (int sum = target; sum >= 0; sum--){
          if (sum - num < 0) {
            continue;
          }
          if (makables[sum - num]){
            makables[sum] = true;
          }
        }
      }

      return makables[target];
    }
};

```

# Step2

## Code2-1

* 変更なし

```cpp
#include <numeric>
#include <set>
#include <vector>
#include <optional>

using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
      int total = accumulate(nums.begin(), nums.end(), 0);
      if (total % 2 == 1){
        return false;
      }
      int target = total / 2;

      vector<bool> makables(target + 1, false);
      makables[0] = true;

      for (int num : nums){
        for (int sum = target; sum >= 0; sum--){
          if (sum - num < 0) {
            continue;
          }
          if (makables[sum - num]){
            makables[sum] = true;
          }
        }
      }

      return makables[target];
    }
};

```

## 他の人のPRを見る

* https://github.com/huyfififi/coding-challenges/pull/51
    * `bool`の代わりに`uint8_t`を使っているが, 方針は同じ

# Step3

## Code3-1

```cpp
#include <numeric>
#include <vector>

using namespace std;

class Solution {
public:
    bool canPartition(vector<int>& nums) {
      int total = accumulate(nums.begin(), nums.end(), 0);
      if (total % 2 == 1){
        return false;
      }

      int target = total / 2;
      vector<bool> makables(target + 1, false);
      makables[0] = true;

      for (int num : nums){
        for (int sum = target; sum >= 0; sum--){
          if (sum - num < 0){
            continue;
          }
          if (makables[sum - num]){
            makables[sum] = true;
          }
        }
      }

      return makables[target];
    }
};

```
