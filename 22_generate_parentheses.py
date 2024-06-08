from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        table = []
        for i in range(n):
            table.append(set())
        for i in range(n):
            patterns = set()
            if i == 0:
                patterns.add("()")
            elif i == 1:
                patterns.add("(())")
                patterns.add("()()")
            else:
                for element in table[i-1]:
                    patterns.add("(" + element +")")
                    patterns.add("()" + element)
                    patterns.add(element + "()")
                for k in range(1, i + 2):
                    for l in range(1, i + 2):
                        if k * l == i + 1:
                            patterns.add(("(" * k + ")" * k  )* l)
            table[i].update(patterns)

        return sorted(list(table[n-1]))




n = 3
solution = Solution()
result = solution.generateParenthesis(n)
print(result)

