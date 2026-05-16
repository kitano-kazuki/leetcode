class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        parentheses = set()

        def generate_parenthesis_helper(num_open_brackets: int, num_close_brackets: int, parts: list[str]) -> None:
            if num_open_brackets == 0 and num_close_brackets == 0:
                parentheses.add("".join(parts))
                return

            if num_open_brackets > num_close_brackets:
                return
            
            if num_open_brackets > 0:
                parts.append("(")
                generate_parenthesis_helper(num_open_brackets - 1, num_close_brackets, parts)
                parts.pop()

            if num_close_brackets > 0:
                parts.append(")")
                generate_parenthesis_helper(num_open_brackets, num_close_brackets - 1, parts)
                parts.pop()

            return

        generate_parenthesis_helper(n, n, [])
        return list(sorted(parentheses))
            