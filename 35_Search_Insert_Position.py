from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        up = len(nums) - 1
        while lo <= up:
            mid = (lo + up) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                up = mid - 1
            else:
                return mid
        return lo

nums = [1,3,5,6]
target = 4
print(Solution().searchInsert(nums=nums, target = target))