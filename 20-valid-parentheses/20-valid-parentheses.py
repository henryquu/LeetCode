class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        
        lst = []

        for i in s:
            if lst and (chr(ord(lst[-1]) + 1) == i or chr(ord(lst[-1]) + 2) == i):
                lst.pop()
            else:
                lst.append(i)

        return lst == []