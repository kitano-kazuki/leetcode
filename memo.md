# Step1

## アプローチ

* `0`, `1`, `2`からなる配列`nums`が与えられる.
* それらが`0`,`1`,`2`の順番に並ぶようにin-placeで並び替えを行う
* 一番単純な方法は,`0`,`1`,`2`の登場回数を記録するために最初に配列を全部見る
* その後に, もう一度配列を先頭から見ていき値を書き換える
* quicksortを２回やることでも解けそう
    * 1回目: 前半が`0`,`1`, 後半が`2`
    * 2回目: 前半の前半が`0`, 前半の後半が`1`
* 2は後ろに配置, 0は前に配置. 先頭と末尾それぞれで, 1が置かれ始める境界を記録しておく

## Code1-1

* `zero_place_index`より左側は`0`であることが確定している
* `two_place_index`より右側は`2`であることが確定している
* `i`は今調べたい場所を表している
* `zero_place_index <= j < i`は`1`であることが確定している

```cpp
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
      if (nums.empty()){
        return;
      }
      int zero_place_index = 0;
      int two_place_index = nums.size() - 1;
      int i = 0;
      while (i <= two_place_index) {
        int num = nums[i];
        if (num == 0){
          swap(nums[i], nums[zero_place_index]);
          zero_place_index++;
          i++;
          continue;
        }
        if (num == 1){
          i++;
          continue;
        }
        if (num == 2){
          swap(nums[i], nums[two_place_index]);
          two_place_index--;
          continue;
        }
      }
    }
};


```

# Step2

## Code2-1

* 変更なし

```cpp
#include <utility>
#include <vector>

using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
      if (nums.empty()){
        return;
      }
      int zero_place_index = 0;
      int two_place_index = nums.size() - 1;
      int i = 0;
      while (i <= two_place_index) {
        int num = nums[i];
        if (num == 0){
          swap(nums[i], nums[zero_place_index]);
          zero_place_index++;
          i++;
          continue;
        }
        if (num == 1){
          i++;
          continue;
        }
        if (num == 2){
          swap(nums[i], nums[two_place_index]);
          two_place_index--;
          continue;
        }
      }
    }
};


```

## 他の人のPRを見る

* https://github.com/huyfififi/coding-challenges/pull/49
    * `step1`の実装と同じ
    * コメントより
        * > 四色だったらどうしますか？という質問をしそうです。三色という設問が良いですね。

# Step3

## Code3-1

```cpp
#include <vector>
#include <utility>

class Solution {
public:
    void sortColors(vector<int>& nums) {
      int zero_place_index = 0;
      int two_place_index = nums.size() - 1;
      int i = 0;
      while (i <= two_place_index){
        if (nums[i] == 1){
          i++;
          continue;
        }
        if (nums[i] == 0){
          swap(nums[i], nums[zero_place_index]);
          zero_place_index++;
          i++;
          continue;
        }
        if (nums[i] == 2){
          swap(nums[i], nums[two_place_index]);
          two_place_index--;
          continue;
        }
      }
    }
};

```
