# Step1

## アプローチ

* ソートしたものが同じかどうかをみる: O(NlogN)
* その文字列に含まれている文字の個数が同じかどうかみる: O(N)

## Code1-1(Count)

```python
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False

        s_char_to_count = collections.defaultdict(int)
        for ch in s:
            s_char_to_count[ch] += 1
        
        t_char_to_count = collections.defaultdict(int)
        for ch in t:
            t_char_to_count[ch] += 1
        
        for s_ch, s_count in s_char_to_count.items():
            if s_ch not in t_char_to_count:
                return False
            if t_char_to_count[s_ch] != s_count:
                return False
        
        for t_ch, t_count in t_char_to_count.items():
            if t_ch not in s_char_to_count:
                return False
            if s_char_to_count[t_ch] != t_count:
                return False

        return True

```


## Code1-2(Sort)

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        
```

# Step2

## Code2-1(Count)

```python
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False

        s_char_to_count = collections.defaultdict(int)
        for ch in s:
            s_char_to_count[ch] += 1
        
        t_char_to_count = collections.defaultdict(int)
        for ch in t:
            t_char_to_count[ch] += 1

        s_chars = set(s_char_to_count.keys())
        t_chars = set(t_char_to_count.keys())

        if s_chars != t_chars:
            return False
        
        for s_c in s_chars:
            if s_char_to_count[s_c] != t_char_to_count[s_c]:
                return False

        return True

```

## 他の人のPRをみる

* https://github.com/docto-rin/leetcode/pull/65
    * `lowercase English lettersなので、長さ26の配列でカウントする`実装をしていた
    * これも解法の幅として最初に出しておきたかった
        * Follow-upをみてunicodeへの対応を考えた時に, dictがいいとしたかった
    * dictの`__eq__`は, 同じkey-valueペアを持っているかどうかを見てくれるみたい
    * sに関するdictの値をtを見ながら減らしていくアプローチもしている
* https://github.com/ryosuketc/leetcode_grind75/pull/7
    * 最初に文字数が等しいかどうか見ていれば, sの文字カウントをした辞書の各エントリをtの辞書と比較するだけでいい
        * `s="a", t="ab"`みたいな場合は最初に弾かれる
* https://github.com/huyfififi/coding-challenges/pull/7
    * > `s`と`t`で別々の`dict`を持つのではなく、同じ`dict`に対して`s`の文字は`+1`、`t`の文字は`-1`し、最後に全てのkeyのvalueが`0`であることを確認する方法。これならメモリ空間の使用量を削減できる
    * > 同じ文字でもUnicodeでは複数の表現を持つ場合があり、こうした場合 Unicode 正規化を行うといいらしい。

# Step3

## Code3-1(Count)

```python
import collections


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def get_count_dict(letters: str) -> dict[str, int]:
            char_to_count = collections.defaultdict(int)
            for ch in letters:
                char_to_count[ch] += 1
            return char_to_count

        s_char_to_count = get_count_dict(s)
        t_char_to_count = get_count_dict(t)
        return s_char_to_count == t_char_to_count
        
```