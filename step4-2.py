class Solution:
    def firstUniqChar(self, s: str) -> int:
        duplicates = set()
        unique_char_to_idx = {}
        for i in range(len(s)):
            if s[i] in duplicates:
                continue
            if s[i] in unique_char_to_idx:
                del unique_char_to_idx[s[i]]
                duplicates.add(s[i])
                continue
            unique_char_to_idx[s[i]] = i

        if unique_char_to_idx:
            return next(iter(unique_char_to_idx.values()))
        return -1