def move_zeroes(nums):
    ind = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[ind] = nums[i]
            ind += 1
    for i in range(ind, len(nums)):
        nums[i] = 0
    return nums
nums = [0,1,0,3,12]
result = move_zeroes(nums)
print("Array after moving zeroes: ", result)