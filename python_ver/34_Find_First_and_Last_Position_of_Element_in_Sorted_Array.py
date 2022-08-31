from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if self.binarySearch(nums, target, 0, len(nums)-1) == -1: return [-1, -1]
        tempL= self.binarySearch(nums, target, 0, len(nums)-1)
        tempR = tempL
        while self.binarySearch(nums, target, 0, tempL-1) != -1:
            tempL -= 1
        while self.binarySearch(nums, target, tempR+1, len(nums)-1) != -1:
            tempR += 1
        return [tempL, tempR]
        
    def binarySearch(self, arr, x, start, end):
        mid = int((start + end) / 2)
        if arr[mid] == x:
            return mid
        if start == end:
            return -1
        if arr[mid] > x:
            return self.binarySearch(arr, x, start, mid -1)
        if arr[mid] < x:
            return self.binarySearch(arr, x, mid + 1, end)

array = [5,7,7,8,8,10]
array2 = [1,3,3,5,5,5,8,9]
t = 5

def binarySearch(arr, x, start, end):
        mid = int((start + end) / 2)
        if arr[mid] == x:
            return mid
        if start == end:
            return -1
        if arr[mid] > x:
            return binarySearch(arr, x, start, mid -1)
        if arr[mid] < x:
            return binarySearch(arr, x, mid + 1, end)

# print(Solution().searchRange(nums=array2,target=9))
# print(binarySearch(array3, 5, 0, len(array3)-1))

class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 1: return [-1, -1]
        firstPos = self.binarySearch(nums, target, 0, len(nums)-1)
        if firstPos == -1: return [-1,-1]
        
        startPos = firstPos
        endPos = firstPos
        while startPos != -1:
            temp1 = startPos
            startPos = self.binarySearch(nums, target, 0, startPos-1)
        startPos = temp1
        while endPos != -1:
            temp2 = endPos
            endPos = self.binarySearch(nums, target, endPos+1, len(nums)-1)
        endPos = temp2
        return [startPos, endPos]
    
    def binarySearch(self, nums, target, left, right):
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            if nums[mid] < target:
                left = mid + 1
        return -1

print(Solution2().searchRange(nums=array2,target=9))