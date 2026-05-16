class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        all_parentheses = []

        def generate_parenthesis_patterns(num_open: int, num_close: int, parts: list[str]) -> None:
            if num_open == n and num_close == n:
                all_parentheses.append("".join(parts))
                return
            
            if num_open < num_close:
                return

            if num_open < n:
                parts.append("(")
                generate_parenthesis_patterns(num_open + 1, num_close, parts)
                parts.pop()
            
            if num_close < n:
                parts.append(")")
                generate_parenthesis_patterns(num_open, num_close + 1, parts)
                parts.pop()
            
            return
        
        generate_parenthesis_patterns(0, 0, [])
        return all_parentheses
