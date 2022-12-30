class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        m = s[0]
        for i in range(n):
            for j in range(i + 1, n):
                if j - i + 1 > len(m) and s[i] == s[j]:
                    sub = s[i:j + 1]
                    if sub == sub[::-1]:
                        m = sub

        return m