# Step1

## アプローチ

* 一回全部の文字列をsetとかに入れる. その後にもう一度先頭から見ていって, setに入っていないものが出てきたら答えとする.
* 後ろから見ていったら２回文字列全体を見る必要がなくなってくれないかな
    * iにおいての仕事の状態
        * 前からの引き継ぎ部分1: `s[i + 1:]`に存在する文字の集合
        * 前からの引き継ぎ部分2: `candidate_non_repeating`として`s[i + 1:]`における最も最初に出現した複数回繰り返さない文字
        * 次に引き継ぐ仕事: `s[i]`を`candidate_non_repeating`にするか, `candidate_non_repeating`をそのまま渡すか. `s[i:]`に含まれる文字の集合.
    * て思ったけど, `aaa`とかで`-1`にならずに`2`になってしまうから最初の単純な方法で実装する

## Code1-1

```python
from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_count = defaultdict(int)
        for c in s:
            char_to_count[c] += 1
        for i in range(len(s)):
            if char_to_count[s[i]] == 1:
                return i
        return -1

```

# Step2

## Code2-1 (変更なし)

```python
from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_count = defaultdict(int)
        for c in s:
            char_to_count[c] += 1
        for i in range(len(s)):
            if char_to_count[s[i]] == 1:
                return i
        return -1

```

# Step3

## Code3-1

```python
from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_count = defaultdict(int)
        for c in s:
            char_to_count[c] += 1
        for i in range(len(s)):
            if char_to_count[s[i]] == 1:
                return i
        return -1

```

# Memo

## 別の解放

### Queue

https://github.com/colorbox/leetcode/pull/29#discussion_r1861430039
> 1-pass で処理するにあたり、文字をキューに入れていき、 2 回以上出現する文字を取り除いていくというやり方を考えました。


### Dict + Set

https://github.com/shining-ai/leetcode/pull/15#issuecomment-1966682629
> ああ、2回以上出てきたやつは、普通の set に、1回のやつは、OrderedDict にいれてみたらどうですか?

https://discord.com/channels/1084280443945353267/1201211204547383386/1211047696862023722
> set使えば綺麗にできましたね。

https://discord.com/channels/1084280443945353267/1195700948786491403/1231538588529852426
> Python 3.7 から dict は順序が保存するようになったので、こういうこともできます。

## Magic number -1

https://github.com/ksaito0629/leetcode_arai60/pull/14/files#r2852198379
> -1 が特殊な値のマジックナンバーになっているのが気になりました。定数として定義すると、読み手にとって読みやすくなると思います。

# Step4

## Code4-2(Dict + Set)

* 今まで見た２つ以上存在する文字をsetに保存
* ユニークになり得る候補を登場した順番にdictに入れておく
* 今見ている文字を確認. 
    * すでに2以上存在していた場合は, スルー
    * 1だった場合は, dictの候補から削除
    * 0だった場合は, dictの候補に追加

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        duplicates = set()
        unique_char_to_idx = {}
        for i in range(len(s)):
            if s[i] in duplicates:
                continue
            if s[i] in unique_char_to_idx:
                del unique_char_to_idx[s[i]]
                duplicates.add(s[i])
                continue
            unique_char_to_idx[s[i]] = i

        if unique_char_to_idx:
            return next(iter(unique_char_to_idx.values()))
        return -1
    
```

* 削除の計算量は`dummy`を配置するだけなのでO(1)

https://github.com/python/cpython/blob/main/Objects/dictobject.c
```
Dummy.  index == DKIX_DUMMY  (combined only)
   Previously held an active (key, value) pair, but that was deleted and an
   active pair has not yet overwritten the slot.
```

https://github.com/python/cpython/blob/c3fb0d9d96902774c08b199dda0479a8d31398a5/Objects/dictobject.c#L2865
```c
dictkeys_set_index(mp->ma_keys, hashpos, DKIX_DUMMY);
```