#ATTEMPTED NOT FINISHED
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    rlist = []
    nums = sorted(nums)

    for i in range(len(nums)):
        if i > 0 and nums[i-1] == nums[i]:
            continue
        print(i)
        target = nums[i]
        start = i+1
        end = len(nums) -1
        while start < end: 
            value = nums[start] + nums[end] + target
            if value == 0:
                rlist.append([target, nums[start], nums[end]])
                break
            elif value < 0: 
                start +=1
                while nums[start-1] == nums[start] and start<end:
                    start+=1
            else:
                end -=1
                while nums[end+1] ==  nums[end] and start<end:
                    end -=1
    return rlist 
    
print(threeSum([0,0,0,0]))