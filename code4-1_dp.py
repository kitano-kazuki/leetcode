class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        is_segmentable = [True] + [False] * len(s)  # s[:i] is segmentable or not

        for start in range(len(s)):
            if not is_segmentable[start]:
                continue
            for word in wordDict:
                if s.startswith(word, start):
                    is_segmentable[start + len(word)] = True
        
        return is_segmentable[len(s)]
