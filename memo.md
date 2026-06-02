# Step1

## アプローチ

* 文字の個数と種類があって, それをもとに作れる回文の長さの最長をしりたい
* 奇数個の文字の場合は, 真ん中に置くことで回文にすることができる
* 偶数個の文字は常に回文の要素として活用できる
* 奇数個の文字がない場合は, 偶数個の文字すべてを使ってつくるのが最長
* 奇数個の文字が1個の場合はそれを使っていい
* 奇数個の文字が複数ある場合は、そのうちの偶数個を基本的には使う
* 一個だけ真ん中に置いていいから, 最後に+1できる可能性がある
* `a2, b3, d1` -> a2とb2と+1 => 長さ5
* 4:30

## Code1-1

* AC: 8:02

```python
import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0
        counter = collections.Counter(s)

        odd_exists = False
        longest_palindrome = 0
        for count in counter.values():
            if count % 2 == 1:
                odd_exists = True
                longest_palindrome += count - 1
            else:
                longest_palindrome += count
        
        if odd_exists:
            longest_palindrome += 1
        
        return longest_palindrome

```

# Step2

## Code2-1

* 変更なし

```python
import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        if not s:
            return 0

        counter = collections.Counter(s)

        odd_exists = False
        longest_palindrome = 0
        for count in counter.values():
            if count % 2 == 1:
                odd_exists = True
                longest_palindrome += count - 1
            else:
                longest_palindrome += count
        
        if odd_exists:
            longest_palindrome += 1
        
        return longest_palindrome

```

## 他の人のPRを見る

* https://github.com/huyfififi/coding-challenges/pull/17
    * ほぼ一緒のコード書いている
    * if文を減らす工夫として以下のようなものも提案されていた
        ```python
        palindrome_length += count - count % 2
        has_odd_count |= count % 2 == 1
        ```
* https://github.com/ryosuketc/leetcode_grind75/pull/17

# Step3

## Code3-1

* 1:15
* 0:46
* 0:45

```python
import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        
        odd_count_exists = False
        palindrome_length = 0
        for count in counter.values():
            if count % 2 == 1:
                odd_count_exists = True
            palindrome_length += (count // 2) * 2

        if odd_count_exists:
            palindrome_length += 1
        
        return palindrome_length
            
```