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
    * 二つ目のアルゴリズムを検討.
        * key = 1文字無くしたタプル, value = 1文字無くす前の文字列のidx(あるいは文字列自体)リスト
        * n個のinputの各文字について, 
            * 平均的な場合では, n個の文字列のうち,同じ箇所が1文字違いになるのは (n / k)個とする
            * １文字を無くしたタプルをdictに追加. ... k種類のタプルが生成されるのでO(k)
            * 追加するものがdictに存在しなければ特に何もしない
            * 追加するものがすでにdictにあった場合, dictのvalueに存在しているものたちは1文字違いの文字たち
                * dictのvalueのリストの要素たちが1文字違いと記録する
                    * dictのvalueのリストの長さ
                        * 最悪の場合はn個の文字列が全て同じ箇所で1文字違いの場合で, nの長さになっている
                        * 平均の場合は, 一番長くて n / k
                * **追記: リストの長さ分何かの処理をしないといけないわけではないので, ここの計算量は考える必要がなかった**
            * トータルで, O(n * k * (n / k))で O(n^2)はかかりそう(最悪の場合はO(k * n^2))
                * 参考サイトのやつの2個目は, 個数を数えるだけなら O(n * k^2)で抑えられそうだけど, 今回みたいに具体的にどの文字列同士が1文字離れか見るならO(n * k^2)は無理じゃない？？
                * **追記: トータルは O(n * k^2)にできる**
    * 一つ目のアルゴリズムを検討
        * 文字列の長さをk
        * 前半の文字列の種類, 後半の文字列の種類ともにp種類ずつだとする. 各バケットにn / p文字はいることを想定
        * key: 前半の文字列, value: 後半の文字列のリストの辞書を用意
        * 各文字列について, 
            * valueのリストに含まれる各文字列と, 今見ている文字列が1文字違いかどうかを見る
        * keyを後半の文字列にしたものも行う
        * トータルでは, 2 * (n + n * (n / (2p)) * (k / 2))なので O(n^2 * k / p)
        * pがnに近い場合は, O(nk)となるが, 今回の問題設定だと1文字差の文字列しか与えられないから, O(n^2 * k)の方が近い見積りになりそう
        * 再帰を使って最適化することはできるみたい
            * でも最悪の場合は結局, 一つのバケットにn個の要素が残るから, 全てのペアを考えるってなったら, O(nklogk + n^2)
            * ペアを出す以上, 同じ場所で1文字違いのペアがO(n^2)あるからこれより改善されることはない
            * でもO(n^2)までは改善できるってこと？？ だしこの方法だったらO(n^2)
            * でも直感的には, O(n^2 * k)より改善はできなさそう
                * 今回の場合, 前半部分をkeyにする事例だけ考えたけど, 後半部分が異なる場合もあるもんな
                * prefixが必ず一緒という制約下ではO(n^2)にはなりそう
            * **追記: 計算量はO(n * k^2)だと思う**
                * 最悪のケースを考えると, 最後の１文字以外が全部同じものがn個ある
                * １回の処理ごとに, 文字列の長さは半分になるが, 一つのkeyにn個要素がある状態は変わらない
                * 文字列の長さが1になるまでには logk 回同じ処理を行う必要がある
                * この時点で, 前半部分->文字列のリストという辞書は全部作られた
                * 改めて, 次の処理を考えた時に, 前半部分->文字列のリストという辞書をうまく使って, 位置文字違いのやつらをグループにしたい
                    * ある文字列xに対して, そのグループを知りたければ, 
                        * 文字列xの前半部分をkeyとしてそのvalueを見ることを繰り返す
                        * **logk回操作を行えば, 対応するvalueの一致を見ることなく, それがグループだとわかる**
                            * 前半部分が長さ1の時, そのvalueに入っているものは必ず1文字違い
                        * １回の操作では, 文字列のハッシュ値を見るのにO(k)かかる
                        * でもxの全てのパターンを網羅するには, `2^(log_2(k) - 1)`回調べる必要がある???
                        * つまり, 文字列xに対してグループを知るには O(k * 2^(log2_(k) - 1))
                    * そしたら計算量はO(n * k * 2^(log_2(k))) = O(n * k^2)になりそうだな
                    * ワイルドカードの方法とも一致したし, あっていそう
    * じゃあpythonだと, 今回のleetcodeの制約で, 全ペアを列挙するのは無理じゃん
        * **追記: 上記考察より, O(n * k^2)なのでできそう**
    * でも, 今回はtransformation sequenceだけを考えればいいから前ペアを必ずしも列挙する必要はなさそう
        * 次に移れる文字列を探していくようにする
            * 最短経路で目的地に行くことを考えた時,  abc -> abd -> abe みたいになることはないから最悪計算量になることはない

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
