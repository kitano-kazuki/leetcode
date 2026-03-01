# Step1

## アプローチ

* 文字列に出現する文字の種類と回数が一緒のものをグループにしたい
* それぞれの文字の種類ごとにハッシュを作る？例えば`ord()`使ったりして.
* でもそれだと, 違う文字の組み合わせだけど, 同じハッシュになるものが存在する.
* それぞれの文字列をソートしたら, 同じ文字の出現回数と種類にものは同じ文字列に行き着く.
* 感覚的にはあまり効率的じゃなさそうだから一回見積もり
* 文字列をソート
* それを辞書かなんかに保存. (あるいはUnion Find? =>あとで検討)
* 辞書には, ソート後の文字列をキー, 元の文字列の配列を値として保存
* 各文字列(長さm)ごとの処理は, ソートの`O(mlog(m))`と辞書のルックアップの`O(1)`, 該当した配列にappendの`O(1)`.
* それを全部の文字列やる `O(n)`
* 最後に, 辞書から答えを持ってくる
    * これはグループの数だけ, 結果を格納する配列に`append`する.
    * グループの数は最悪の場合で`n`個
* トータル
    * `O(n * m * log(m) + n)`だから`O(n * m * log(m))`
* 検討事項
    * 辞書の代わりに`Union find`を使えるか検討する
    * これより効率的なアルゴリズムがないかもう少し考える
* `Union find`についての検討
    * 二つのノード間（要素間）のエッジの有無をもとにグループ分けできる.
    * 全体のグラフから, 森を抽出するみたいなイメージ
    * 今回はそれぞれが繋がっているか見るために, 全ての組み合わせを見なければいけない？？
        * これには`O(n ^ 2)`かかる
        * この時点で`Union find`は使えなさそう
* 他のアルゴリズムの可能性を検討
    * 無駄がありそうなのは, ソートしている部分. ソートしなくてもグループ分けに使えるkeyを作れないかな.
    * いい感じにハッシュを作る方法はあるか
        * `O(m)`で各文字列ごとに, そこに含まれる文字の種類と個数がわかったら嬉しい.
        * 例えば, `m`は最大でも`100`だから`2^7 - 1`あればいい. `7 bit unsigned`で表現可能
        * 各アルファベットごとに`7bit`を用意. それらを並べて`7 * 26 bit`にすれば, 各アルファベットの種類ごとの個数をまとめたものを一意の数字で表せる
        * でも`7 * 26 bit`って`182 bit`だし, それが, `10^4`個あるとなると, `10^4 * 128 bit`のスペースを使用する.
        * `182 bit`ってどんくらいかな
            * 一つの文字を表すのが, `4 byte`で`32 bit`かな.
                * あれ, `unicode`も`4byte`だったっけ？？自信はない
            * `182 bit`は文字で言うと6文字分くらい
            * `6 * 10^4 = 60000`文字程度なら普通のコード書いていて読み書きすることも多い
            * じゃあ特段気にしなければいけないほど空間を圧迫しているわけでもなさそう
    * このハッシュ生成方法で問題を解いた場合の計算量
        * ハッシュの計算に`O(m)`で, それ以外は`sort`の方法と一緒
        * 全体だと, `O(n * m)`か.
    * ただ, この方法はアルファベットが増えたり, 大文字も許容するようになると増えた文字数分空間を圧迫することになる
    * このハッシュを作るためには, その文字列に含まれる文字ごとの個数を記録する
    * ってことは, わざわざbitによる一つの数字にしなくても同じようなことができる？？？
    * 二次元配列を用意するみたいな
        * `something[アルファベットが何か][そのアルファベットの個数][アルファベットが何か][そのアルファベットの個数]...`
        * 何次元配列だ？？？
        * アルファベットの種類 = 26
        * アルファベットの個数の最大 = 100
        * 2600次元配列？？
        * 配列に格納するのは, そのグループを表すはっしゅ？？
        * これは`182 bit`使う方法よりも空間を圧迫しそう
* 今回は二つの方法で実装する
    * ソートを使う方法 (pattern 1)
    * ハッシュを使う方法 (pattern 2)


## Code1-2

### 以下は120件目のテストケースでエラーしたコード

```python
from typing import List


class Solution:
    def calculate_hash(self, word):

        # Calculate value representing (alphabet, count) pair.
        def calculate_value(alphabet, count):
            seven_bit_maximum = 0b1111111
            if count < 0 or count > seven_bit_maximum:
                raise ValueError(f"count: {count} must be zero or positive and less than or equal to {seven_bit_maximum}")

            a_ord = ord("a")
            z_ord = ord("z")
            alphabet_ord = ord(alphabet)
            if alphabet_ord < a_ord or z_ord < alphabet_ord:
                raise ValueError(f"alphabet: {alphabet} must be small english letter")

            position = alphabet_ord - a_ord
            return count << position


        chr_to_count = {}
        for chr in word:
            chr_to_count.setdefault(chr, 0)
            chr_to_count[chr] += 1

        hash = 0
        for chr, count in chr_to_count.items():
            hash += calculate_value(chr, count)
        return hash


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_to_group = {}
        for word in strs:
            hash_value = self.calculate_hash(word)
            hash_to_group.setdefault(hash_value, [])
            hash_to_group[hash_value].append(word)
        return list(hash_to_group.values())

```            
        
