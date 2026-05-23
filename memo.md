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

# Step2

## Code2-1 (Trie)

```python
class IntTrieNode:
    def __init__(self):
        self.children = [None] * 10

class IntTrieTree:
    def __init__(self):
        self.root = IntTrieNode()

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
                node.children[d] = IntTrieNode()
            node = node.children[d]

        return


    def get_longest_common_prefix_length(self, num: int) -> int:
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
        trie_tree = IntTrieTree()

        for num1 in arr1:
            trie_tree.add(num1)

        max_prefix_length = float("-inf")
        for num2 in arr2:
            prefix_length = trie_tree.get_longest_common_prefix_length(num2)
            max_prefix_length = max(max_prefix_length, prefix_length)
        
        return max_prefix_length

```

## Code2-2 (Hash)

* Hashを使う方法もあるらしい
* `arr1`から存在しうる`prefix`をすべて`set`に追加する
    * O(Nd^2) => O(N)
* `arr2`の存在しうる`prefix`が`set`にあるかどうかを探る
    * O(Md^2) => O(M)

```python
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        for num1 in arr1:
            num1_str = str(num1)
            for i in range(1, len(num1_str) + 1):
                prefixes.add(num1_str[:i])
        
        longest_common_prefix = 0
        for num2 in arr2:
            num2_str = str(num2)
            for i in range(len(num2_str), 0, -1):
                if num2_str[:i] not in prefixes:
                    continue
                longest_common_prefix = max(longest_common_prefix, i)
                break
        
        return longest_common_prefix

```

# Step3

## Code3-1 (Trie)

* 1st: 5:26
* 2nd: 4:22
* 3rd: 3:29

```python

class Node:
    def __init__(self):
        self.children = [None] * 10


class Trie:
    def __init__(self):
        self.root = Node()

    def _get_digits(self, num: int) -> list[int]:
        if num == 0:
            return [0]
        
        digits_reversed = []
        while num > 0:
            digits_reversed.append(num % 10)
            num //= 10
        
        return reversed(digits_reversed)


    def add(self, num: int) -> None:
        digits = self._get_digits(num)

        node = self.root
        for d in digits:
            if node.children[d] is None:
                node.children[d] = Node()
            node = node.children[d]

        return

    
    def get_longest_common_prefix_length(self, num: int) -> int:
        digits = self._get_digits(num)

        node = self.root
        prefix_length = 0
        for d in digits:
            if node.children[d] is None:
                return prefix_length
            node = node.children[d]
            prefix_length += 1
        
        return prefix_length


class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        trie = Trie()

        for num1 in arr1:
            trie.add(num1)
        
        max_prefix_length = 0 
        for num2 in arr2:
            prefix_length = trie.get_longest_common_prefix_length(num2)
            max_prefix_length = max(max_prefix_length, prefix_length)
        
        return max_prefix_length


```
