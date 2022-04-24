class Solution:
    def translateNum(self, num: int) -> int:
        num_str = str(num)
        n = len(num_str)
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n+1):
            if num_str[i-2] != '0' and int(num_str[i-2:i]) < 26:
                dp[i] += dp[i-2]
            dp[i] += dp[i-1]
        return dp[-1]  