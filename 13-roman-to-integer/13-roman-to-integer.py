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
        previous = 0
        for letter in s[::-1]:
            number = self.symbol[letter]
            if number >= previous:
                sum += number
            else:
                sum -= number
            previous = number
        return sum
