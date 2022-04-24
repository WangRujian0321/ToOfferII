class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        i, j, k = 0, 0, 0
        while len(dp) < n:
            u_i = dp[i] * 2
            u_j = dp[j] * 3
            u_k = dp[k] * 5
            u = min(u_i, u_j, u_k)
            dp.append(u)
            if u == u_i:
                i += 1
            if u == u_j:
                j += 1
            if u == u_k:
                k += 1
        return dp[-1]


sol = Solution()
print(sol.nthUglyNumber(10))


