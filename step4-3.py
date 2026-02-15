class Solution:
    def isValid(self, s: str) -> bool:
        processing_idx = 0
        open_to_close = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        open_brackets = open_to_close.keys()

        def parentheses():
            nonlocal processing_idx
            if s[processing_idx] not in open_brackets:
                return False
            expected_close_bracket = open_to_close[s[processing_idx]]
            processing_idx += 1
            while processing_idx < len(s) and s[processing_idx] != expected_close_bracket:
                is_valid = parentheses()
                if not is_valid:
                    return False
            if processing_idx < len(s):
                processing_idx += 1
                return True
            return False
        
        while processing_idx < len(s):
            is_valid = parentheses()
            if not is_valid:
                return False
        return True