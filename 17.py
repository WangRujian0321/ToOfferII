class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tn, sn = len(t), len(s)
        if tn > sn or(tn == sn and s != t):
            return ""
        for i in range(sn - tn):
            if s[i:i+tn] == t:
                return s[i:tn]
        return ""


sol = Solution()
print(sol.minWindow("ADOBECODEBANC", "ABC"))
