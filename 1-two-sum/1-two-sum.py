class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needed = dict()
        for x, val in enumerate(nums):
            if val > target:
                pass
            if val in needed:
                return [needed[val], x]
            needed[target - val] = x

