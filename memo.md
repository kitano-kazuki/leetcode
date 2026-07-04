# Step1

## アプローチ

* 普通にTrie木を実装する

## Code1-1

* AC: 3:37

```python
class Node:
    def __init__(self):
        self.children = [None] * (ord("z") - ord("a") + 1)
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            c_i = ord("z") - ord(c)
            if node.children[c_i] is None:
                node.children[c_i] = Node()
            node = node.children[c_i]
        node.is_word = True
        return


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            c_i = ord("z") - ord(c)
            if node.children[c_i] is None:
                return False
            node = node.children[c_i]
        
        return node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            c_i = ord("z") - ord(c)
            if node.children[c_i] is None:
                return False
            node = node.children[c_i]
        
        return True
```

# Step2

## Code2-1

* 変更なし

```python
class Node:
    def __init__(self):
        self.children = [None] * (ord("z") - ord("a") + 1)
        self.is_word = False

class Trie:

    def __init__(self):
        self.root = Node()


    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            c_i = ord("z") - ord(c)
            if node.children[c_i] is None:
                node.children[c_i] = Node()
            node = node.children[c_i]
        node.is_word = True
        return


    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            c_i = ord("z") - ord(c)
            if node.children[c_i] is None:
                return False
            node = node.children[c_i]
        
        return node.is_word
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            c_i = ord("z") - ord(c)
            if node.children[c_i] is None:
                return False
            node = node.children[c_i]
        
        return True
```

## 他の人のPRを見る

* https://github.com/huyfififi/coding-challenges/pull/35

# Step3

* Trieを使う問題を何回も解いているので今回は省略

