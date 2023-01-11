class Solution():
    def searchInsert(self, nums, target):
        for x, val in enumerate(nums):
            if target <= val:
                return x
        return len(nums)

            
