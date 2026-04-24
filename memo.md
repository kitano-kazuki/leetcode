# Step1

## アプローチ

* Trie木を作っておけば, 前から見ながら辞書の要素とマッチさせられそう
    * leetcode
    * [lee, tcode, leet, codo]
    * の時に, leetじゃなくてleeにマッチさせないと正しく動作しない
    * 全てのパターンを試すのが一番ナイーブな方法
        * leeでやってみる, ダメだったらleetでやってみる
    * この時の計算量を見積もらないと, このアプローチが良いかどうか判断しかねる
        * 計算量が最悪となるのは, 共通のprefixを持つものがlen(wordDict)存在する時
        * かつ, `s`でprefixをマッチさせた後がまだprefixになる場合
        * aaaaaaaaaaaaaa
        * [a, aa, aaa, aaaa, aaaaa]
        * とか??
        * len(wordDict) * len(wordDict) * ... * len(wordDict)
        * n = len(wordDict), m = len(s)とする
        * O(n^m)
        * 1000^300 stepほど必要だから到底終わらない
    * Greedyに一番長いものからやるとしたらどうか
        * 定数倍しか変わらなさそう
    * でも, 人の手でやる時も`aaaaa`系のものに対しては全部辞書の値と見比べないとできなくない？？
* rolling hashをする場合はどうだろう
    * やっていることはTrie木と一緒な気がする
* Divide and Conquerは？？
    * 真ん中からハッシュを広げてマッチするのがdictにあるかみる
        * でも結局複数そこでマッチしてしまったら, その個数分呼び出す必要がある
        * 長さが半分に減っていく分処理としては軽い可能性ある？？
* 今更気づいたけど, `wordDict[i].length`はたかだか20
    * prefixとsuffixが同じになるwordはたかだか20か？？と思ったけど違いそう
        * aabaa, aacaa, aadaa, ...
* わからないので, leetcodeのSolutionを流し読みする
    * ざっくりDPとBFSがあるっぽい
* `s`の各indexをノードとしてそのindexまでの文字列を辞書語で作れるならエッジがあるとする
    * そしたら, たかだかm^2しかエッジは存在しない
    * 各エッジごとに, `s`の部分文字列がdictに存在するかみるため, ハッシュ計算と部分文字列の生成でO(m)はかかる
    * O(m^3)程度の実行時間
    * 300^3 = 27 * 10^6なので, 2.7sec ~ 27secくらいの実行時間
    * 部分文字列の長さが20より大きくなりそうなら計算しなくていい(wordDict[i].length <= 20)ので, 実質的にはO(m^2 * n)くらいにできそう
* 今までのアプローチの問題点は, あるindexまでの作り方のパターンが複数あったとしてそれらを全部見ていたこと
    * 大事なのはそのindexまで作れるかどうか

## Code1-1 (DP)

```python
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_dict_set = set(wordDict)
        # edges[i] means s[:i] can be segmented
        edges = [False] * (len(s) + 1)
        edges[0] = True
        
        for end in range(1, len(s) + 1):
            for start in range(end):
                if not edges[start]:
                    continue
                substring = s[start:end]
                if substring not in word_dict_set:
                    continue
                edges[end] = True
                break
        
        return edges[len(s)]

```

# Step2

## Code2-1 (DP)

```python
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_dict_set = set(wordDict)
        # is_segmentable[i] means s[:i] can be segmented
        is_segmentable = [False] * (len(s) + 1)
        is_segmentable[0] = True
        
        for end in range(1, len(s) + 1):
            for start in range(end, -1, -1):
                if not is_segmentable[start]:
                    continue
                substring = s[start:end]
                if substring not in word_dict_set:
                    continue
                is_segmentable[end] = True
                break
        
        return is_segmentable[len(s)]

```

## Code2-2 (Trie)

* Trie木での実装を行った.
* 計算量を見積もる
    * len(wordDict) = n, len(s) = m, len(wordDict[i]) = k
    * Trie木の構築
        * O(n * k)
    * 分割可能かの判定
        * 各sの文字ごとに, Trie木を辿る
        * Trie木を辿って得られた結果分, is_segmentableを更新する
            * これは, Trie木辿っているときに一緒に更新しても良さそう.
            * でも, Trie木の構造に今回の問題の内容が含まれるのが気持ち悪い
        * O(n * k)
    * O(n * k)??? でも, 直感的にはO(n^3)がここまで改善されるのは不思議なきもしてしまう
        * Step3で詳しく考えていこう

