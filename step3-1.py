from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_word_to_group = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            sorted_word_to_group.setdefault(sorted_word, [])
            sorted_word_to_group[sorted_word].append(word)
        return list(sorted_word_to_group.values())

