class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_dict_set = set(wordDict)
        # is_segmentable[i] means s[:i] can be segmented
        is_segmentable = [False] * (len(s) + 1)
        is_segmentable[0] = True
        
        for end in range(1, len(s) + 1):
            for start in range(end, -1, -1):
                if not is_segmentable[start]:
                    continue
                substring = s[start:end]
                if substring not in word_dict_set:
                    continue
                is_segmentable[end] = True
                break
        
        return is_segmentable[len(s)]
        