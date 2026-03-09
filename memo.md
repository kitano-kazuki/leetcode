# Step1

## アプローチ

* １文字違いのword同士でエッジがあるとする
* DFSやBFSを使って一番短いパスを見つける問題と言えそう
* やっていることは全探索になるので, 計算時間的にどのくらいかかるか次第でこのアプローチ取れるか変わりそう
* 各文字同士が１文字違いかどうか見るために, `len(beginWord) * len(wordList) ^ 2`で全てのwordの組み合わせを確認.
* グラフが構築される
* グラフのあるノード(beginWord)からあるノード(endWord)までのパスを辿る
* このパスを辿るためにかかるステップ数が見積もれない...
    * 後で確認しよう

## Code1-1 (51/52テストケースでTLE)

```python
from typing import List
from collections import deque
import copy


class Node:
    def __init__(self, id : int, nexts : List[Node]):
        self.id = id
        self.nexts = nexts
    
    def __repr__(self)        :
        return f"Node(id={self.id})"

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def is_one_word_difference(word1, word2):
            if len(word1) != len(word2):
                raise ValueError(f"The length of {word1} and {word2} are different")
            difference_count = 0
            word_len = len(word1)
            for i in range(word_len):
                if word1[i] == word2[i]:
                    continue
                difference_count += 1
            return difference_count == 1

        start_node_id = None
        end_node_id = None
        id_to_node = {}
        for word1_id in range(len(wordList)):
            if wordList[word1_id] == beginWord:
                start_node_id = word1_id
            elif wordList[word1_id] == endWord:
                end_node_id = word1_id

            if word1_id not in id_to_node:
                id_to_node[word1_id] = Node(word1_id, [])
            word1_node = id_to_node[word1_id]
            for word2_id in range(word1_id + 1, len(wordList)):
                if not is_one_word_difference(wordList[word1_id], wordList[word2_id]):
                    continue
                if word2_id not in id_to_node:
                    id_to_node[word2_id] = Node(word2_id, [])
                word2_node = id_to_node[word2_id]
                word1_node.nexts.append(word2_node)
                word2_node.nexts.append(word1_node)


        copy_word_list = copy.deepcopy(wordList)
        if start_node_id is None:
            copy_word_list.extend([beginWord])
            start_node_id = len(copy_word_list) - 1
            start_node = Node(start_node_id, [])
            id_to_node[start_node_id] = start_node
            for word_id in range(len(wordList)):
                if not is_one_word_difference(beginWord, copy_word_list[word_id]):
                    continue
                start_node.nexts.append(id_to_node[word_id])
                id_to_node[word_id].nexts.append(start_node)

        total_words = len(copy_word_list)                

        visited = [False] * total_words
        candidate_nodes = deque()
        candidate_nodes.append(id_to_node[start_node_id])

        distance = 0
        while candidate_nodes:
            num_nodes = len(candidate_nodes)
            distance += 1
            for _ in range(num_nodes):
                node = candidate_nodes.popleft()
                if node.id == end_node_id:
                    return distance
                if visited[node.id]:
                    continue
                visited[node.id] = True
                for connected_node in node.nexts:
                    if visited[connected_node.id]:
                        continue
                    candidate_nodes.append(connected_node)
        
        NOT_FOUND = 0
        return NOT_FOUND

```


# 気になったところを調べる

* デバッグする前のコードでは, `Node`の定義を以下のようにしていた
    *  `start_node = Node(start_node_id)`をしたときに, 勝手に`nexts`にnodeが入っていたため, 正しい動作をしなかった
    * これは, デフォルト引数は関数定義時に作られるからである.
    * 公式ドキュメントに`important warning`として記載されていた
        * https://docs.python.org/3/tutorial/controlflow.html#default-argument-values
        * > The default value is evaluated only once. This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes. For example, the following function accumulates the arguments passed to it on subsequent calls:
    * 知らなかった. デバッグ時間かかったけど, 知ることができてよかった


```python
class Node:
    def __init__(self, id : int, nexts : List[Node] = []):
        self.id = id
        self.nexts = nexts
```

