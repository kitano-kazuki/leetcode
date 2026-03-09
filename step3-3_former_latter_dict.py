from collections import defaultdict, deque
import copy


class Solution:

    def group_one_word_different_words_in_range(self, word_list: list[str], check_range_left: int, check_range_right: int) -> list[list[str]]:
        if check_range_left == check_range_right:
            return [word_list]
        
        check_range_mid = (check_range_left + check_range_right) // 2
        former_half_to_words = defaultdict(list)
        latter_half_to_words = defaultdict(list)
        for word in word_list:
            if check_range_left <= check_range_mid:
                former_half = word[check_range_left:check_range_mid + 1]
                former_half_to_words[former_half].append(word)
            if check_range_mid + 1 <= check_range_right:
                latter_half = word[check_range_mid + 1:check_range_right + 1]
                latter_half_to_words[latter_half].append(word)
        
        result = []
        if check_range_mid + 1 <= check_range_right:
            for words_with_same_former in former_half_to_words.values():
                if len(words_with_same_former) == 1:
                    continue
                groups = self.group_one_word_different_words_in_range(words_with_same_former, check_range_mid + 1, check_range_right)
                result.extend(groups)
        if check_range_left <= check_range_mid:
            for words_with_same_latter in latter_half_to_words.values():
                if len(words_with_same_latter) == 1:
                    continue
                groups = self.group_one_word_different_words_in_range(words_with_same_latter, check_range_left, check_range_mid)
                result.extend(groups)
        
        return result


    def get_word_to_adjacents_dict(self, word_list: list[str]) -> dict[str, set[str]]:
        one_word_different_groups = self.group_one_word_different_words_in_range(word_list, 0, len(word_list[0]) - 1)

        word_to_adjacents = defaultdict(set)
        for group in one_word_different_groups:
            group_set = set(group)
            for word in group_set:
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
        



