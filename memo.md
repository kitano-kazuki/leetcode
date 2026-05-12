# Step1

## アプローチ

* 一番最初に思いついたもの
    * 被りがない文字列の長さの最大を探したい
    * 被りが出るまで右に伸ばし続けたい.
    * 被りが出てきたら, 被った文字がなくなるまで左側を縮める
    * これを繰り返して一番後ろまで行けばいい
    * O(N)
* できそうだなと思った他のアプローチ
    * 今みている文字と同じ文字が次どこにでてくるかの対応表があるとする
    * 先頭から順番に文字を見ていく
    * 今見ている文字cでi番目とする
    * cが次に出てくるのがj番目だとする
    * 最大で取れる長さは j - i.
    * i ~ jの間にある各文字 xについて
        * xが次に出てくるのが k (< j)だと, i ~ kまでしか被りなしの文字列は作れない
    * スタート地点を決めたのち, ゴール地点が単調減少で手前によってくるということか
    * 計算的には非効率な感じはする
        * 各文字ごとに次に登場するインデックスを保存した表を作る
            * O(N)
        * 文字列の先頭から順番に処理を行う
            * 今見ている文字から次に同じ文字が登場する位置までに存在する文字についてゴール地点がどこになるかを測る
            * O(N^2)
        * 全体ではO(N^2)
* O(N^2)でいいのだったら全ての文字列のスタートとエンドのパターンごとにその間に文字列が何個含まれているか見るアプローチだっていける？？
    * この場合は文字列が何個含まれているか見るためにスタートとエンドの間の文字列を見る必要があるからO(N^3)か
    
## Code1-1

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        right = 1
        longest_length = 1
        chars_in_window = set(s[0])

        # s[left:right]は被りなし
        while right < len(s):

            # right+=1するために左端を縮める
            while s[right] in chars_in_window:
                chars_in_window.remove(s[left])
                left += 1

            chars_in_window.add(s[right]) 
            right += 1
            longest_length = max(longest_length, right - left)

        return longest_length

```

# Step2

## Code2-1

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        # window区間[left,right)
        left = 0
        right = 1
        longest_length = 1
        chars_in_window = set(s[0])

        while right < len(s):

            while s[right] in chars_in_window:
                chars_in_window.remove(s[left])
                left += 1

            chars_in_window.add(s[right]) 
            right += 1
            longest_length = max(longest_length, right - left)

        return longest_length

```

# Step3

## 他の人のコード

### olsen-blue : https://github.com/olsen-blue/Arai60/pull/49

* dictを利用して, 前回登場した文字の一つ次のindexにleftを動かすことができる
    * 定数倍の効率化

### naoto-iwase : https://github.com/naoto-iwase/leetcode/pull/49

* dictやwhileループの代わりに`find`を使用

## 他の人のコメント

* https://github.com/garunitule/coding_practice/pull/47#discussion_r2685035102
    * > 趣味の範囲ですがここはforで回してもいいかもしれません。

# Step4

## Code4-1

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        left = 0
        right = 1
        longest_length = 1
        chars_in_window = set(s[0])

        while right < len(s):
            
            while s[right] in chars_in_window:
                chars_in_window.remove(s[left])
                left += 1
            
            chars_in_window.add(s[right])
            right += 1
            longest_length = max(longest_length, right - left)

        return longest_length


```
