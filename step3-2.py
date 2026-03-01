from typing import List


class Solution:
    def calc_hash_by_alphabet_count(self, word, bit_span=7):
        alphabet_to_count ={}
        for alphabet in word:
            alphabet_to_count.setdefault(alphabet, 0)
            alphabet_to_count[alphabet] += 1


        hash_value = 0
        for alphabet, count in alphabet_to_count.items():
            if count > 2 ** bit_span - 1:
                raise ValueError("bit span is too small")

            alphabet_count_value = count << (ord(alphabet) - ord("a")) * bit_span
            hash_value = hash_value | alphabet_count_value
        
        return hash_value


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_to_group = {}
        for word in strs:
            word_hash = self.calc_hash_by_alphabet_count(word)
            hash_to_group.setdefault(word_hash, [])
            hash_to_group[word_hash].append(word)
        return list(hash_to_group.values())

