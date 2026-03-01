from typing import List


class Solution:
    def calculate_hash(self, word):

        # Calculate value representing (alphabet, count) pair.
        def calculate_value(alphabet, count):
            seven_bit_maximum = 0b1111111
            if count < 0 or count > seven_bit_maximum:
                raise ValueError(f"count: {count} must be zero or positive and less than or equal to {seven_bit_maximum}")

            a_ord = ord("a")
            z_ord = ord("z")
            alphabet_ord = ord(alphabet)
            if alphabet_ord < a_ord or z_ord < alphabet_ord:
                raise ValueError(f"alphabet: {alphabet} must be small english letter")

            position = alphabet_ord - a_ord
            num_bit_for_each = 7
            return count << position * num_bit_for_each


        chr_to_count = {}
        for chr in word:
            chr_to_count.setdefault(chr, 0)
            chr_to_count[chr] += 1

        hash = 0
        for chr, count in chr_to_count.items():
            hash += calculate_value(chr, count)
        return hash


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_to_group = {}
        for word in strs:
            hash_value = self.calculate_hash(word)
            hash_to_group.setdefault(hash_value, [])
            hash_to_group[hash_value].append(word)
        return list(hash_to_group.values())

            
        