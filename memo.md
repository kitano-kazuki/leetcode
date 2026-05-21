# Step1

## アプローチ

* sを先頭から見る. tの中に今見ているsの文字と一致しているものがあったら, sの次の文字を見る
* この方法だと, tの中にsのi番目と一致するものが複数出てきた場合にどれを採用するかで場合分けが生じる
    * でも結局出てくる順番だけが大切だから, べつに場合分けをする必要もなさそう
    * 最初に出てきたものを採用して解に至らなくなることはない

## Code1-1 (two poitner)

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        if not s:
            return True

        s_i = 0
        for t_i in range(len(t)):
            if s[s_i] != t[t_i]:
                continue
            s_i += 1
            if s_i == len(s):
                return True

        return False

```

# Step2

## Code2-1 (two pointer)

* `t_i`は要素アクセスでしか使われないので, インデックスを使わずに文字でループを回した

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        if not s:
            return True

        s_i = 0
        for c in t:
            if s[s_i] != c:
                continue
            s_i += 1
            if s_i == len(s):
                return True

        return False

```

## 他の人のコードを見る

* https://github.com/olsen-blue/Arai60/pull/58
    * 同じ解法
        * 無限ループや再帰でも実装している
* https://github.com/naoto-iwase/leetcode/pull/58
    * もし単一のtに, 複数のsが与えられたらというフォローアップにも取り組んでいる
    * findを使ってネイティブコードで動く解法も実装している

# Step3

## Code3-1 (two pointer)

```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        if not s:
            return True

        s_i = 0
        for ch in t:
            if s[s_i] != ch:
                continue
            s_i += 1
            if s_i == len(s):
                return True
        
        return False

```

