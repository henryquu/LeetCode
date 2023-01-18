class Solution:
    def fizzBuzz(self, n):
        lst = ['']*n
        for y in range(1, n + 1):
            if y % 15 == 0:
                lst[y - 1] = 'FizzBuzz'
            elif y % 3 == 0:
                lst[y - 1] = 'Fizz'
            elif y % 5 == 0:
                lst[y - 1] = 'Buzz'
            else:
                lst[y - 1] = str(y)
        return lst
        