* １文字違いの検出にO(k * n^2)かかる問題
    * https://discord.com/channels/1084280443945353267/1200089668901937312/1216123084889788486
        * > 頭から半分または尻尾から半分が一致しているはずなので、それでバケットを作ってバケット内でのみ比較すればいいというやりかたもありますね。(編集距離が1であるかの確認に、頭から何文字一致していて、尻尾から何文字一致しているかを足してやればいいという方法をどっかで使ったことあります。)
        * https://cs.stackexchange.com/questions/93467/data-structure-or-algorithm-for-quickly-finding-differences-between-strings
            * > Take each string and store it in a hashtable, keyed on the first half of the string. Then, iterate over the hashtable buckets. For each pair of strings in the same bucket, check whether they differ in 1 character (i.e., check whether their second half differs in 1 character).
            * >  In each of these strings replace one of the letters with a special character, not found in any of the strings. While you add them, check that they are not already in the set. If they are then you have two strings that only differ by (at most) one character.

# 他の人のコード

1. https://github.com/ksaito0629/leetcode_arai60/pull/19
    * 言語: Python3
    * Step1では, 自分の解法と同様に最初に1文字違いのword群を辞書で保存していた.
        * これはやっぱりTLEになるっぽい. 
    * Step2.1, Step2.2では上項で調べた1文字違いの文字列発見のアルゴリズムを使用
        * [key = 1文字無くしたタプル, value = 1文字無くす前の文字列のidx(あるいは文字列自体)リスト] のやつ
        * 自分のコードみたいにNodeとしてわざわざ定義しない方が簡潔に書けそう
        * queueにdistanceを一緒に保存する方法も使っていた. この辺は好みかな
        * Step3で`yield`を使った最適化をしている
    * Step2.3では双方向のBFSを使用
        * endWordからも探ることで, 探索を小さい方の集合で行っている
        * 最悪計算量は変わらないけど, いくつかのケースでは探索量が減りそう
    * Step2.4では, 上項で調べた1文字違いの文字発見アルゴリズムの一つ目を利用(前半のkeyを使うやつ)
        * 実行にかかる時間をT(N, k)とする. Nは文字列の数, kは文字列の長さ
        * T(N, k) = T(n1, k/2) + T(n2, k/2) + ... + T(m1, k/2) + T(m2, k/2) + ...
        * n1, n2 ...は前半の文字列がx1で等しい文字列の個数
        * m1, m2 ...は後半の文字列がx2で等しいて文字列の個数
        * 文字列が同じものを含まない時, n1 + n2 + ... + m1 + m2 + ... = Nになる
        * そして左辺を右辺に変換するのにかかる計算量は O(N * k)
            * N個の要素について, 前半部分のハッシュを計算するのにO(k)かかる
        * 最終的にはT(N, k) = ... = T(a1, 1) + T(a2, 1) + T(a3, 1) + ... になる
        * ここに至るまでに行われる変換の総数は O(n * k * logk)
            * 全てのT(a_i, k')をいくつかのT(b_i, k' / 2)にするときは, 各々のa_iについて見なくても, Σa_iがNであるから T(N,k')と同じと考えられて, O(N * k')
            * 最終的に k -> k / 2 -> ... -> 1となるまでには logk回の変換が必要
            * k'はkとしても計算量を考える上ではいい
        * T(a1, 1) + T(a2, 1) + T(a3, 1) ... となっている状況では, それぞれの塊(a_i)が１文字違いのものたちを表す
            * これらをdictにmappingするためには, a1^2 + a2^2 + a3^2 + ...とかかる
            * これは (a1 + a2 + ... )^2よりも小さいので, Orderを考える上では上界を使って良い
            * O(N^2)
        * トータルだと O(n * k * logk + n^2)
