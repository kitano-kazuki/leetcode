from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_word_to_count = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            sorted_word_to_count.setdefault(sorted_word, [])
            sorted_word_to_count[sorted_word].append(word)
        return list(sorted_word_to_count.values())