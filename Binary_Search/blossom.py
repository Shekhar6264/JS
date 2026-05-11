def minDays(bloomDay,m,k):
    def valid(arr,day,m,k):
        count = 0
        b = 0
        for i in range(len(arr)):
            if arr[i]<=day:
                count += 1
            else:
                b += count //k
                count =0
        b += count // k
        return b >= m
    if (m * k) > len(bloomDay):
        return -1
    low = min(bloomDay)
    high = max(bloomDay)
    res = high
    while low <= high:
        mid = (low + high) // 2
        if valid(bloomDay,mid,m,k):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res
bloomDay = [7,7,7,7,12,7,7]
m = 2
k = 3
print("Number of Days is:",minDays(bloomDay,m,k))