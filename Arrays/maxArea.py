def maxArea(a):
    l = 0
    r = len(a)-1
    ans = 0
    while l<r:
        ans = max(ans,min(a[l],a[r])*(r-l))
        if a[l]<a[r]:
            l += 1
        else:
            r -= 1
    return ans
a = [1,8,6,2,5,4,8,3,7]
result = maxArea(a)
print("Maximum area of water that can be contained: ", result)