# Step1

## アプローチ


### 問題設定を整理

* `query`が与えられて, `wordsContainer`の中から最長の`query`とのサフィックスを持つ単語（のインデックス）を出力する
* `len(wordsContainer)` <= 10^4: Nとする
* `query`や`wordsContainer`内の単語の文字数 <= 5 * 10^3: Lとする
* `query`自体の個数 <= 10^4: Mとする
* `wordsContainer`に含まれる単語の全ての文字数の和 <= 5 * 10^5
* `query`に含まれる単語の全ての文字数の和 <= 5 * 10^5

### 解法を考える

* 一番単純にやる
    * `wordsContainer`の中の各単語`word`に対して, `query`と末尾から共通する文字を比較し続ける
    * O(N * M * L)
        * 10^11 / 10^6 ~= 10^5 secかかる
* `wordsContainer`の中身をTrie木として持っておく
    * `query`ごとにそのTrie木をたどればいい
* Trie木の構築にどのくらいかかるか
    * `wordsContainer`の全ての文字を見ればいいから
        * O(N * L)
        * 問題の制約より 5 * 10^5 / 10^6 ~= 0.1 sec程度でできそう
* Trie木を辿るのに全部でどのくらいかかるか
    * `query`ごとに, その文字数を見ればいいので
        * O(M * L)
        * 問題の制約より 5 * 10^5 / 10^6 ~= 0.1 sec程度でできそう
* インデックスを返したいけどそれはできそうか
    * Trie木で通常できるのは, `wordsContainer`の全単語共通のsuffixを辿ることだけ
    * 各段階(ノード)ごとに, どのwordに対応しているかを保存しておく
    * かつ, suffixが共通の時は, 問題の指示では単語の長さが一番短いものを返す必要がある
    * 単語の長さをもとにheapを各ノードに持たせるか
    * そしたら, Trie木を作るのは
        * O(M * L * logM)になりそう
        * 5 * 10^5 * log10^4 ~= 10^6~10^7 secくらい
        * 十分早い(1sec以内)
* Trie木は通常prefixを作るのに使うけど, suffixを作るにあたって考え方をどう変える必要があるか
    * 文字列をreverseするのが一番単純？
    * 最初に, 全部の文字をreverseした配列を作ってしまうのが単純そう
        * O(N * L)だから0.1secくらいでできそう
* ここまで17:46. 実装にうつる

## Code1-1

* 18:07でAC

```python
import heapq

class Node:
    def __init__(self):
        self.children = [None] * (ord("z") - ord("a") + 1)
        self.word_length_and_index = []

    def add_word_info(self, word, index) -> None:
        heapq.heappush(self.word_length_and_index, (len(word), index))

class Trie:
    def __init__(self, reversed_words: list[str]):
        node = Node()
        for i, reversed_word in enumerate(reversed_words):
            node.add_word_info(reversed_word, i)
        self.root = node

    def _get_char_index(self, ch: str) -> int:
        return ord(ch) - ord("a")

    def add(self, reversed_word: str, index: int) -> None:
        node = self.root
        for ch in reversed_word:
            i_ch = self._get_char_index(ch)
            if node.children[i_ch] is None:
                node.children[i_ch] = Node()
            node = node.children[i_ch]
            node.add_word_info(reversed_word, index)
        return

    def get_longest_common_suffix_index(self, reversed_query: str) -> None:
        node = self.root
        for ch in reversed_query:
            i_ch = self._get_char_index(ch)
            if node.children[i_ch] is None:
                break
            node = node.children[i_ch]
        return node.word_length_and_index[0][1]
            

class Solution:

    def _reverse_all_words(self, words: list[str]) -> list[str]:
        reversed_words = []
        for word in words:
            reversed_words.append(word[::-1])
        return reversed_words

    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        reversed_words_container = self._reverse_all_words(wordsContainer)
        trie = Trie(reversed_words_container)
        for i, reversed_word in enumerate(reversed_words_container):
            trie.add(reversed_word, i)

        longest_common_suffix_indices = []
        reversed_queries = self._reverse_all_words(wordsQuery)
        for reversed_query in reversed_queries:
            index = trie.get_longest_common_suffix_index(reversed_query)
            longest_common_suffix_indices.append(index)
        
        return longest_common_suffix_indices
        
```

# Step2

## Code2-1

```python
import heapq


class Node:
    def __init__(self):
        self.children = [None] * (ord("z") - ord("a") + 1)
        self.word_length_and_index = []

class Trie:
    def __init__(self, reversed_words: list[str]):
        self.root = Node()
        for i, reversed_word in enumerate(reversed_words):
            # suffixが一致しなかった時用
            heapq.heappush(
                self.root.word_length_and_index, 
                (len(reversed_word), i))

            self._add(reversed_word, i)

    def _get_char_index(self, ch: str) -> int:
        return ord(ch) - ord("a")

    def _add(self, reversed_word: str, index: int) -> None:
        node = self.root
        for ch in reversed_word:
            i_ch = self._get_char_index(ch)
            if node.children[i_ch] is None:
                node.children[i_ch] = Node()
            node = node.children[i_ch]
            heapq.heappush(
                node.word_length_and_index, 
                (len(reversed_word), index))
        return

    def get_longest_common_suffix_index(self, reversed_query: str) -> None:
        node = self.root
        for ch in reversed_query:
            i_ch = self._get_char_index(ch)
            if node.children[i_ch] is None:
                break
            node = node.children[i_ch]
        return node.word_length_and_index[0][1]
            

class Solution:

    def _reverse_all_words(self, words: list[str]) -> list[str]:
        reversed_words = []
        for word in words:
            reversed_words.append(word[::-1])
        return reversed_words

    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = Trie(self._reverse_all_words(wordsContainer))

        longest_common_suffix_indices = []
        for reversed_query in self._reverse_all_words(wordsQuery):
            index = trie.get_longest_common_suffix_index(reversed_query)
            longest_common_suffix_indices.append(index)
        
        return longest_common_suffix_indices

```