# Step1

## アプローチ

* 二分木をシリアライズ/デシリアライズするアルゴリズムを考える.
* `inorder`と`preorder`をそれぞれ保存しておけば, 復元することはできる
    * でも, ちょっと冗長な感じもする
* `TreeNode`を何かしらの形でSerializeすれば, 再帰的にDeerializeすることもできそう

## Code1-1

* `position`として現在までに読んだ位置を保存しておく. 再帰関数の呼び出しで共通してそれを更新する.

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include <cstddef>
#include <functional>


 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 };

class Codec {
public:

  std::string serialize(TreeNode* root) {
    if (root == NULL) {
      return "n";
    }
    std::string val_serialized = std::to_string(root->val);
    std::string left_serialized = serialize(root->left);
    std::string right_serialized = serialize(root->right);
    return "(" + val_serialized + "," + left_serialized + "," + right_serialized + ")";
  }

  TreeNode* deserialize(std::string data) {
    int position = 0;
    std::function<TreeNode*(void)> deserialize_with_position = [&]() -> TreeNode* {

      if (data[position] == 'n') {
        position++;
        return NULL;
      }

      // read "("
      position++;


      // read val
      int val = 0;
      int sign = 1;
      if (data[position] == '-') {
        sign = -1;
        position++;
      }
      while (data[position] != ',') {
        val = val * 10 + (data[position] - '0');
        position++;
      }
      val = val * sign;

      // read ","
      position++;

      TreeNode* left_root = deserialize_with_position();

      // read ","
      position++;

      TreeNode* right_root = deserialize_with_position();

      // read ")"
      position++;

      TreeNode* deserialized_root = new TreeNode(val);
      deserialized_root->left = left_root;
      deserialized_root->right = right_root;

      return deserialized_root;
    };

    return deserialize_with_position();

  }
};


```

# Step2

## 他の人のPRをみる

* https://github.com/tom4649/Coding/pull/125
    * step3のコード
        * pre-orderで訪れた値を保存しておく
        * deserializeでもpre-orderで順番に復元する
* https://github.com/hayashi-ay/leetcode/pull/74
    * > serializeとdeserializeがほぼ同じ見た目になると分かりやすいのではないかと感じました。
        * これは確かにと思った.
* `NULL`を表す文字をserializeしておけば, pre-orderやpost-orderのみでdeserializeすることが可能
* 再帰でもループでもかける. BFSはやや煩雑なのでDFSが想定解っぽい
    * > BFS 版は DFS 版に比べて、やや煩雑に感じました。おそらく DFS 版が想定解なのではないかと思います。


## Code2-2 (using stream)

* `istringstream`の`>>`オペレータは, 空白を無視して値を読み取る.
* `ostringstream`でserializeするときに空白を入れておくことで, 上記の特徴を生かせる
* C++のスタイルガイドに, ラムダ式はキャプチャするものを明示した方が良いと書いてあったので明示した.
    * 再帰関数の場合もそうなのかはあまり自信がないが。。。
    * つまり, `std::function`を使用して, キャプチャに`[&]`を使う方が見やすい可能性もあると思った.
* `istringstream`からのキャプチャで`int`として統一的に表したかったので, NO_NODEを表すものを`INT`
の上限値にした.
    * ノードの値の範囲によっては今回の実装が意図通りに動かない可能性があることは認識している
    * ただ、一度 stringで受け取って, それが"NULl"や"#"などでないか比較して、そうでなかったらintにキャストして。。。とやるほうが冗長で醜くなると思った.

```cpp
#include <cstddef>
#include <limits>
#include <sstream>
#include <string>
#include <functional>


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};


constexpr int NO_NODE = std::numeric_limits<int>::max();


class Codec {
public:

  std::string serialize(TreeNode* root) {
    std::ostringstream oss;

    auto write_value_to_stream = [&oss](auto self, TreeNode* node) -> void {
      if (node == NULL) {
        oss << NO_NODE << " ";
        return;
      }
      oss << node->val << " ";
      self(self, node->left);
      self(self, node->right);
    };

    write_value_to_stream(write_value_to_stream, root);
    return oss.str();
  }

  TreeNode* deserialize(std::string data) {
    std::istringstream iss(data);

    auto read_value_from_stream = [&iss](auto self) -> TreeNode* {
      int value;
      iss >> value;
      if (value == NO_NODE) {
        return NULL;
      }
      TreeNode* node = new TreeNode(value);
      node->left = self(self);
      node->right = self(self);
      return node;
    };

    return read_value_from_stream(read_value_from_stream);
  }
};

```

# Step3

## Code3-2 (using stream)

```cpp
#include <limits>
#include <sstream>
#include <string>


constexpr int NO_NODE = std::numeric_limits<int>::max();


class Codec {
public:

  std::string serialize(TreeNode* root) {
    std::ostringstream oss;

    auto write_to_stream = [&oss](auto self, TreeNode* node) -> void {
      if (node == NULL) {
        oss << NO_NODE << " ";
        return;
      }
      oss << node->val << " ";
      self(self, node->left);
      self(self, node->right);
    };

    write_to_stream(write_to_stream, root);
    return oss.str();
  }

  TreeNode* deserialize(std::string data) {
    std::istringstream iss(data);

    auto read_from_stream = [&iss](auto self) -> TreeNode* {
      int val;
      iss >> val;
      if (val == NO_NODE) {
        return NULL;
      }

      TreeNode* node = new TreeNode(val);
      node->left = self(self);
      node->right = self(self);
      return node;
    };

    return read_from_stream(read_from_stream);
  }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));

```
