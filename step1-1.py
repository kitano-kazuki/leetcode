class Solution:
    def isValid(self, s: str) -> bool:
        parentheses1 = 0
        parentheses2 = 0
        parentheses3 = 0
        for i in range(len(s)):
            if parentheses1 < 0 or parentheses2 < 0 or parentheses3 < 0:
                return False
            if s[i] == "(":
                parentheses1 += 1
            elif s[i] == "{":
                parentheses2 += 1
            elif s[i] == "[":
                parentheses3 += 1
            elif s[i] == ")":
                parentheses1 -= 1
            elif s[i] == "}":
                parentheses2 -= 1
            elif s[i] == "]":
                parentheses3 -= 1
        if parentheses1 == 0 and parentheses2 == 0 and parentheses3 == 0:
            return True
        return False
            