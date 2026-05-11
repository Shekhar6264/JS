def insert_interval(intervals,newInterval):
    intervals.append(newInterval)
    intervals.sort(key= lambda x:x[0])
    res = []
    for i in intervals:
        if not res or res[-1][1] < i[0]:
            res.append([i[0],i[1]])
        else:
            res[-1][1] = max(res[-1][1],i[1])
    return res
intervals = [[1,3],[6,7],[8,10]]
newInterval = [2,5]
print("Intervals are: ",insert_interval(intervals,newInterval))