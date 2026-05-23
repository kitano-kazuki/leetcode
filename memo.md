# Step1

## アプローチ

* `len(arr1) = N` , `len(arr2) = M`, `len(arr1[i]) = L`とする
* `arr1`からTrie木を作っておいて, `arr2`の各要素に対してprefixとなっている文字数を測る
* 計算量: O(NL + ML)
    * 実行時間: 10^4 * 10^8 / 10^6 ~= 10^6 sec
* 時間はかかりそうだけど, 他に方法が思いつかないので実装する

## Code1-1 (Trie)

* TLEになると思ったがAC.
* 10^8は桁数としては8桁だからだ！！！

```python
class Node:
    def __init__(self):
        self.children = [None] * 10

class Trie:
    def __init__(self):
        self.root = Node()

    def _get_digits(self, num: int) -> list[int]:
        digits = []
        if num == 0:
            digits.append(0)
        else:
            while num > 0:
                digits.append(num % 10)
                num = num // 10

        digits.reverse()
        return digits


    def add(self, num: int) -> None:
        digits = self._get_digits(num)
        
        node = self.root
        for d in digits:
            if node.children[d] is None:
                node.children[d] = Node()
            node = node.children[d]

        return


    def get_common_prefix_length(self, num: int) -> int:
        digits = self._get_digits(num)

        node = self.root
        length = 0
        for d in digits:
            if node.children[d] is None:
                return length
            length += 1
            node = node.children[d]
        
        return length

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()
        for num1 in arr1:
            trie.add(num1)

        longest_length = float("-inf")
        for num2 in arr2:
            prefix_length = trie.get_common_prefix_length(num2)
            longest_length = max(longest_length, prefix_length)
        
        return longest_length

```