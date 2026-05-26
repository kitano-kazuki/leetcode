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
