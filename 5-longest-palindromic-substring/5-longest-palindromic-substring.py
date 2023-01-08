class Solution:
        def longestPalindrome(self, s):
            lst = ['|'] * (2 * len(s) + 1)
            lst[1::2] = s

            center = 0
            radius = 0
            longest = s[0]

            while center < len(lst):
                while radius + 1 <= center and radius + 1 + center < len(lst) and lst[center - radius - 1] == lst[center + radius + 1]:
                    radius += 1

                if radius * 2 + 1 > len(longest):
                    longest = lst[center - radius: center + radius + 1]
                center += 1
                radius = 0

            if longest[0] == '|' == longest[-1]:
                longest = ''.join(longest[1::2])
            else:
                longest = ''.join(longest[::2])

            return longest