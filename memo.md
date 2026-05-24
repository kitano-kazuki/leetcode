# Step1

## アプローチ

* 一番最初に思いついたもの
    * 先頭からまず, 英数字以外を削除 -> 前から読んだ文字列と後ろから読んだ文字列の一致を比較
* palindromeということは, 真ん中から文字列を見ればいい
    * 最初の文字列の削除もしなくていい(無視すればいい)
* ここまで 1:53

## Code1-1

* AC: 22:31
* 真ん中から左右に広げてみる方法を考えていたが, 文字列以外を無視する時に, 与えられた`s`の長さの真ん中を取るのは良くなかった

```python
class Solution:
    def is_alphanumeric(self, ch: str) -> bool:
        if ord("0") <= ord(ch) <= ord("9"):
            return True
        if ord("a") <= ord(ch) <= ord("z") or ord("A") <= ord(ch) <= ord("Z"):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        n = len(s)

        left = 0
        right = n - 1
        while left < right:
            if not self.is_alphanumeric(s[left]):
                left += 1
                continue
            if not self.is_alphanumeric(s[right]):
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
                continue
            return False

        return True
        
```

# Step2

## Code2-1

* 変更なし

```python
class Solution:
    def is_alphanumeric(self, ch: str) -> bool:
        if ord("0") <= ord(ch) <= ord("9"):
            return True
        if ord("a") <= ord(ch) <= ord("z") or ord("A") <= ord(ch) <= ord("Z"):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        n = len(s)

        left = 0
        right = n - 1
        while left < right:
            if not self.is_alphanumeric(s[left]):
                left += 1
                continue
            if not self.is_alphanumeric(s[right]):
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
                continue
            return False

        return True
        
```

## Code2-2

```python
class Solution:
    def is_alphanumeric(self, ch: str) -> bool:
        if ord("0") <= ord(ch) <= ord("9"):
            return True
        if ord("a") <= ord(ch) <= ord("z") or ord("A") <= ord(ch) <= ord("Z"):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        alphanumerics = []
        for ch in s:
            if self.is_alphanumeric(ch):
                alphanumerics.append(ch.lower())
        
        if alphanumerics == list(reversed(alphanumerics)):
            return True
        else:
            return False

```

## 他の人のPRを見る

* https://github.com/TaisukeFujise/leetcode_tafujise/pull/10
    * 自分のcode2-1と同じ
* https://github.com/naoto-iwase/leetcode/pull/63
    * `isalnum`を避けたいという感覚が一緒.
        * 自分は`ord`を使ったが, このPRは`re`を使っている
* https://github.com/ryosuketc/leetcode_grind75/pull/5
* https://github.com/huyfififi/coding-challenges/pull/5

# Step3

## Code3-1

* 1st: 3:30
* 2nd: 2:06
* 3rd: 1:01

```python
class Solution:
    def is_alphanumeric(self, ch: str) -> bool:
        if ord("0") <= ord(ch) <= ord("9"):
            return True
        if ord("a") <= ord(ch) <= ord("z") or ord("A") <= ord(ch) <= ord("Z"):
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        left = 0
        right = len(s) - 1
        while left < right:
            if not self.is_alphanumeric(s[left]):
                left += 1
                continue
            if not self.is_alphanumeric(s[right]):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        
        return True
```