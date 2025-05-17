class Solution:
    def minWindow(self, s: str, t: str) -> str:
        chars_in_t = {}
        for c in t:
            chars_in_t[c] = chars_in_t.get(c, 0) + 1
        left = 0
        right = 0
        min_start = -1
        minimum = len(s) + 1
        count = len(t)
        while right < len(s):
            c = s[right]
            if chars_in_t.get(c,0) > 0:
                count -= 1
            chars_in_t[c] = chars_in_t.get(c,0) - 1
            right += 1

            while (count == 0):
                if (right - left < minimum):
                    minimum = right - left
                    min_start = left
                chars_in_t[s[left]] += 1
                if chars_in_t[s[left]] > 0:
                    count += 1
                left += 1
        if minimum != len(s) + 1:
            return s[min_start:min_start + minimum]
        else:
            return ""






s = "ADOBECODEBANC"
t = "ABC"
solution = Solution()
print(solution.minWindow(s, t))

