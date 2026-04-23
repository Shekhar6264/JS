def minSubArrayLen(target, nums):
        l = 0
        Sum = 0
        n = len(nums)
        ans = float('inf')
        for r in range(n):
            Sum += nums[r]
            while Sum >= target:
                ans = min(ans,r-l+1)
                Sum -= nums[l]
                l += 1
        if ans == float('inf'):
            return 0
        return ans
target = 7
nums = [2,3,1,2,4,3]
result = minSubArrayLen(target, nums)
print("Minimum subarray length: ", result)