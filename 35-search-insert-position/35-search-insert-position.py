class Solution():
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            middle = (l + r) // 2

            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                if l == r:
                    return middle
                r = middle
            else:
                if l == r:
                    return middle + 1
                l = middle + 1
            
