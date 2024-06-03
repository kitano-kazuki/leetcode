class Solution:
    def calc_result(self, s:str, numRows:int) -> str:
        if numRows == 1:
            return s

        result = []
        interval = numRows - 1
        col = 0
        str_index = 0
        s_len = len(s)

        for i in range (numRows):
           result.append([])

        while True:
            for i in range (numRows):
                if len(result[i]) == col + 1:
                    if i == numRows - 1:
                        break
                    result[i+1][col] = s[str_index]
                else:
                    result[i].append(s[str_index])
                str_index = str_index + 1
                if str_index == s_len:
                    return result

            for i in range(interval):
                letter_row = numRows - 2 - i
                for r in range (numRows - 1, -1, -1):
                    if r == letter_row and r != numRows - 1:
                        result[r].append(s[str_index])
                        str_index = str_index + 1
                        if str_index == s_len:
                            return result
                    else:
                        result[r].append(" ")

            col = col + interval

        return result

    def convert(self,s, numRows):
        result = self.calc_result(s, numRows)
        flattend = [c for row in result for c in row]
        flattend =  [c for c in flattend if c.strip()]
        return "".join(flattend)

solution = Solution()
result = solution.convert("PAYPALISHIRING", 3)
print(result)
