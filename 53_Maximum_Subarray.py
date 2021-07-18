from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0: return 0
        curr = res = nums[0]
        for i in range(1, l):
            curr += nums[i]
            if curr == 0 or nums[i] > curr:
                curr = nums[i]
            if res < curr:
                res = curr

        return res

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(Solution().maxSubArray(nums= nums))