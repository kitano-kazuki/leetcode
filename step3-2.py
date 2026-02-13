class Solution:
    def isValid(self, s: str) -> bool:
        unclosed_open_brackets = []
        bracket_pairs = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        open_brakets = bracket_pairs.keys()
        for i in range(len(s)):
            if s[i] in open_brakets:
                unclosed_open_brackets.append(s[i])
                continue
            if len(unclosed_open_brackets) == 0:
                return False
            last_open_bracket = unclosed_open_brackets.pop(-1)
            expected_close_bracket = bracket_pairs[last_open_bracket]
            if s[i] != expected_close_bracket:
                return False
        if len(unclosed_open_brackets) > 0:
            return False
        return True
