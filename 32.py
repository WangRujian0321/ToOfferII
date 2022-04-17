class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) and s == t:
            return False
        s = list(s)
        t = list(t)
        s.sort()
        t.sort()
        return "".join(s) == "".join(t)

sol = Solution()
print(sol.isAnagram("a", "a"))

