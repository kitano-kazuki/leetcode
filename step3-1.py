from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_to_count = defaultdict(int)
        for c in s:
            char_to_count[c] += 1
        for i in range(len(s)):
            if char_to_count[s[i]] == 1:
                return i
        return -1