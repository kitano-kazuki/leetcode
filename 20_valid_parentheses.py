class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_parentheses = ["(", "[", "{"]
        close_parentheses = [")", "]", "}"]
        for c in s:
            if c in open_parentheses:
                stack.append(c)
            if c in close_parentheses:
                c_i = close_parentheses.index(c)
                open_p = open_parentheses[c_i]
                if len(stack) > 0:
                    open_p_candidate = stack.pop()
                    if open_p != open_p_candidate:
                        return False
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False

s = "()[]{}"
solution = Solution()
result = solution.isValid(s)
print(result)