* `bd`と`aacc`が同じグループに割り当てられている以外はあっていた.
* なぜこれらが同じハッシュを持ったのか??
    * オーバーフロー？？って思ったけど, 起こり得るのは`z`がいっぱい存在している時なはず
* とりあえずそれぞれのハッシュ値を`print`してみる
    * `bd`も`aacc`も`10`だった.
    * それ以外のものも全体的に想定していたより`hash`の値が小さすぎる
    * `<< position`ダメだ. `7bit`ずつ動かせていない

### ACとなったコード

```python
from typing import List


class Solution:
    def calculate_hash(self, word):

        # Calculate value representing (alphabet, count) pair.
        def calculate_value(alphabet, count):
            seven_bit_maximum = 0b1111111
            if count < 0 or count > seven_bit_maximum:
                raise ValueError(f"count: {count} must be zero or positive and less than or equal to {seven_bit_maximum}")

            a_ord = ord("a")
            z_ord = ord("z")
            alphabet_ord = ord(alphabet)
            if alphabet_ord < a_ord or z_ord < alphabet_ord:
                raise ValueError(f"alphabet: {alphabet} must be small english letter")

            position = alphabet_ord - a_ord
            num_bit_for_each = 7
            return count << position * num_bit_for_each


        chr_to_count = {}
        for chr in word:
            chr_to_count.setdefault(chr, 0)
            chr_to_count[chr] += 1

        hash = 0
        for chr, count in chr_to_count.items():
            hash += calculate_value(chr, count)
        return hash


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_to_group = {}
        for word in strs:
            hash_value = self.calculate_hash(word)
            hash_to_group.setdefault(hash_value, [])
            hash_to_group[hash_value].append(word)
        return list(hash_to_group.values())

```

# Step2

## Code2-1

* `sorted_word_to_group.values()`で得られるものを直接`return`するように変更

```python
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_word_to_group = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            sorted_word_to_group.setdefault(sorted_word, [])
            sorted_word_to_group[sorted_word].append(word)
        return list(sorted_word_to_group.values())
```

## Code2-2

* `chr`や`hash`などのライブラリに含まれる関数を避けた.
*　変数名や関数名を変更

```python
from typing import List


class Solution:
    def calculate_hash_by_alphabet_count(self, word):

        def calculate_alphabet_count_value(alphabet, count):
            bit_span = 7
            bit_maximum = 2 ** bit_span - 1
            if count < 0 or count > bit_maximum:
                raise ValueError(f"count: {count} must be zero or positive and less than or equal to {bit_maximum}")

            a_ord = ord("a")
            z_ord = ord("z")
            alphabet_ord = ord(alphabet)
            if alphabet_ord < a_ord or z_ord < alphabet_ord:
                raise ValueError(f"alphabet: {alphabet} must be small english letter")

            position = alphabet_ord - a_ord
            return count << position * bit_span


        alphabet_to_count = {}
        for alphabet in word:
            alphabet_to_count.setdefault(alphabet, 0)
            alphabet_to_count[alphabet] += 1

        hash = 0
        for alphabet, count in alphabet_to_count.items():
            hash += calculate_alphabet_count_value(alphabet, count)
        return hash


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_to_group = {}
        for word in strs:
            hash_value = self.calculate_hash_by_alphabet_count(word)
            hash_to_group.setdefault(hash_value, [])
            hash_to_group[hash_value].append(word)
        return list(hash_to_group.values())
```

# Step3

## Code3-1

```python
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_word_to_count = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            sorted_word_to_count.setdefault(sorted_word, [])
            sorted_word_to_count[sorted_word].append(word)
        return list(sorted_word_to_count.values())

```

## Code3-2

```python
from typing import List


class Solution:
    def calc_hash_by_alphabet_count(self, word, bit_span=7):
        alphabet_to_count = {}
        for alphabet in word:
            alphabet_to_count.setdefault(alphabet, 0)
            alphabet_to_count[alphabet] += 1
        
        hash_value = 0
        maximum_representable = 2 ** bit_span - 1
        for alphabet, count in alphabet_to_count.items():
            if count > maximum_representable:
                raise ValueError("bit span is too small")
            alphabet_count_value = count << (ord(alphabet) - ord("a")) * bit_span
            hash_value = hash_value | alphabet_count_value

        return hash_value

            
        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_to_group = {}
        for word in strs:
            hash_value = self.calc_hash_by_alphabet_count(word)
            hash_to_group.setdefault(hash_value, [])
            hash_to_group[hash_value].append(word)
        return list(hash_to_group.values())

```

# 学んだこと

* bitを使わなくても, `tuple`自体がhashableなことを利用すればもっと単純にかけた.
* やっていることは似ているが, 公式の`tuple`のハッシュ化の方が効率化されていそう
    * https://github.com/python/cpython/blob/main/Objects/tupleobject.c

```c
    for (Py_ssize_t i = 0; i < len; i++) {
        Py_uhash_t lane = PyObject_Hash(item[i]);
        if (lane == (Py_uhash_t)-1) {
            return -1;
        }
        acc += lane * _PyTuple_HASH_XXPRIME_2;
        acc = _PyTuple_HASH_XXROTATE(acc);
        acc *= _PyTuple_HASH_XXPRIME_1;
    }
```
