from collections import Counter
def topKFrequent(words, k):
    d = Counter(words)
    a = sorted(d.keys(),key = lambda x:(-d[x],x))
    l = []
    for i in range(k):
        l.append(a[i])
    return l
print(topKFrequent(['i','love','leetcode','coding','i','love'],3))
