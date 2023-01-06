class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            dic = {}

            for ind, x in enumerate(numbers):
                if target - x in dic:
                    return [dic[target - x] + 1, ind + 1]
                dic[x] = ind