from collections import deque, defaultdict
import copy

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def construct_word_to_adjacents_dict(word_list):
            word_to_adjacents = defaultdict(set)
            word_set = set(word_list)
            for word in word_list:
                for i in range(len(word)):
                    for alphabet_ord in range(ord("a"), ord("z") + 1):
                        alphabet = chr(alphabet_ord)
                        if word[i] == alphabet:
                            continue
                        ith_replaced = f"{word[:i]}{alphabet}{word[i + 1:]}"
                        if ith_replaced in word_set:
                            word_to_adjacents[word].add(ith_replaced)
            return word_to_adjacents
       
        copy_word_list = copy.deepcopy(wordList)
        if beginWord not in copy_word_list:
            copy_word_list.append(beginWord)
        
        word_to_adjacents = construct_word_to_adjacents_dict(copy_word_list)

        visited = {word : False for word in copy_word_list}
        candidate_queue = deque()
        candidate_queue.append(beginWord)
        distance = 0
        while candidate_queue:
            num_candidates = len(candidate_queue)
            distance += 1
            for _ in range(num_candidates):
                cur_word = candidate_queue.popleft()
                if visited[cur_word]:
                    continue
                visited[cur_word] = True
                if cur_word == endWord:
                    return distance
                if cur_word not in word_to_adjacents:
                    continue
                for adj_word in word_to_adjacents[cur_word]:
                    candidate_queue.append(adj_word)
        
        NOT_FOUND = 0
        return NOT_FOUND