```python
class Node:
    def __init__(self):
        self.children = [None] * (ord("z") - ord("a") + 1)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, s: str) -> None:
        node = self.root
        for c in s:
            index = self._get_alphabet_index(c)
            if node.children[index] is None:
                node.children[index] = Node()
            node = node.children[index]
        node.is_word = True
        return

    def get_word_end_indices(self, word: str, start: int) -> list[int]:
        node = self.root
        end_indices = []
        for i in range(start, len(word)):
            index = self._get_alphabet_index(word[i])
            if node.children[index] is None:
                return end_indices
            node = node.children[index]
            if node.is_word:
                end_indices.append(i)
        return end_indices

    def _get_alphabet_index(self, char: str) -> int:
        return ord("z") - ord(char)


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.add(word)
        
        is_segmentable = [False] * (len(s) + 1)
        is_segmentable[0] = True
        for i in range(len(s)):
            if not is_segmentable[i]:
                continue
            word_end_indices = trie.get_word_end_indices(s, i)
            for end_index in word_end_indices:
                is_segmentable[end_index + 1] = True

        return is_segmentable[len(s)]

```

# Step3

## 他の人のコードをみる

* https://github.com/olsen-blue/Arai60/pull/39
    * 再帰関数を用いた方法
        * `tail_index`まで分割できるかを知りたい
            * `wordDict`の各単語分引き戻した文字列があるなら, そこを`tail_index`にして再帰
        * 直感的（自然言語での動作と似ている）でわかりやすい
            * でも、今回自分は素手で作業することを考えた時にも後ろからやる方法は思いつかなかった
    * ボトムアップとトップダウンのDPそれぞれ
    * sliceはコピーが作成されるのでstr.startswith()の使用について言及
    * リーダブルコードという本がコメントで紹介されていたので買った
    
* https://github.com/naoto-iwase/leetcode/pull/44
    * step1ではスタックに次見る候補を入れる方法
    * bottom-up DPでの実装も

* https://github.com/mamo3gr/arai60/pull/37
    * DFSを読みやすく書いている
        * 今までは, DFSやBFSを考える時に, ノードがこれでエッジがこれって考えていたが、もっと単純に可能性を列挙すると捉えた方がわかりやすそう

## 他の人のコメントを見る

* Trieクラスのメソッドについて
    * https://github.com/katsukii/leetcode/pull/11#discussion_r1929802127
    * > Trie クラスにもう少しメソッドを生やしませんか。今、外側から中身をいじっていますが、自然言語で説明すると Trie にさせたいことは、「Trie に単語を登録する」「Trie に文字列と開始位置を渡して、そこからマッチする単語をすべて返してもらう」の2つですよね。素直にそれをメソッドにすればよいかと思います。
* 計算量の見積もり
    * https://discord.com/channels/1084280443945353267/1200089668901937312/1221644164576444527
    * > この問題、まず正規表現で書くことができるので O(n) で解けるはずとまず初めに考えました。
    * Code2-2のところで, O(n * k)???と書いたが, 正規表現でできるという感覚があればこの疑問は生まれなかった
* Trie木の表現方法における最適化（C++）
    * https://github.com/5ky7/arai60/pull/40#discussion_r2990860360
    * > vector<TrieNode>を作って、vectorへのindexをTrieNode内で持つ方がおそらく速いですね
* 問題背景(ビタビアルゴリズム)
    * https://github.com/tom4649/Coding/pull/37#discussion_r3063553642
    * > 背景として、 Vitabi のアルゴリズムがありそうな気がしました。

## 自分で調べてみる

### `startswith`メソッド

公式ドキュメント
https://docs.python.org/3/library/stdtypes.html#str.startswith
> Return True if string starts with the prefix, otherwise return False. prefix can also be a tuple of prefixes to look for. With optional start, test string beginning at that position. With optional end, stop comparing string at that position.


ソースコード
https://github.com/python/cpython/blob/v3.14.4/Objects/unicodeobject.c

13609行目に関数定義, メインの処理は9937行目の`tailmatch`メソッド.

```cpp
int result = tailmatch(self, substring, start, end, -1);
```

`tailmatch`の動作
```cpp
if (kind_self == kind_sub) {
    return ! memcmp((char *)data_self +
                        (offset * PyUnicode_KIND(substring)),
                    data_sub,
                    PyUnicode_GET_LENGTH(substring) *
                        PyUnicode_KIND(substring));
}
```

`memcmp`のリフェレンス
```
int memcmp( const void* lhs, const void* rhs, size_t count );
```
> Compares the first count bytes of the objects pointed to by lhs and rhs. The comparison is done lexicographically.
> The sign of the result is the sign of the difference between the values of the first pair of bytes (both interpreted as unsigned char) that differ in the objects being compared.
> The behavior is undefined if access occurs beyond the end of either object pointed to by lhs and rhs. The behavior is undefined if either lhs or rhs is a null pointer.

つまり, 与えられた二つの文字列をバイトとして比較している
確かにコピーを作らないし, 早いわけだ

#### 気になること

https://github.com/python/cpython/blob/23116f998f6789d8c2fbe5ed5b8146854c8c2a4f/Objects/unicodeobject.c#L9965
```cpp
if (direction > 0)
    offset = end;
else
    offset = start;
```

`direction`が正の時に, `offset = end`として, `direction`が負の時に, `offset = start`としている.
感覚的には, 逆な気がする. 
`tailmatch`という名が指す通り, `tail`が`start`側か`end`側かという意味で, ↑みたいになっているのか.納得


# Step4