from typing import List


class Solution:
    def calc_hash_by_alphabet_count(self, word, bit_span=7):
        alphabet_to_count = {}
        for alphabet in word:
            alphabet_to_count.setdefault(alphabet, 0)
            alphabet_to_count[alphabet] += 1
        
        hash_value = 0
        maximum_representable = 2 ** bit_span - 1
        for alphabet, count in alphabet_to_count.items():
            if count > maximum_representable:
                raise ValueError("bit span is too small")
            alphabet_count_value = count << (ord(alphabet) - ord("a")) * bit_span
            hash_value = hash_value | alphabet_count_value

        return hash_value

            
        

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_to_group = {}
        for word in strs:
            hash_value = self.calc_hash_by_alphabet_count(word)
            hash_to_group.setdefault(hash_value, [])
            hash_to_group[hash_value].append(word)
        return list(hash_to_group.values())