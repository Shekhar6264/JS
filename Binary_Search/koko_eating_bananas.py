import math
def minspeed(arr,h):
    def hours(piles,h):
        total = 0
        for i in piles:
            total += math.ceil(i/h)
        return total
    low = 1
    high = max(arr)
    res = 0
    while low <= high:
        mid = (low + high) // 2
        if hours(arr,mid) <= h:
            res = mid
            high = mid -1
        else:
            low =mid + 1
    return res

arr = [30,11,23,4,20]
h = 6
print("Minimum Eating Speed is: ",minspeed(arr,h))