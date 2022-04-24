class Solution:
    def findNthDigit(self, n: int) -> int:
        i = 0
        m = 1
        while n > m + (10 **(i+1)-10 ** i) * (i+1):
            m += (10 **(i+1)-10 ** i) * (i+1)
            i += 1
        n -= m
        num = n // (i+1)
        return int(str(num+10**i)[n%(i+1)])