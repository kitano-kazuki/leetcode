class Solution:
    def isValid(self, s: str) -> bool:
        unclosed_brackets = []
        brackets_pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        for i in range(len(s)):
            if s[i] in brackets_pairs.keys():
                unclosed_brackets.append(s[i])
            else:
                if len(unclosed_brackets) == 0:
                    return False
                last_unclosed_bracket = unclosed_brackets.pop(-1)
                if brackets_pairs[last_unclosed_bracket] != s[i]:
                    return False
        if len(unclosed_brackets) == 0:
            return True
        return False