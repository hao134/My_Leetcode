from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        indexTofind = len(nums) - k
        self.quickSort(nums, 0, len(nums)-1)
        return nums[indexTofind]

    def quickSort(self, nums, left, right):
        if left < right:
            partitionIdx = self.partition(nums, left, right)
            self.quickSort(nums, left, partitionIdx-1)
            self.quickSort(nums, partitionIdx+1, right)
    
    def partition(self, nums, left, right):
        pivotElement = nums[right]
        partitionIdx = left
        for j in range(left, right):
            if nums[j] < pivotElement:
                self.swap(nums, partitionIdx, j)
                partitionIdx += 1

        self.swap(nums, partitionIdx, right)
        return partitionIdx

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp


## Better Solution


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        indexTofind = len(nums) - k
        self.quickSelect(nums, 0, len(nums)-1, indexTofind)
        return nums[indexTofind]

    def quickSelect(self, nums, left, right, indexTofind):
        if left < right:
            partitionIdx = self.partition(nums, left, right)
            if indexTofind == partitionIdx:
                return nums[indexTofind]
            elif indexTofind < partitionIdx:
                return self.quickSelect(nums, left, partitionIdx-1, indexTofind)
            else:
                return self.quickSelect(nums, partitionIdx+1, right, indexTofind)
    
    def partition(self, nums, left, right):
        pivotElement = nums[right]
        partitionIdx = left
        for j in range(left, right):
            if nums[j] < pivotElement:
                self.swap(nums, partitionIdx, j)
                partitionIdx += 1

        self.swap(nums, partitionIdx, right)
        return partitionIdx

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

nums = [3,2,1,5,6,4]
k = 2
print(Solution2().findKthLargest(nums=nums, k=k))