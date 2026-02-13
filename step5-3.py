class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        open_brackets = open_to_close.keys()
        processing_idx = 0

        def is_chunk_valid():
            nonlocal processing_idx
            if processing_idx >= len(s):
                return False
            if s[processing_idx] not in open_brackets:
                return False
            expected_end_bracket = open_to_close[s[processing_idx]]
            processing_idx += 1
            while processing_idx < len(s) and s[processing_idx] != expected_end_bracket:
                if not is_chunk_valid():
                    return False
            if processing_idx >= len(s):
                return False
            processing_idx += 1
            return True

        while processing_idx < len(s):
            if not is_chunk_valid():
                return False
        
        return True
                
                