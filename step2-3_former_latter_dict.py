from collections import deque, defaultdict
import copy

class Solution:
    def get_word_to_adjacents(self, word_list: list[str]) -> dict[str, list[str]]:
        word_to_adjacents = defaultdict(list)

        def register_to_word_to_adjacents_in_range(start_idx, end_idx, candidates):
            if start_idx > end_idx:
                return
            if start_idx == end_idx:
                for i in range(len(candidates)):
                    for j in range(len(candidates)):
                        if i == j:
                            continue
                        word_to_adjacents[candidates[i]].append(candidates[j])
                return
                
            mid_idx = (start_idx + end_idx) // 2
            former_to_matched_words = defaultdict(list)
            latter_to_matched_words = defaultdict(list)
            for candidate in candidates:
                former = candidate[start_idx:mid_idx + 1]
                if former:
                    former_to_matched_words[former].append(candidate)
                latter = candidate[mid_idx + 1:end_idx + 1]
                if latter:
                    latter_to_matched_words[latter].append(candidate)
            
            for former_matched_candidates in former_to_matched_words.values():
                register_to_word_to_adjacents_in_range(mid_idx + 1, end_idx, former_matched_candidates)
            for latter_matched_candidates in latter_to_matched_words.values():
                register_to_word_to_adjacents_in_range(start_idx, mid_idx, latter_matched_candidates)
            return

        register_to_word_to_adjacents_in_range(0, len(word_list[0]) - 1, word_list)
        return word_to_adjacents

    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        copy_word_list = copy.deepcopy(wordList)
        if beginWord not in copy_word_list:
            copy_word_list.append(beginWord)
        
        word_to_adjacents = self.get_word_to_adjacents(copy_word_list)

        visited = set()
        candidates = deque()
        candidates.append(beginWord)
        distance = 0
        while candidates:
            num_candidates = len(candidates)
            distance += 1
            for _ in range(num_candidates):
                cur_word = candidates.popleft()
                if cur_word in visited:
                    continue
                visited.add(cur_word)
                if cur_word == endWord:
                    return distance
                for adj_word in word_to_adjacents[cur_word]:
                    if adj_word in visited:
                        continue
                    candidates.append(adj_word)
        NOT_FOUND = 0
        return NOT_FOUND