'''Given an integer array nums of unique elements, return all possible  subsets (the power set).'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        

def recursive(nums):
    if len(nums) == 0: 
        return []
    if len(nums) == 1:
        return nums
    
    return recursive(nums[:-1]) + 

