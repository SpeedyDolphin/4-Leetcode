def twoSum(nums: list[int], target: int) -> list[int]:
        nums.sort()
        for i in range(len(nums)):
            secondIndex = binarySearch(nums, target-nums[i])
            if secondIndex != -1:
                return [i, secondIndex]


def binarySearch(nums: list[int], target: int, start, end) ->int:
    start = 0
    end = len(nums)
    while True:
        if end-start < 1: 
            return -1
        mid = int((end-start)/2) + start
        if (nums[mid] == target):
            return mid
        if nums[mid] < target: 
            start = mid+1
        if nums[mid] > target: 
            end = mid-1

print(binarySearch([2,7,11,15], 16, 0, 3))

from collections import defaultdict
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        
        lookup = defaultdict(int)
        for num in nums: 
            lookup[num] += 1

        for i in range(len(nums)):
            if nums[i]-target in lookup.keys():
                if num[i] == num[i]-target and lookup[num[i]-target] < 2: 
                        continue
                return [i, nums.index(num[i], i+1)]

