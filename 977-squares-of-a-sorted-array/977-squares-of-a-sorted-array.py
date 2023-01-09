class Solution:
    def sortedSquares(self, nums):
        dequed = collections.deque(nums)
        lst = collections.deque()


        while dequed:
            right_sqr = dequed[-1]**2
            left_sqr = dequed[0]**2
            if left_sqr > right_sqr:
                lst.appendleft(left_sqr)
                dequed.popleft()
            else:
                lst.appendleft(right_sqr)
                dequed.pop()

        return list(lst)