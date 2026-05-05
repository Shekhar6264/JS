def subarraysum(nums,k):
    count = 0
    d = {0:1}
    ps = 0
    for i in nums:
        ps += i
        if ps-k in d:
            count += d[ps-k]
        d[ps] = d.get(ps,0)+1
    return count
nums = [1, 1, 1, 2, 3]
k = 3
result = subarraysum(nums, k)
print("Number of subarrays that sum to k: ", result)