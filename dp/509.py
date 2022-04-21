class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        pre0, pre1 = 0, 1
        ans = 0
        for _ in range(1, n):
            ans = pre0 + pre1
            pre0 = pre1
            pre1 = ans
        return ans