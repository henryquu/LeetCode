class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:  return False
        a = str(x)
        return a == a[::-1]

           