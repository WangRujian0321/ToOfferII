class Solution:
    def partition(self, s: str):
        n = len(s)
        f = [[True] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = (s[i] == s[j]) and f[i + 1][j - 1]

        ans = []
        temp = []
        def dfs(start):
            if start == n:
                ans.append(temp.copy())
                return
            for j in range(start, n):
                if f[start][j]:
                    temp.append(s[start:j+1])
                    dfs(j+1)
                    temp.pop()
        dfs(0)
        return ans


sol = Solution()
print(sol.partition("google"))