2. https://github.com/TakayaShirai/leetcode_practice/pull/20/changes
    * 言語: Dart
    * 「素直な方法」では, 最初に`adjacentWordsMap`として文字列から１文字違いの文字列のリストが手に入る辞書を用意. O(n^2)のペアに対してO(k)で先頭から一致した文字数の個数を確認
        * PythonだとTLEだけど, Dartならいけるって話？？
        * 10^7 steps / sec と言っているから, O(n^2 * k)のステップ数 (5 * 10^3)^2 * 10 = 25 * 10^7に対してもTLEしそうだけど...
            * https://medium.com/full-struggle-developer/flutter-benchmark-tuesday-apologies-to-zoomers-208dd83a3e57
            * この記事によると, 10^8 / secくらいのポテンシャルはありそう
    * 「a-zを使用する方法」では, `adjacentWordsMap`を構築する別の方法を提案
        * あらかじめ与えられた`wordList`をSetとして用意しておく.
        * wordListの各wordに対して, 文字列のi番目を別のアルファベットに置き換えて, それがSetに含まれているかを見ることで1文字違いを発見
        * これ計算量的にどのくらい改善されているのか
            * Setを用意するのにかかる時間は各文字列のハッシュ値の計算分だから O(n * k)
            * 各文字列ごとに計算 O(n)
                * 各位置ごとに計算 O(k)
                    * アルファベット25通り(その文字以外だから) O(26)
                        * 置き換えで文字列をコピーしていたら, O(k)
                        * それで置き換えたものごとに,ハッシュ値の計算で O(k)
                        * ハッシュ値がSetにあるかどうかは, O(1)
            * トータルだと O(n * k + n * k^2) = O(n * k^2)
        * めっちゃ改善されているし, 発想も割と直感的な気がする
    * 「ワイルドカードを使用する方法」も同様に`adjacentWordsMap`の構築方法について (1の解法のStep2.1, 2.2に該当)
        * 計算量を考えてみる
            * まず, `patternMap`として文字列の一箇所を`*`で置き換えたkeyに対して, 置き換える前の文字列をvalueのリストに追加
                * 各文字列について O(n)
                    * 各位置について O(k)
                        * `*`で置き換えた文字列を用意 O(k)
                        * それのハッシュ値の計算 O(k)
                * だから, O(n * k^2)
            * 次に, `adjacentWordsMap`に, 文字列をkeyとして, 1文字違いの文字列のリストを保存する
                * 各文字列について O(n)
                    * 各位置について O(k)
                        * `*`に置き換えたパターンを計算 O(k)
                        * そのハッシュを計算 O(k)
                        * パターンに対応する文字列群を`patternMap`から取得 O(1)
                        * 置き換える前の文字列をkeyとして, valueに上記で取得したものを追加 O(1)
                * O(n * k^2)
    * 残りの部分はBFS
3. https://github.com/Hiroto-Iizuka/coding_practice/pull/20
    * Step1は, 愚直にO(n * k)で, １文字違う文字列をwordListから探す
        * ただ, 最初に構築するのではなくて, 今見ているwordの次のwordを探す段階で探索している分少しだけ効率的か
    * Step2では, アルファベットを置き換える方法を使用(2の解法でも使用していた)
4. https://github.com/PafsCocotte/leetcode/pull/3
    * Step1では, 愚直にO(n * k)の方法. C++なのでACになっていそう
    * Step2では, アルファベットを置き換える方法
5. https://github.com/xbam326/leetcode/pull/22
    * Step1では愚直な方法. PythonなのでTLE
    * Step2ではワイルドカードを使う方法

# Step2

## Code2-1 (alphabet replacement)

