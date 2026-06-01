def threesum(arr):
    if len(arr) <= 1:
        return arr
    arr.sort()
    res = []
    n = len(arr)
    for i in range(n):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        target = -arr[i]
        l = i+1
        r = n-1
        while l<r:
            s = arr[l] + arr[r]
            if s == target:
                res.append((arr[i],arr[l],arr[r]))
                l += 1
                r -= 1
                while l<r and arr[l] == arr[l-1]:
                    l += 1
                while l<r and arr[r] == arr[r+1]:
                    r -= 1
            elif s < target:
                l += 1
            else:
                r -= 1
    return res
arr =[1,0,-1,1,2,-1,-1]
print(threesum(arr))