class Solution:
    def canPartition(self, nums):
        def solve(ind,target):
            if target == 0:
                return True
            if ind == 0:
                return nums[0] == target
            if dp[ind][target] is not None:
                return dp[ind][target]
            nt = solve(ind-1,target)
            take = False
            if(nums[ind]<=target):
                take=solve(ind-1,target-nums[ind])
            dp[ind][target]=take or nt 
            return dp[ind][target]
        n=len(nums)
        ts=0
        s=sum(nums)
        if(s%2!=0):return False
        target=s//2
        dp=[[None]*(target+1) for _ in range(n)]
        return solve(n-1,target)   


        