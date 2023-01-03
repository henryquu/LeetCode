class Solution:
    def reverseWords(self, s: str) -> str:
        new = ''
        for word in s.split():
            if new: new += ' '
            new += word[::-1]
        return new