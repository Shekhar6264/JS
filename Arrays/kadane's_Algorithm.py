def maxsubarray(arr):
    Sum = 0
    ans = float('-inf')
    for i in arr:
        Sum += i
        ans = max(ans, Sum)
        if Sum < 0:
            Sum = 0
    return ans
arr = [-2,1,-3,4,-1,2,1,-5,4]
result = maxsubarray(arr)
print("Maximum subarray sum: ", result)