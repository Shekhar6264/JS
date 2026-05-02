def findMaxAverage(nums, k):
        l = 0
        n = len(nums)
        ans = float('-inf')
        cs = 0
        for r in range(n):
            cs += nums[r]
            if r-l+1 == k:
                ans = max(cs/k,ans)
                cs -= nums[l]
                l += 1
        return ans
nums = [1,12,-5,-6,50,3]
k = 4
result = findMaxAverage(nums, k)
print("Maximum average subarray: ", result)