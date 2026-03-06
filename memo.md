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

