def solve(nums, ds, res, freq):
    if len(ds) == len(nums):
        res.append(ds.copy())
        return
    for i in range(len(nums)):
        if not freq[i]:
            freq[i] = True
            ds.append(nums[i])
            solve(nums, ds, res, freq)
            ds.pop()
            freq[i] = False
def permute(nums):
    res = []
    ds = []
    freq = [False] * len(nums)
    solve(nums, ds, res, freq)
    return res
nums = [1,2,3]
print(permute(nums))
