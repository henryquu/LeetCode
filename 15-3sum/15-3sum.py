class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()
        pos, neg, zer = [], [], []

        for val in nums:
            if val < 0:
                neg.append(val)
            elif val == 0:
                zer.append(val)
            else:
                pos.append(val)

        pos_set = set(pos)
        neg_set = set(neg)

        if len(zer) >= 3:
            result.add((0, 0, 0))

        if zer:
            for val in pos_set:
                if -val in neg_set:
                    result.add((0, val, -val))

        for ind, val in enumerate(pos):
            for val2 in pos[ind + 1:]:
                if (-val - val2) in neg_set:
                    result.add(tuple(sorted((val, val2, -val - val2))))

        for ind, val in enumerate(neg):
            for val2 in neg[ind + 1:]:
                if (-val - val2 )in pos_set:
                    result.add(tuple(sorted((val, val2, -val - val2))))
    
        return result