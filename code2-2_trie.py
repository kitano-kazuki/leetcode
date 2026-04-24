class Node:
    def __init__(self):
        self.children = [None] * (ord("z") - ord("a") + 1)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, s: str) -> None:
        node = self.root
        for c in s:
            index = self._get_alphabet_index(c)
            if node.children[index] is None:
                node.children[index] = Node()
            node = node.children[index]
        node.is_word = True
        return

    def get_word_end_indices(self, word: str, start: int) -> list[int]:
        node = self.root
        end_indices = []
        for i in range(start, len(word)):
            index = self._get_alphabet_index(word[i])
            if node.children[index] is None:
                return end_indices
            node = node.children[index]
            if node.is_word:
                end_indices.append(i)
        return end_indices

    def _get_alphabet_index(self, char: str) -> int:
        return ord("z") - ord(char)


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.add(word)
        
        is_segmentable = [False] * (len(s) + 1)
        is_segmentable[0] = True
        for i in range(len(s)):
            if not is_segmentable[i]:
                continue
            word_end_indices = trie.get_word_end_indices(s, i)
            for end_index in word_end_indices:
                is_segmentable[end_index + 1] = True

        return is_segmentable[len(s)]
