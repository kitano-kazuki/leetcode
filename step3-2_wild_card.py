from typing import Generator
from collections import defaultdict, deque
import copy


class Solution:
    def get_word_to_adjacents_dict(self, word_list: list[str]) -> dict[str, list[set]]:

        def yield_pattern_from_word(word: str) -> Generator[tuple[str, str], None, None]:
            for pos in range(len(word)):
                yield (word[:pos], word[pos + 1:])
        
        pattern_to_words = defaultdict(set)
        for word in word_list:
            for pattern in yield_pattern_from_word(word):
                pattern_to_words[pattern].add(word)
        
        word_to_adjacents = defaultdict(set)
        for word in word_list:
            for pattern in yield_pattern_from_word(word):
                word_to_adjacents[word] = word_to_adjacents[word] | pattern_to_words[pattern]
        
        return word_to_adjacents
        

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_list_copy = copy.deepcopy(wordList)
        if beginWord not in word_list_copy:
            word_list_copy.append(beginWord)

        word_to_adjacents = self.get_word_to_adjacents_dict(word_list_copy)
        
        visited = set() 
        candidates = deque()
        candidates.append(beginWord)
        distance = 0
        while candidates:
            num_cur_candidates = len(candidates)
            distance += 1
            for _ in range(num_cur_candidates):
                word = candidates.popleft()
                if word == endWord:
                    return distance
                if word in visited:
                    continue
                visited.add(word)
                for adj_word in word_to_adjacents[word]:
                    if adj_word in visited:
                        continue
                    candidates.append(adj_word)
        
        NOT_FOUND = 0
        return NOT_FOUND