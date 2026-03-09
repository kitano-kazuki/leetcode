import copy
from typing import Generator
from collections import defaultdict, deque


class Solution:
    def get_word_to_adjacents_dict(self, word_list: list[str]) -> dict[str, list[str]]:

        def yield_one_alphabet_replaced(word: str) -> Generator[str, None, None]:
            for pos in range(len(word)):
                for alphabet_ord in range(ord("a"), ord("z") + 1):
                    alphabet = chr(alphabet_ord)
                    if word[pos] == alphabet:
                        continue
                    yield f"{word[:pos]}{alphabet}{word[pos + 1:]}"

        word_to_adjacents = defaultdict(list)
        
        word_list_set = set(word_list)
        for word in word_list:
            for replaced_word in yield_one_alphabet_replaced(word):
                if replaced_word in word_list_set:
                    word_to_adjacents[word].append(replaced_word)
        
        return word_to_adjacents
                    
                    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_list_copy = copy.deepcopy(wordList)
        if beginWord not in word_list_copy:
            word_list_copy.append(beginWord)
        
        word_to_adjacents = self.get_word_to_adjacents_dict(word_list_copy)

        candidates = deque()
        candidates.append(beginWord)
        visited = set()
        distance = 0
        while candidates:
            distance += 1
            num_cur_candidates = len(candidates)
            for _ in range(num_cur_candidates):
                word = candidates.popleft()
                if word == endWord:
                    return distance
                if word in visited:
                    continue
                visited.add(word)
                for adj_word in word_to_adjacents[word]:
                    if adj_word not in visited:
                        candidates.append(adj_word)
        
        NOT_FOUND = 0
        return NOT_FOUND
            