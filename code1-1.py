class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        right = 1
        longest_length = 1
        chars_in_window = set(s[0])

        # s[left:right]は被りなし
        while right < len(s):

            # right+=1するために左端を縮める
            while s[right] in chars_in_window:
                chars_in_window.remove(s[left])
                left += 1

            chars_in_window.add(s[right]) 
            right += 1
            longest_length = max(longest_length, right - left)

        return longest_length
