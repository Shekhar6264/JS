from collections import Counter
def numberOfPairs(nums):
    d = Counter(nums)
    count = 0
    left = 0
    for i in d.values():    
        count += (i//2)
        if i % 2 == 1:
            left+=1
    return [count,left]
print(numberOfPairs([1,2,3,1,2,3,2]))