def two_sum(nums,target):
    mp = {}
    for i,num in enumerate(nums):
        comp = target - num
        if comp in mp:
            return [mp[comp],i]
        else:
            mp[num] = i
    return [-1,-1]
print(two_sum(nums=[2,5,8,9,4],target=11))