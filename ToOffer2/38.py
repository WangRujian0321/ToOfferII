class Solution:
    def permutation(self, s: str):
        n = len(s)
        res = []
        s_list = []
        for item in s:
            s_list.append(item)
        def track(first=0):
            if first == n:
                res.append("".join(s_list))
            for i in range(first, n):
                s_list[first], s_list[i] = s_list[i], s_list[first]
                track(i + 1)
                s_list[first], s_list[i] = s_list[i], s_list[first]
        track()
        return res


sol = Solution()
print(sol.permutation("abc"))
