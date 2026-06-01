def rearrangeArray(nums):
    pos = []
    neg = []
    res = []
    for i in nums:
        if i > 0:
            pos.append(i)
        else:
            neg.append(i)
    for j in range(len(pos)):
        res.append(pos[j])
        res.append(neg[j])
    return res
print(rearrangeArray(nums=[1,4,-5,-56,78,-38]))