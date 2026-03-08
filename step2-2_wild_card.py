from collections import deque, defaultdict
import copy

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def construct_word_to_adjacents_dict(word_list):
            # MEMO: 実行時にforのwordが取り込まれそうで怖いからwに変数名を変えた
            get_patterns = lambda w : [ (w[:i], w[i + 1:]) for i in range(len(w))]
            pattern_to_words = defaultdict(list)
            for word in word_list:
                for pattern in get_patterns(word):
                    pattern_to_words[pattern].append(word)

            word_to_adjacents = defaultdict(list)
            for word in word_list:
                for pattern in get_patterns(word):
                    adj_words = pattern_to_words[pattern]
                    # MEMO: extendの時に後追加されるものはdeepcopyなのか？？？今回はshallowでも影響ないけど
                    word_to_adjacents[word].extend(adj_words)
            
            return word_to_adjacents
        
        word_list_copy = copy.deepcopy(wordList)
        if beginWord not in word_list_copy:
            word_list_copy.append(beginWord)

        word_to_adjacents = construct_word_to_adjacents_dict(word_list_copy)

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
