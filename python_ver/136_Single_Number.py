from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res

print(Solution().singleNumber(nums=[1,2,1,3,4,2,3]))