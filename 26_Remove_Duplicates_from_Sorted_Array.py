class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i, j = 0, 1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1


nums = [1,2,2,2,3]

print(Solution().removeDuplicates(nums = nums))
