class Solution:
    def coinChange(self, coins, amount):
        n = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(n)]
        def solve(ind, amount):
            if ind == n:
                if amount == 0:
                    return 0
                else:
                    return float('inf')
            if dp[ind][amount] != -1:
                return dp[ind][amount]
            skip = solve(ind + 1, amount)
            take = float('inf')
            if amount >= coins[ind]:
                take = solve(ind, amount - coins[ind])
                if take != float('inf'):
                    take += 1
            dp[ind][amount] = min(skip,take)
            return dp[ind][amount]
        ans = solve(0, amount)
        return ans if ans != float('inf') else -1

        