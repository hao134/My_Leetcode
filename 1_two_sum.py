from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i != j and num + num2 == target:
                    return [i, j]

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_temp = {}
        for index, num in enumerate(nums):
            if target - num in dict_temp:
                return [dict_temp[target-num],index]
            dict_temp[num] = index

#print(Solution2().twoSum(nums=[3,2,4], target=6))