```python
from collections import deque, defaultdict
import copy

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def construct_word_to_adjacents_dict(word_list):
            word_to_adjacents = defaultdict(set)
            word_set = set(word_list)
            for word in word_list:
                for i in range(len(word)):
                    for alphabet_ord in range(ord("a"), ord("z") + 1):
                        alphabet = chr(alphabet_ord)
                        if word[i] == alphabet:
                            continue
                        ith_replaced = f"{word[:i]}{alphabet}{word[i + 1:]}"
                        if ith_replaced in word_set:
                            word_to_adjacents[word].add(ith_replaced)
            return word_to_adjacents
       
        copy_word_list = copy.deepcopy(wordList)
        if beginWord not in copy_word_list:
            copy_word_list.append(beginWord)
        
        word_to_adjacents = construct_word_to_adjacents_dict(copy_word_list)

        visited = {word : False for word in copy_word_list}
        candidate_queue = deque()
        candidate_queue.append(beginWord)
        distance = 0
        while candidate_queue:
            num_candidates = len(candidate_queue)
            distance += 1
            for _ in range(num_candidates):
                cur_word = candidate_queue.popleft()
                if visited[cur_word]:
                    continue
                visited[cur_word] = True
                if cur_word == endWord:
                    return distance
                if cur_word not in word_to_adjacents:
                    continue
                for adj_word in word_to_adjacents[cur_word]:
                    candidate_queue.append(adj_word)
        
        NOT_FOUND = 0
        return NOT_FOUND

```

## Code2-2 (wild card)

* extendの挙動について
    * extendは複数回の`append`と考えたら良さそう
    * 文字列はimmutableなので, 下の１つ目の例のintの要素を持つ配列と同じような挙動になる

```python
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
b.append(7)
print(a)

# [1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6]

a = [[1], [2], [3]]
b = [[4], [5], [6]]
a.extend(b)
print(a)
b[0].append(7)
print(a)

# [[1], [2], [3], [4], [5], [6]]
# [[1], [2], [3], [4, 7], [5], [6]]
```

* lambda関数の引数について
    * lambda xとしたときのxはlocal変数なので大丈夫
    * lambda: xとした場合は, xを外から取り込むことになる. この時のxは実行時に取り込まれるので注意が必要

```python
from collections import deque, defaultdict
import copy

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def construct_word_to_adjacents_dict(word_list):
            # MEMO: 実行時にforのwordが取り込まれそうで怖いからwに変数名を変えた
            get_patterns = lambda w : [ (w[:i], w[i + 1:]) for i in range(len(w))]
            pattern_to_words = defaultdict(list)
            for word in word_list:
                for pattern in get_patterns(word):
                    pattern_to_words[pattern].append(word)

            word_to_adjacents = defaultdict(list)
            for word in word_list:
                for pattern in get_patterns(word):
                    adj_words = pattern_to_words[pattern]
                    # MEMO: extendの時に後追加されるものはdeepcopyなのか？？？今回はshallowでも影響ないけど
                    word_to_adjacents[word].extend(adj_words)
            
            return word_to_adjacents
        
        word_list_copy = copy.deepcopy(wordList)
        if beginWord not in word_list_copy:
            word_list_copy.append(beginWord)

        word_to_adjacents = construct_word_to_adjacents_dict(word_list_copy)

        visited = set()
        candidates = deque()
        candidates.append(beginWord)
        distance = 0
        while candidates:
            num_candidates = len(candidates)
            distance += 1
            for _ in range(num_candidates):
                cur_word = candidates.popleft()
                if cur_word in visited:
                    continue
                visited.add(cur_word)
                if cur_word == endWord:
                    return distance
                for adj_word in word_to_adjacents[cur_word]:
                    if adj_word in visited:
                        continue
                    candidates.append(adj_word)
        
        NOT_FOUND = 0
        return NOT_FOUND


```

## Code2-3 (former latter dict)

