from typing import List


class Solution:
    def calculate_hash_by_alphabet_count(self, word):

        def calculate_alphabet_count_value(alphabet, count):
            bit_span = 7
            bit_maximum = 2 ** bit_span - 1
            if count < 0 or count > bit_maximum:
                raise ValueError(f"count: {count} must be zero or positive and less than or equal to {bit_maximum}")

            a_ord = ord("a")
            z_ord = ord("z")
            alphabet_ord = ord(alphabet)
            if alphabet_ord < a_ord or z_ord < alphabet_ord:
                raise ValueError(f"alphabet: {alphabet} must be small english letter")

            position = alphabet_ord - a_ord
            return count << position * bit_span


        alphabet_to_count = {}
        for alphabet in word:
            alphabet_to_count.setdefault(alphabet, 0)
            alphabet_to_count[alphabet] += 1

        hash = 0
        for alphabet, count in alphabet_to_count.items():
            hash += calculate_alphabet_count_value(alphabet, count)
        return hash


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_to_group = {}
        for word in strs:
            hash_value = self.calculate_hash_by_alphabet_count(word)
            hash_to_group.setdefault(hash_value, [])
            hash_to_group[hash_value].append(word)
        return list(hash_to_group.values())

            