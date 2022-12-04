class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        l = 0
        r = 0
        new = [0]*((m + n) // 2 + 1)

        for x, _ in enumerate(new):
            if r >= n:
                new[x] = nums1[l]
                l += 1
                pass
            elif l >= m:
                new[x] = nums2[r]
                r += 1
                pass
            elif nums1[l] > nums2[r]:
                new[x] = nums2[r]
                r += 1
            else:
                new[x] = nums1[l]
                l += 1
        median = new[-1]
        if not (n + m) % 2:
            median = (median + new[-2]) / 2
        return median