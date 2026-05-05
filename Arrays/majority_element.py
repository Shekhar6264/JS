def majority_element(nums):
    count = 0
    ele = None
    for num in nums:
        if count == 0:
            ele = num
        if num == ele:
            count += 1
        else:
            count -= 1
    return ele
nums = [2, 2, 1, 1, 1, 2, 2]
result = majority_element(nums)
print("Majority element: ", result)
