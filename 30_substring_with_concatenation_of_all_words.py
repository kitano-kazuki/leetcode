from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        default = {}
        n = len(words[0])
        for word in words:
            default[word] = default.get(word,0) + 1

        result = []
        for i in range(len(s) - n * len(words) + 1):
            # print(f"i = {i}")
            left = i
            count = 0
            seen = {}
            for j in range(i, len(s) - n + 1, n):
                # print(seen)
                word_candidate = s[j: j + n]
                if word_candidate in words:
                    seen[word_candidate] = seen.get(word_candidate, 0) + 1
                    if seen[word_candidate] <= default[word_candidate]:
                        count += 1
                    else:
                        while seen[word_candidate] > default[word_candidate]:
                            substr = s[left: left + n]
                            seen[substr] -= 1
                            if seen[substr] <= default[substr]:
                                count -= 1
                            left += n
                    if count == len(words):
                        result.append(left)
                        substr = s[left: left + n]
                        seen[substr] -= 1
                        count -= 1
                        left += n
                else:
                    left = j + n
                    count = 0
                    seen = {}
        return list(set(result))


s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]

solution = Solution()
print(solution.findSubstring(s, words))

