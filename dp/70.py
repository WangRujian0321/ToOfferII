class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        pre0 = 1
        pre1 = 1
        ans = 1
        for _ in range(n-1):
            ans = pre0 + pre1
            pre0 = pre1
            pre1 = ans
        return ans