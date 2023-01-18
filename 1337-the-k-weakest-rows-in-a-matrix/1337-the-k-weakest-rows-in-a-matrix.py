class Solution:
    def kWeakestRows(self, mat, k):
        lst = [(x, sum(row)) for x, row in enumerate(mat)] 
        lst.sort(key = lambda x: (x[1], x[0]))
        return [x[0] for x in lst[:k]]