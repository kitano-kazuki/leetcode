# Step1

## アプローチ

* 二進数の足し算を行う
* 各位について, carry, a, bの３つを受け取って, carryを次の位に引き継ぎつつ、結果にcarry以外の部分を加える
* 1:28

## Code1-1 (while)

* AC: 6:41
* `a_i`や`b_i`が使わなくなっても引かれ続けているのは若干きになる

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_binary = []
        carry = 0
        a_i = len(a) - 1
        b_i = len(b) - 1
        while 0 <= a_i or 0 <= b_i or carry == 1:
            a_bit = int(a[a_i]) if 0 <= a_i else 0
            b_bit = int(b[b_i]) if 0 <= b_i else 0

            sum_bits = a_bit + b_bit + carry

            sum_binary.append(str(sum_bits % 2))
            carry = sum_bits // 2
            a_i -= 1
            b_i -= 1
        
        return "".join(list(reversed(sum_binary)))

```

# Step2

## Code2-1 (while)

* 変数の命名を変えた
* `summed_bits`と`sum_bits`が混在しているのはわかりにくいけど、ほかにいい名前思いつかず

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        summed_bits = []
        carry = 0
        i_a = len(a) - 1
        i_b = len(b) - 1
        while 0 <= i_a or 0 <= i_b or carry == 1:
            a_bit = int(a[i_a]) if 0 <= i_a else 0
            b_bit = int(b[i_b]) if 0 <= i_b else 0

            sum_bits = a_bit + b_bit + carry

            summed_bits.append(str(sum_bits % 2))
            carry = sum_bits // 2
            if 0 <= i_a:
                i_a -= 1
            if 0 <= i_b:
                i_b -= 1

        
        return "".join(list(reversed(summed_bits)))

```

## 他の人のPRを見る

* https://github.com/ryosuketc/leetcode_grind75/pull/20
* https://github.com/huyfififi/coding-challenges/pull/20
    * `zip_longest`を使うとシンプルで良さそう
    * ほかにも, 最初に`a`や`b`をpaddingする方法がある
        * `"0" * (len(a) - len(b))`としたときに, `len(a) - len(b)`がマイナスだと結果は`""`になる

# Step3

## Code3-2 (zip longest)

* 1:52
* 1:24
* 1:04

```python
import itertools
import collections


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        summed_bits = collections.deque([])
        carry = 0
        for bit_a, bit_b in itertools.zip_longest(reversed(a), reversed(b), fillvalue="0"):
            total = int(bit_a) + int(bit_b) + carry
            summed_bits.appendleft(str(total % 2))
            carry = total // 2
        
        if carry == 1:
            summed_bits.appendleft("1")
        
        return "".join(summed_bits)

```