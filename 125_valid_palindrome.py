import re

class Solution(object):
    def isPalindrome(self, s):
        s = re.sub(r'[^a-zA-Z0-9]','',s)
        s = s.lower()
        left = 0
        right = len(s) - 1
        is_palindrome = True
        while (left < len(s) and right >= 0):
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            else:
                is_palindrome = False
                break

        return is_palindrome
    
s = "A man, a plan, a canal: Panama"
solution = Solution()
print(solution.isPalindrome(s))