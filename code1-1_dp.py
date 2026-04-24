class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_dict_set = set(wordDict)
        # edges[i] means s[:i] can be segmented
        edges = [False] * (len(s) + 1)
        edges[0] = True
        
        for end in range(1, len(s) + 1):
            for start in range(end):
                if not edges[start]:
                    continue
                substring = s[start:end]
                if substring not in word_dict_set:
                    continue
                edges[end] = True
                break
        
        return edges[len(s)]