def f_and_l_occurence(nums,target):
    low = 0
    high = len(nums) - 1
    res = -1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            res = mid
            high = mid -1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    lo = 0
    hi = len(nums) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            result = mid
            lo = mid + 1
        elif nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return [res,result]
nums = [1,2,3,4,5,6,7,7,8,9]
target = 7
print("First and Last Occurences are: ",f_and_l_occurence(nums,target))