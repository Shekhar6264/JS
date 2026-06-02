from collections import Counter
def topKFrequent(nums, k):
    d = Counter(nums)
    a = sorted(d.keys(),key = lambda x:(-d[x],x))
    l = []
    for i in range(k):
        l.append(a[i])
    return l
print(topKFrequent([1,4,2,3,5,1,2,3],3))
