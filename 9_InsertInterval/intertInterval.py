#Making a new array is more time efficient. This way is more memory efficient. 
def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    if newInterval[1] <= intervals[0][0]:
        intervals.insert(0, newInterval)
        print(intervals)
        mergeForward(intervals)
        return intervals
    
    for i in range(len(intervals)):
        #newInterval start <= interval[i] end
        # this means that the new interval starts in the middle of an existing interval
        if newInterval[0] <= intervals[i][1]:
            intervals[i][1] = max(intervals[i][1], newInterval[1])
            mergeForward(intervals, i)
            return intervals
            
        #newInterval start < intervals[i] start
        #this means that the new interval starts between two existing intervals
        elif newInterval[0] < intervals[i][0]:  
            intervals.insert(i, newInterval)
            mergeForward(intervals, i)
            return intervals

    #At the end with no overlap 
    intervals.append(newInterval)
    return intervals 

def mergeForward(intervals, i):
    # merge while newInterval end >= next interval start 
    while i+1 < len(intervals) and intervals[i][1] >= intervals[i+1][0]:
        intervals[i][1] = max(intervals[i+1][1], intervals[i][1])
        intervals.pop(i+1)
        
if __name__ == "__main__":
    print(insert([[1,5]], [0,3]))