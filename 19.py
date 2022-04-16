class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(s):
            n = len(s)
            i, j = 0, n-1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        n= len(s)
        x, y = 0, n - 1
        while x < y:
            if s[x] != s[y]:
                return check(s[x: y]) or check(s[x+1: y+1])
            x += 1
            y -= 1
        return True