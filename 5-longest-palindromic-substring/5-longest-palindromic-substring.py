class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                sub = s[i: j]
                if len(sub) > len(m) and sub == sub[::-1]:
                    m = sub
        return m