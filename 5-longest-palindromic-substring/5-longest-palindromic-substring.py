class Solution:
        def longestPalindrome(self, s):
            modified = '|' + '|'.join(s) + '|'

            center = 0
            radius = 0
            longest = s[0]

            n = len(modified)
            for center in range(1, n - 1):
                while radius + 1 <= center and radius + 1 + center < n and modified[center - radius - 1] == modified[center + radius + 1]:
                    radius += 1

                if radius * 2 + 1 > len(longest):
                    longest = modified[center - radius: center + radius + 1]
                center += 1
                radius = 0

            longest = ''.join([a for a in longest if a != '|'])

            return longest