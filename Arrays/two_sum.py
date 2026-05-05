def two_sum(nums,target):
    d = {}
    for i,num  in enumerate(nums):
        comp = target - num
        if comp in d:
            return [d[comp],i]
        d[num] = i
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print("Indices of the two numbers that add up to target: ", result)