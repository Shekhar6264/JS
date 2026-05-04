def remove_duplicates(nums):
    ind = 0
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            ind += 1
            nums[ind] = nums[i]
    return ind+1
nums = [0,0,1,1,1,2,2,3,3,4]
result = remove_duplicates(nums)
print("Length of array after removing duplicates: ", result)