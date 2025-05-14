class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        letter_dict = {}
        longest = 1
        left = 0
        letter_dict[s[left]] = left
        right = 1
        while right < len(s):
            if s[right] in letter_dict.keys() and s[right] != -1:
                left = letter_dict[s[right]] + 1
                for k, v in letter_dict.items():
                    if v < left:
                        letter_dict[k] = -1
            length = right - left + 1
            longest = max(longest, length)
            letter_dict[s[right]] = right
            right = right + 1
        return longest

s = "tmmzuxt"
solution = Solution()
print(solution.lengthOfLongestSubstring(s))

