class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        parentheses = []

        def generate_parenthesis_helper(num_placed_open: int, num_placed_close: int, parts: list[str]) -> None:
            if num_placed_open == n and num_placed_close == n:
                parentheses.append("".join(parts))

            if num_placed_open < num_placed_close:
                return
            
            if num_placed_open < n:
                parts.append("(")
                generate_parenthesis_helper(num_placed_open + 1, num_placed_close, parts)
                parts.pop()

            if num_placed_close < n:
                parts.append(")")
                generate_parenthesis_helper(num_placed_open, num_placed_close + 1, parts)
                parts.pop()

            return

        generate_parenthesis_helper(0, 0, [])
        return parentheses
            