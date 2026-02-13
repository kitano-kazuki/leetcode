BRACKET_PAIRS = {
    "(" : ")",
    "{" : "}",
    "[" : "]"
}
class Solution:
    def _isValid(self, s, idx, stack):
        if idx == len(s):
            if len(stack) == 0:
                return True
            return False
        if s[idx] in BRACKET_PAIRS.keys():
            stack.append(s[idx])
            return self._isValid(s, idx + 1, stack)
        if len(stack) == 0:
            return False
        last_unclosed_bracket = stack.pop(-1)
        if BRACKET_PAIRS[last_unclosed_bracket] != s[idx]:
            return False
        return self._isValid(s, idx + 1, stack)

    def isValid(self, s: str) -> bool:
        return self._isValid(s, 0, [])