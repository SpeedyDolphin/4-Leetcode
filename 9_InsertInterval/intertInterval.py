#Making a new array is more time efficient. This way is more memory efficient. 
def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    for i in range(len(intervals)):
        #New segment is completely contained by an existing segment
        if intervals[i][0] <= newInterval[0] and newInterval[1] <= intervals[i][1]:
            print('contained')
            return intervals
         
        if intervals[i][0] > newInterval[0]:
            #Start overlap
            if i > 0 and intervals[i][1] > newInterval[1]:
                #sets the start position
                intervals[i-1] = [intervals[i-1][0], newInterval[1]]

            #No start overlap insert
            else:                
                intervals.insert(i, newInterval)

            #potentially merges because the end is larger than the next start
            while newInterval[1] >= intervals[i][0]:
                intervals[i-1][1] = intervals[i][1]
                intervals.pop(i)
        
            return intervals

    #At the end with no overlap 
    intervals.append(newInterval)
    return intervals 

if __name__ == "__main__":
    print(insert([[1,5]], [2,7]))