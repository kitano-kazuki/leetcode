from collections import defaultdict, deque
import copy


class Solution:

    def group_one_word_differents(self, word_list: list[str]) -> list[list[str]]:
        
        def get_groups_by_narrowing_down_search_length_if_half_same(start_pos: int, end_pos: int, words_to_check: list[str]) -> list[list[str]]:
            if start_pos == end_pos:
                return [words_to_check]
            
            former_half_to_words = defaultdict(list)
            latter_half_to_words = defaultdict(list)
            mid_pos = (start_pos + end_pos) // 2
            for word in words_to_check:
                if mid_pos - start_pos >= 0:
                    former_half = word[start_pos:mid_pos + 1]
                    former_half_to_words[former_half].append(word)
                if end_pos - (mid_pos + 1) >= 0:
                    latter_half = word[mid_pos + 1:end_pos + 1]
                    latter_half_to_words[latter_half].append(word)
            
            result = []
            for former_same_words in former_half_to_words.values():
                if not mid_pos + 1 <= end_pos:
                    continue
                if len(former_same_words) == 1:
                    continue
                groups = get_groups_by_narrowing_down_search_length_if_half_same(mid_pos + 1, end_pos, former_same_words)
                result.extend(groups)
            for latter_same_words in latter_half_to_words.values():
                if not start_pos <= mid_pos:
                    continue
                if len(latter_same_words) == 1:
                    continue
                groups = get_groups_by_narrowing_down_search_length_if_half_same(start_pos, mid_pos, latter_same_words)
                result.extend(groups)
            
            return result

        return get_groups_by_narrowing_down_search_length_if_half_same(0, len(word_list[0]) - 1, word_list)

    def get_word_to_adjacents_dict(self, word_list: list[str]) -> dict[str, set[str]]:
        one_word_different_groups = self.group_one_word_differents(word_list)

        word_to_adjacents = defaultdict(set)
        for group in one_word_different_groups:
            for word in group:
                word_to_adjacents[word] = word_to_adjacents[word].union(set(group))

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
        



