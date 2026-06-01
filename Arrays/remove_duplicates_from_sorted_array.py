def duplicates(nums):
    ind = 0
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            ind += 1
        nums[ind] = nums[i]
    return ind+1
print(duplicates(nums=[1,2,2,2,3,3,4,5,5,5,5]))
