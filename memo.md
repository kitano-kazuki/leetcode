# Step1

## アプローチ

* `magazine`に含まれるワードを使って`ransomNote`が作れるならTrueを返す
* `magazine`に含まれるワードの数分残機があって、`ransomNote`の各単語に遭遇するたびにそれを減らしていけばいいかな
* `magazine`の長さをM
* `ransomNote`の長さをNとすると
* 計算量は, O(M + N)
* 実行時間は, 10^5 * 2 / 10^6 ~= 0.1 sec程度
* 使用メモリは,
    * dictオブジェクトを作って, 文字の種類ごとに個数をカウントする
    * intの28byteと, 文字の個数26個分程度かな？？
    * 28 * 26 ~= 900 bytes
* ここまで 3:21

## Code1-1

* AC: 1:25

```python
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_to_count = collections.defaultdict(int)
        for c in magazine:
            char_to_count[c] += 1
        
        for c in ransomNote:
            if c not in char_to_count:
                return False
            if char_to_count[c] == 0:
                return False
            char_to_count[c] -= 1
        
        return True
                
```

# Step2

## Code2-1 (Dict)

* 変更なし

```python
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_to_count = collections.defaultdict(int)
        for c in magazine:
            char_to_count[c] += 1
        
        for c in ransomNote:
            if c not in char_to_count:
                return False
            if char_to_count[c] == 0:
                return False
            char_to_count[c] -= 1
        
        return True

```

## Code2-2 (Counter)

```python
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = collections.Counter(magazine)
        for c in ransomNote:
            if c not in counter:
                return False
            if counter[c] == 0:
                return False
            counter[c] -= 1
        return True
                
```

## 他の人のPRを見る

* https://github.com/tom4649/Coding/pull/66
    * 方針は同じ
    * `dict.get()`を使うことで, `if c not in dict`と`if dict[c] == 0`を同時に判定できる
    * 制約で英語小文字だけであることから, 長さ26の配列を用意してもいい
* https://github.com/ryosuketc/leetcode_grind75/pull/15
* https://github.com/huyfififi/coding-challenges/pull/15

# Step3

## Code3-1

* 1st: 0:48
* 2nd: 0:31
* 3rd: 0:31

* そもそもdefaultdict使っているから, `char_to_count.get(c, 0)`としなくていい

```python
import collections


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_to_count = collections.defaultdict(int)
        for c in magazine:
            char_to_count[c] += 1
        
        for c in ransomNote:
            if char_to_count[c] == 0:
                return False
            char_to_count[c] -= 1
        
        return True

```