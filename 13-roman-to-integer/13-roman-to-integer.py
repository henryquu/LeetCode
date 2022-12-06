class Solution(object):
    symbol = {
    'I': 1, 
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000}

    def romanToInt(self, s):
            sum = 0
            s = 'I' + s[::-1]
            for ind, letter in enumerate(s[1:], 1):
                number = self.symbol[letter]
                if number >= self.symbol[s[ind - 1]]:
                    sum += number
                else:
                    sum -= number
            return sum