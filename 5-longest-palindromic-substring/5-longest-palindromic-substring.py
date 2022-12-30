class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = s[0]
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if j - i + 1 > len(m) and s[i] == s[j]:
                    if s[i:j + 1] == s[i:j + 1][::-1]:
                        m = s[i:j + 1]

        return m