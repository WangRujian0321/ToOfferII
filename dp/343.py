class Solution:
    def integerBreak(self, n: int) -> int:
        # dp = [1] * (n+1)
        # for i in range(2, n + 1):
        #     for j in range(i):
        #         dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        # return dp[n]
        if n <4:
            return n-1
        dp = [1] * (n+1)
        dp[0],dp[1],dp[2],dp[3] = 0,0,2,3
        for i in range(4, n + 1):
            dp[i] = max(dp[i-2]*2, dp[i-3]*3)
        print(dp)
        return dp[-1]