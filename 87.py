class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        temp = []
        ans = []

        def dfs(num, pos):
            if num == 4:
                if pos == len(s):
                    ans.append(".".join(temp))
                return
            if pos == len(s):
                return
            if s[pos] == "0":
                temp.append(s[pos])
                dfs(num + 1, pos + 1)
                temp.pop()
                return

            for i in range(min(3, len(s) - pos)):
                arr = s[pos:pos + i + 1]
                if int(arr) < 256:
                    temp.append(str(arr))
                    dfs(num + 1, pos + i + 1)
                    temp.pop()

        dfs(0, 0)
        return ans

sol = Solution()
print(sol.restoreIpAddresses("1111"))
