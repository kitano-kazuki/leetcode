from collections import defaultdict, deque
import copy


class Solution:

    def group_one_word_differents_in_range(self, range_start: int, range_end: int, words: list[str]) -> list[set[str]]:
        if range_start > range_end:
            return []
        if range_start == range_end:
            words_set = set(words)
            if len(words_set) == 1:
                return []
            return [words_set]
        
        range_mid = (range_start + range_end) // 2
        former_to_words = defaultdict(list)
        latter_to_words = defaultdict(list)
        for word in words:
            if range_start <= range_mid:
                former = word[range_start:range_mid + 1]
                former_to_words[former].append(word)
            if range_mid + 1 <= range_end:
                latter = word[range_mid + 1:range_end + 1]
                latter_to_words[latter].append(word)
        
        result = []
        if range_mid + 1 <= range_end:
            for words_with_same_former in former_to_words.values():
                groups = self.group_one_word_differents_in_range(range_mid + 1, range_end, words_with_same_former)
                result.extend(groups)
        if range_start <= range_mid:
            for words_with_same_latter in latter_to_words.values():
                groups = self.group_one_word_differents_in_range(range_start, range_mid, words_with_same_latter)
                result.extend(groups)
        
        return result
            

    def get_word_to_adjacents_dict(self, word_list: list[str]) -> defaultdict[str, set[str]]:
        if not word_list:
            return defaultdict(set)

        groups = self.group_one_word_differents_in_range(0, len(word_list[0]) - 1, word_list)
        word_to_adjacents = defaultdict(set)
        for group in groups:
            group_set = set(group)
            for word in group:
                word_to_adjacents[word] = word_to_adjacents[word] | group_set
        
        return word_to_adjacents

            

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
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
        



