# Step1

## 条件の確認

* stringをintegerに変えるパーサーみたいなものを作る
* stringには数字, 符号, 空白以外も含まれるか?
    * 上記と`.`, ` `, english lettersが含まれる
* leading white spaceが存在するか
    * 存在するから無視する
* leading zeroが存在するか
    * 存在する
* `.`が二つ以上存在するか(数字としてはinvalid)
* `+`や`-`が途中に存在するか
* non_digit characterが来たら読み取りを終了
    * 小数は考慮しなくていい
* 数字の途中に空白が入ることはあるか？入る場合はどう扱うか. 無視 or 終了
* 文字列の長さはどのくらいか
* 32bit の範囲に収める必要がある

## アプローチ

* state machine的に解きたい
    * leading white spaceを読み取る
    * 符号を読み取る
    * leading zeroを読み取る
    * 数字を読み取る
* 計算量: O(N) 
* 実行時間: 200 / 10^6 ~= 2 * 10^-4 sec程度

## Code1-1

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        if not s:
            return 0

        i = 0

        # ignore leading spaces
        while i < len(s) and s[i] == " ":
            i += 1

        if i == len(s):
            return 0

        # read sign
        is_positive = True
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            is_positive = False
            i += 1
        
        # read digits
        is_leading_zeroes = True
        number = 0
        while i < len(s) and s[i].isdigit():
            # ignore leading zeroes
            if is_leading_zeroes:
                if s[i] == "0":
                    i += 1
                    continue
                else:
                    is_leading_zeroes = False
                    continue
            
            number = number * 10 + int(s[i])
            i += 1

        
        if is_positive:
            return min(number, 2**31 - 1)
        else:
            return -1 * min(number, 2**31)

```

# Step2

## Code2-1

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0

        # ignore leading white spaces
        while i < len(s) and s[i] == " ":
            i += 1

        if i == len(s):
            return 0

        # read sign
        is_negative = False
        if s[i] in ["+", "-"]:
            if s[i] == "-":
                is_negative = True
            i += 1

        
        # read digits
        parsing_leading_zeroes = True
        number = 0
        while i < len(s) and s[i].isdigit():
            # ignore leading zeroes
            if parsing_leading_zeroes:
                if s[i] == "0":
                    i += 1
                else:
                    parsing_leading_zeroes = False
            # after leading zeroes
            else:
                number = number * 10 + int(s[i])
                i += 1
        
        if is_negative:
            return -1 * min(number, 2**31)
        else:
            return min(number, 2**31 - 1)

```

## 他の人のコードを見る

* https://github.com/olsen-blue/Arai60/pull/60
    * INT_MAXを超えた時点で, `return`するようにしたい
        * 無限に値が増え続けてしまう(余計なメモリを使用する)
* https://github.com/naoto-iwase/leetcode/pull/60
    * `is_digit`だと, 丸数字や上付き数字でもTrueになる
    * `is_dicimal`が今回だと厳密に数字を表せる
        * あるいは`ord`を使うか
    * pythonだと問題ないが, overflowを考慮する場合は, 値を計算する前に条件を確認する必要がある
    * 以下のものがわかりやすかった

```python
  def _is_overflow(self, sign: int, value: int, digit: int) -> bool:
        if sign == 1:
            if value > MAX_INT // 10:
                return True
            if value == MAX_INT // 10 and digit > MAX_INT % 10:
                return True
        else:
            if value < (MIN_INT + 9) // 10:
                return True
            if value == (MIN_INT + 9) // 10 and digit > (10 - MIN_INT % 10) % 10:
                return True
        return False
```

* https://github.com/mamo3gr/arai60/pull/54
    * 以下のコメントが参照されていた
        * > 他の(オーバーフローが)問題になるような言語だと、標準ライブラリーにそういう関数があることが多いというのも意識してもいいかもしれません まあ、要は自分で作らないべきものであるということです。

# Step3

## Code3-1

* 1st: 5:32
* 2nd: 3:05
* 3rd: 6:57

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0

        while i < len(s) and s[i] == " ":
            i += 1 
        if i == len(s):
            return 0
        
        sign = 1
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1

        is_leading_zeroes = False
        num = 0
        while i < len(s) and s[i].isdecimal():
            if is_leading_zeroes:
                if s[i] == "0":
                    i += 1
                    continue
                is_leading_zeroes = False
                continue

            num = num * 10 + (ord(s[i]) - ord("0"))
            if sign == 1 and num > 2**31 - 1:
                return 2**31 - 1
            if sign == -1 and num > 2**31:
                return -2**31

            i += 1

        return sign * num


```