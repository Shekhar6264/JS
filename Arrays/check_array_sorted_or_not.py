def check(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        if nums[i] > nums[(i+1)%n]:
            count += 1
            if count > 1:
                return False
    return True
print(check(nums=[4,7,9,1,3]))
        