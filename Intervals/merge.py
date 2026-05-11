def merge(intervals):
    intervals.sort(key= lambda x:x[0])
    res = []
    for i in intervals:
        if not res or res[-1][1] < i[0]:
            res.append([i[0],i[1]])
        else:
            res[-1][1] = max(res[-1][1],i[1])
    return res
intervals = [[1,3],[2,5],[6,8],[15,19]] 
print("Intervals are: ",merge(intervals))