```python
from collections import deque, defaultdict
import copy

class Solution:
    def get_word_to_adjacents(self, word_list: list[str]) -> dict[str, list[str]]:
        word_to_adjacents = defaultdict(list)

        def register_to_word_to_adjacents_in_range(start_idx, end_idx, candidates):
            if start_idx > end_idx:
                return
            if start_idx == end_idx:
                for i in range(len(candidates)):
                    for j in range(len(candidates)):
                        if i == j:
                            continue
                        word_to_adjacents[candidates[i]].append(candidates[j])
                return
                
            mid_idx = (start_idx + end_idx) // 2
            former_to_matched_words = defaultdict(list)
            latter_to_matched_words = defaultdict(list)
            for candidate in candidates:
                former = candidate[start_idx:mid_idx + 1]
                if former:
                    former_to_matched_words[former].append(candidate)
                latter = candidate[mid_idx + 1:end_idx + 1]
                if latter:
                    latter_to_matched_words[latter].append(candidate)
            
            for former_matched_candidates in former_to_matched_words.values():
                register_to_word_to_adjacents_in_range(mid_idx + 1, end_idx, former_matched_candidates)
            for latter_matched_candidates in latter_to_matched_words.values():
                register_to_word_to_adjacents_in_range(start_idx, mid_idx, latter_matched_candidates)
            return

        register_to_word_to_adjacents_in_range(0, len(word_list[0]) - 1, word_list)
        return word_to_adjacents

    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        copy_word_list = copy.deepcopy(wordList)
        if beginWord not in copy_word_list:
            copy_word_list.append(beginWord)
        
        word_to_adjacents = self.get_word_to_adjacents(copy_word_list)

        visited = set()
        candidates = deque()
        candidates.append(beginWord)
        distance = 0
        while candidates:
            num_candidates = len(candidates)
            distance += 1
            for _ in range(num_candidates):
                cur_word = candidates.popleft()
                if cur_word in visited:
                    continue
                visited.add(cur_word)
                if cur_word == endWord:
                    return distance
                for adj_word in word_to_adjacents[cur_word]:
                    if adj_word in visited:
                        continue
                    candidates.append(adj_word)
        NOT_FOUND = 0
        return NOT_FOUND

```


# Step3

## Code3-1 (alphabet replacement)

```python
import copy
from typing import Generator
from collections import defaultdict, deque


class Solution:
    def get_word_to_adjacents_dict(self, word_list: list[str]) -> dict[str, list[str]]:

        def yield_one_alphabet_replaced(word: str) -> Generator[str, None, None]:
            for pos in range(len(word)):
                for alphabet_ord in range(ord("a"), ord("z") + 1):
                    alphabet = chr(alphabet_ord)
                    if word[pos] == alphabet:
                        continue
                    yield f"{word[:pos]}{alphabet}{word[pos + 1:]}"

        word_to_adjacents = defaultdict(list)
        
        word_list_set = set(word_list)
        for word in word_list:
            for replaced_word in yield_one_alphabet_replaced(word):
                if replaced_word in word_list_set:
                    word_to_adjacents[word].append(replaced_word)
        
        return word_to_adjacents
                    
                    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_list_copy = copy.deepcopy(wordList)
        if beginWord not in word_list_copy:
            word_list_copy.append(beginWord)
        
        word_to_adjacents = self.get_word_to_adjacents_dict(word_list_copy)

        candidates = deque()
        candidates.append(beginWord)
        visited = set()
        distance = 0
        while candidates:
            distance += 1
            num_cur_candidates = len(candidates)
            for _ in range(num_cur_candidates):
                word = candidates.popleft()
                if word == endWord:
                    return distance
                if word in visited:
                    continue
                visited.add(word)
                for adj_word in word_to_adjacents[word]:
                    if adj_word not in visited:
                        candidates.append(adj_word)
        
        NOT_FOUND = 0
        return NOT_FOUND
            

```

## Code3-2 (wild card)

```python
from typing import Generator
from collections import defaultdict, deque
import copy


class Solution:
    def get_word_to_adjacents_dict(self, word_list: list[str]) -> dict[str, list[set]]:

        def yield_pattern(word: str) -> Generator[tuple[str, str], None, None]:
            for i in range(len(word)):
                yield (word[:i], word[i + 1:])
        
        pattern_to_words = defaultdict(set)
        for word in word_list:
            for pattern in yield_pattern(word):
                pattern_to_words[pattern].add(word)
        
        word_to_adjacents = defaultdict(set)
        for word in word_list:
            for pattern in yield_pattern(word):
                word_to_adjacents[word] = word_to_adjacents[word] | pattern_to_words[pattern]

        return word_to_adjacents

        

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_list_copy = copy.deepcopy(wordList)
        if beginWord not in word_list_copy:
            word_list_copy.append(beginWord)

        word_to_adjacents = self.get_word_to_adjacents_dict(word_list_copy)
        
        visited = set() 
        candidates = deque()
        candidates.append(beginWord)
        distance = 0
        while candidates:
            num_cur_candidates = len(candidates)
            distance += 1
            for _ in range(num_cur_candidates):
                word = candidates.popleft()
                if word == endWord:
                    return distance
                if word in visited:
                    continue
                visited.add(word)
                for adj_word in word_to_adjacents[word]:
                    if adj_word in visited:
                        continue
                    candidates.append(adj_word)
        
        NOT_FOUND = 0
        return NOT_FOUND

```


