class Solution:
    def myAtoi(self, s: str) -> int:
        init_index = 0
        for i in range(len(s)):
            if s[i] == " ":
                init_index = init_index + 1
            else:
                break
        s = s[init_index:]
        if len(s) == 0:
            return 0
        s_index = 0
        is_negative = False
        if s[0] == "-":
            s_index = s_index + 1
            is_negative = True
        elif s[0] == "+":
            s_index = s_index + 1
        integers = []
        for i in range(s_index, len(s)):
            if ord("0") <= ord(s[i]) and ord(s[i]) <= ord("9"):
                integers.append(ord(s[i]) - ord("0"))
            else:
                break

        int_start = 0
        for i in range(len(integers)):
            if integers[i] == 0:
                int_start = int_start + 1
            if integers[i] != 0:
                break

        integers = integers[int_start:]

        result = 0
        for i in range(len(integers)):
            result = result + integers[i] * (10 **(len(integers[i:]) - 1))

        if is_negative:
            result = -1 * result

        if result < -1 * (1 << 31):
            result = -1 * (1 << 31)
        elif (1 << 31) - 1 < result:
            result = (1 << 31) - 1

        return result






s = "   -042"
solution = Solution()
result = solution.myAtoi(s)
print(result)
