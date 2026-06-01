def longest_subarray(nums,k):
    mp = {}
    s = 0
    n = len(nums)
    maxlen = 0
    for i in range(n):
        s += nums[i]
        if s == k:
            maxlen = max(maxlen,i+1)
        rem = s - k
        if rem in mp:
            maxlen = max(maxlen,i-mp[rem])
        if s not in mp:
            mp[s] = i
    return maxlen
nums = [2,3,5,1,9] 
k = 10
print(longest_subarray(nums,k))