## Code3-3 (former latter)

* 再帰を考える時には, グループする機能にした方がわかりやすかった
    * グループ化した後に, それをもとに`word_to_adjacents`を作る
* イメージとしては以下のようなものを考えた
    * いろんなファッションをしている人がN人並んでいる.
    * 各シフトの人は, 指定された範囲(e.g. 上半身)を上半分(e.g. 顔部分)と下半分(e.g. Tシャツ部分)に分けて一緒かどうか見る
    * そして, 1アイテム違いのファッションになりそうなグループを次のシフトの人に引き継ぐ.
    * 顔のアクセサリーが全部一緒だったら, 次のシフトの人にはTシャツ部分を見て貰えばいい
        * 帽子A, メガネBで一緒の人たちはひとまとめにした上で次のシフトの人に見てもらう
        * 帽子B, メガネBで一緒の人たちも別のまとまりとして次のシフトの人に見てもらう
    * 同様に, Tシャツ部分が全部一緒だったら, 次のシフトの人には顔の部分を見て貰えばいい

```python
from collections import defaultdict, deque
import copy


class Solution:

    def group_one_word_differents_in_range(self, range_start: int, range_end: int, words: list[str]) -> list[set[str]]:
        if range_start > range_end:
            return []
        if range_start == range_end:
            words_set = set(words)
            if len(words_set) == 1:
                return []
            return [words_set]
        
        range_mid = (range_start + range_end) // 2
        former_to_words = defaultdict(list)
        latter_to_words = defaultdict(list)
        for word in words:
            if range_start <= range_mid:
                former = word[range_start:range_mid + 1]
                former_to_words[former].append(word)
            if range_mid + 1 <= range_end:
                latter = word[range_mid + 1:range_end + 1]
                latter_to_words[latter].append(word)
        
        result = []
        if range_mid + 1 <= range_end:
            for words_with_same_former in former_to_words.values():
                groups = self.group_one_word_differents_in_range(range_mid + 1, range_end, words_with_same_former)
                result.extend(groups)
        if range_start <= range_mid:
            for words_with_same_latter in latter_to_words.values():
                groups = self.group_one_word_differents_in_range(range_start, range_mid, words_with_same_latter)
                result.extend(groups)
        
        return result
            

    def get_word_to_adjacents_dict(self, word_list: list[str]) -> defaultdict[str, set[str]]:
        if not word_list:
            return defaultdict(set)

        groups = self.group_one_word_differents_in_range(0, len(word_list[0]) - 1, word_list)
        word_to_adjacents = defaultdict(set)
        for group in groups:
            group_set = set(group)
            for word in group:
                word_to_adjacents[word] = word_to_adjacents[word] | group_set
        
        return word_to_adjacents

            

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_list_copy = copy.deepcopy(wordList)
        if beginWord not in word_list_copy:
            word_list_copy.append(beginWord)
        
        word_to_adjacents = self.get_word_to_adjacents_dict(word_list_copy)

        visited = set()
        candidates = deque()
        candidates.append(beginWord)
        distance = 0
        while candidates:
            num_cur_candidates = len(candidates)
            distance += 1
            for _ in range(num_cur_candidates):
                word = candidates.popleft()
                if word == endWord:
                    return distance
                if word in visited:
                    continue
                visited.add(word)
                for adj_word in word_to_adjacents[word]:
                    if adj_word in visited:
                        continue
                    candidates.append(adj_word)
        
        NOT_FOUND = 0
        return NOT_FOUND

```