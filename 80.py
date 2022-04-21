class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.ans = []
        self.dfs(1, k, [])
        return self.ans

    def dfs(self, m, k, path):
        if k == 0:
            self.ans.append(path)
        for i in range(m, self.n + 1):
            if i not in path:
                self.dfs(i + 1, k - 1, path + [i])