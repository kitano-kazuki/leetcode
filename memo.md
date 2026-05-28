# Step1

## アプローチ

* LRUキャッシュの拡張
* 最も使用されていないものを削除. 同一順位だった場合は, LRUの挙動
* どうやって, 使用された数をカウントして, それの最も低いものを保持するか?
* 使われた回数が少ない順に集合sをキューに追加
* 集合`s_i`は, `i`回使用されたキーの集合
* キーごとに, どの`s_i`に属しているか`dict`に保存しておく
* アクセスがあると`dict`を参照して, そのキー`x`がある`s_i`を特定
* `s_i`から`x`を削除, `s_i+1`に`x`を追加. `dict`の`x`に対する値を`i + 1`に更新
* `s_i`内は本当は, 使用された順序が保持されていると嬉しい
    * 同一の`s_i`内で順序が変わることはない.
    * 使われると`s_i+1`に移動するため
* `s_i`は集合ではなくて, `queue`構造を持てばよさそう
* `queue`だとすると, 途中に入っていた要素を削除するのが大変
    * `linkedlist`にした方がいい
    * 末尾にもアクセスしたいから`double linked list`にするべき
* かつ, 現在の要素数もtrackしたい
* かつ, 最も使用されていない要素を持つ集合を知りたい
* `s_i`自体は, stackで管理がいい？
    * 新しいものが上に来る(使用された回数がすくない)
    * `s_i`の要素が無くなった時に, それを`pop`するようにしたい
* ここまで15分

## Code1-1

* AC: 39:18
* 最初に書いたコードでバグなく実装できていて嬉しかった
    * 最初の提出からの変更点は二箇所のみ
        * `del self.key_to_frequency[key]` -> `del self.key_to_frequency[least_key]`
        * `self.update_usage(key)` -> `self._update_usage(key)`

```python
import collections


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.key_to_frequency = {}
        self.key_to_value = {}
        self.frequency_to_key_chunks = collections.OrderedDict()
        self.least_frequency = 0

    def _update_usage(self, key: int) -> None:
        frequency = self.key_to_frequency[key]
        key_chunks = self.frequency_to_key_chunks[frequency]

        del key_chunks[key]

        # frequency回使用されたキー集合の中身がなくなった
        if len(key_chunks) == 0:
            del self.frequency_to_key_chunks[frequency]
            if frequency == self.least_frequency:
                self.least_frequency += 1

        # frequency + 1回使用されたキー集合にkeyを追加
        if frequency + 1 not in self.frequency_to_key_chunks:
            self.frequency_to_key_chunks[frequency + 1] = collections.OrderedDict()
        new_key_chunks = self.frequency_to_key_chunks[frequency + 1]
        new_key_chunks[key] = True
        self.key_to_frequency[key] = frequency + 1

        return

    def get(self, key: int) -> int:
        if key not in self.key_to_value:
            return -1

        value = self.key_to_value[key]

        self._update_usage(key)

        return value


    def put(self, key: int, value: int) -> None:
        # キーを更新
        if key in self.key_to_value:
            self.key_to_value[key] = value
            self._update_usage(key)
            return

        # 最も使用頻度が低く, 最近使われていないキーを削除
        if self.size >= self.capacity:
            least_key_chunk = self.frequency_to_key_chunks[self.least_frequency]
            least_key, _ = least_key_chunk.popitem(last=False)
            if len(least_key_chunk) == 0:
                del self.frequency_to_key_chunks[self.least_frequency]
            self.size -= 1
            del self.key_to_frequency[least_key]
            del self.key_to_value[least_key]
        
        # キーを追加
        self.least_frequency = 1
        self.key_to_frequency[key] = self.least_frequency
        self.key_to_value[key] = value
        self.size += 1
        if self.least_frequency not in self.frequency_to_key_chunks:
            self.frequency_to_key_chunks[self.least_frequency] = collections.OrderedDict()
        key_chunk = self.frequency_to_key_chunks[self.least_frequency]
        key_chunk[key] = True

        return

```

# Step2


以下に記した小田さんのコメントとnodaさんの実装を参考にもうちょと読みやすくしてみる

---

```
struct Node {
  int key;
  int value;
  int freqency;
};
std::unordered_map<int, std::list<Node>> freq_to_nodes_;
std::unordered_map<int, std::list<Node>::iterator> key_to_iter_;
```

でもいけますか。これだと、最小の頻度が追い出されてなくなった時に次の頻度を計算するのが難しそうなのですが、それは実は必ず1です。

---

## Code2-1

* `Node`が`key`, `value`, `frequency`をもつ
* ある`key`の使用回数が増えた時
    * `key_to_node`で対応したいもの
        * その`key`を持つ`Node`が欲しい
    * `frequency_to_nodes`で対応したいもの
        * その`Node`の`frequency`と同じ回数使われたノードのリストが欲しい
        * その`frequency`に`+1`した回数使われたノードのリストが欲しい

```python
from collections import OrderedDict


class Node:
    def __init__(self, key, value, frequency):
        self.key = key
        self.value = value
        self.frequency = frequency


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.least_frequency = 0
        self.freq_to_nodes : dict[int, OrderedDict[Node, bool]] = {}
        self.key_to_node : dict[str, Node] = {}


    def _increment_frequency(self, key: int) -> None:
        node = self.key_to_node[key]
        freq = node.frequency
        new_freq = freq + 1

        nodes_in_freq = self.freq_to_nodes[freq]

        del nodes_in_freq[node]
        if not nodes_in_freq:
            del self.freq_to_nodes[freq]
            if freq == self.least_frequency:
                self.least_frequency = new_freq

        node.frequency = new_freq
        if new_freq not in self.freq_to_nodes:
            self.freq_to_nodes[new_freq] = OrderedDict()
        self.freq_to_nodes[new_freq][node] = True

        return

    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        self._increment_frequency(key)

        return self.key_to_node[key].value


    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            self._increment_frequency(key)
            self.key_to_node[key].value = value
            return

        self.size += 1

        if self.size > self.capacity:
            self.size -= 1
            nodes_in_least_freq = self.freq_to_nodes[self.least_frequency]
            node_deleted, _ = nodes_in_least_freq.popitem(last=False)
            if not nodes_in_least_freq:
                del self.freq_to_nodes[self.least_frequency]
            del self.key_to_node[node_deleted.key]
        
        self.least_frequency = 1
        node = Node(key, value, 1)
        self.key_to_node[key] = node
        if 1 not in self.freq_to_nodes:
            self.freq_to_nodes[1] = OrderedDict()
        self.freq_to_nodes[1][node] = True

        return

```
