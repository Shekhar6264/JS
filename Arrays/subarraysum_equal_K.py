def subarraysum(nums,k):
    count = 0
    d = {0:1}
    s = 0
    for num in nums:
        s += num
        rem = s-k
        if rem in d:
            count += d[rem]
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    return count
nums = [1, 1, 1, 2, 3]
k = 3
result = subarraysum(nums, k)
print("Number of subarrays that sum to k: ", result)