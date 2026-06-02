def longestConsecutive(nums):
    if not nums:
        return 0
    a = set(nums)
    start = 0
    max_count = 0
    for num in a:
        if num-1 not in a:
            start = num
            count = 1
            while start+1 in a:
                count += 1
                start += 1
            max_count = max(max_count,count)
    return max_count
print(longestConsecutive(nums=[1,200,100,3,2,4]))
    