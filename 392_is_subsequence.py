class Solution:
    def isSubsequence(self, s: str, t : str) -> bool:
        if s == "":
            return True
        s_i = 0
        for i in range(len(t)):
            c = t[i]
            if c == s[s_i]:
                s_i = s_i + 1
            if s_i == len(s):
                return True

        return False



s = "abc"
t = "ahbgdc"
solution = Solution()
result = solution.isSubsequence(s,t)
print(result)
