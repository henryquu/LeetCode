class Solution:
    def isValid(self, s: str) -> bool:
        pairs = dict((')(', '][', '}{'))
        stack = []

        for i in s:
            if i in '([{':
                stack.append(i)
            elif len(stack) == 0 or stack.pop() != pairs[i]:
                return False

        return len(stack) == 0