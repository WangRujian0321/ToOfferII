class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        for L in range(2, n+1):
            for i in range(n-L+1):
                j = i + L - 1
                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i > 1:
                        dp[i][j] = dp[i+1][j-1]
                    else:
                        dp[i][j] = True
        ans = 0
        for i in range(n):
            for j in range(i, n):
                if dp[i][j]:
                    ans += 1
        print(dp)
        return ans


sol = Solution()
print(sol.countSubstrings("aaa"))