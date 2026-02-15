class Solution:
    def isValid(self, s: str) -> bool:
        unclosed_brackets = []
        parentheses_pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        open_brackets = parentheses_pairs.keys()
        for i in range(len(s)):
            if s[i] in open_brackets:
                unclosed_brackets.append(s[i])
                continue
            if len(unclosed_brackets) == 0:
                return False
            last_unclosed_bracket = unclosed_brackets.pop(-1)
            expected_close_bracket = parentheses_pairs[last_unclosed_bracket]
            if s[i] != expected_close_bracket:
                return False
        if len(unclosed_brackets) > 0:
            return False
        return True