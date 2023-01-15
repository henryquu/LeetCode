# row1 = s[::numRows + 5]
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lst = []
        i = 0
        while i < len(s): 
            if i + numRows < len(s):
                lst.append(s[i: i + numRows])
                i += numRows
            else:
                lst.append(s[i: len(s)] + '-' * (numRows - (len(s) - i)))
                break

            for j in range(numRows - 2, 0, -1):
                if i >= len(s):
                    break
                tmp = ['-'] * numRows
                tmp[j] = s[i]
                lst.append(''.join(tmp))
                i += 1

        s = ''
        for i in zip(*lst):
            s += ''.join(i)

        return s.replace('-', '')