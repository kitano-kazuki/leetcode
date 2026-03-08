from typing import List
from collections import deque
import copy


class Node:
    def __init__(self, id : int, nexts : List[Node]):
        self.id = id
        self.nexts = nexts
    
    def __repr__(self)        :
        return f"Node(id={self.id})"

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def is_one_word_difference(word1, word2):
            if len(word1) != len(word2):
                raise ValueError(f"The length of {word1} and {word2} are different")
            difference_count = 0
            word_len = len(word1)
            for i in range(word_len):
                if word1[i] == word2[i]:
                    continue
                difference_count += 1
            return difference_count == 1

        start_node_id = None
        end_node_id = None
        id_to_node = {}
        for word1_id in range(len(wordList)):
            if wordList[word1_id] == beginWord:
                start_node_id = word1_id
            elif wordList[word1_id] == endWord:
                end_node_id = word1_id

            if word1_id not in id_to_node:
                id_to_node[word1_id] = Node(word1_id, [])
            word1_node = id_to_node[word1_id]
            for word2_id in range(word1_id + 1, len(wordList)):
                if not is_one_word_difference(wordList[word1_id], wordList[word2_id]):
                    continue
                if word2_id not in id_to_node:
                    id_to_node[word2_id] = Node(word2_id, [])
                word2_node = id_to_node[word2_id]
                word1_node.nexts.append(word2_node)
                word2_node.nexts.append(word1_node)


        copy_word_list = copy.deepcopy(wordList)
        if start_node_id is None:
            copy_word_list.extend([beginWord])
            start_node_id = len(copy_word_list) - 1
            start_node = Node(start_node_id, [])
            id_to_node[start_node_id] = start_node
            for word_id in range(len(wordList)):
                if not is_one_word_difference(beginWord, copy_word_list[word_id]):
                    continue
                start_node.nexts.append(id_to_node[word_id])
                id_to_node[word_id].nexts.append(start_node)

        total_words = len(copy_word_list)                

        visited = [False] * total_words
        candidate_nodes = deque()
        candidate_nodes.append(id_to_node[start_node_id])

        distance = 0
        while candidate_nodes:
            num_nodes = len(candidate_nodes)
            distance += 1
            for _ in range(num_nodes):
                node = candidate_nodes.popleft()
                if node.id == end_node_id:
                    return distance
                if visited[node.id]:
                    continue
                visited[node.id] = True
                for connected_node in node.nexts:
                    if visited[connected_node.id]:
                        continue
                    candidate_nodes.append(connected_node)
        
        NOT_FOUND = 0
        return NOT_FOUND