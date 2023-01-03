class Solution:
        def longestPalindrome(self, s):
            longest_palindrome = s[0]
            table = [[0] * len(s) for _ in range(len(s))]

            for i in range(len(s)):
                table[i][i] = True

            for i in range(len(s) - 1)[::-1]:
                for j in range(i + 1, len(s)):
                    if s[i] == s[j] and (j - i == 1 or table[i + 1][j - 1]): 
                        table[i][j] = True
                        if len(longest_palindrome) < j - i + 1:
                            longest_palindrome = s[i: j + 1]

            return longest_palindrome