def maxproduct(nums):
    pro = 1
    max_pro = float('-inf')
    for num in nums:
        pro *= num
        max_pro = max(max_pro, pro)
        if pro == 0:
            pro = 1
    pro = 1
    for num in reversed(nums):
        pro *= num
        max_pro = max(max_pro, pro)
        if pro == 0:
            pro = 1
    return max_pro
nums = [2, 3, -2, 4]
result = maxproduct(nums)
print("Maximum product of a subarray: ", result)