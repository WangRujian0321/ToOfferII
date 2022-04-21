class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * n for _ in range(m)]
        if 1 in obstacleGrid[0]:
            pos = obstacleGrid[0].index(1)
            for i in range(pos, n):
                dp[0][i] = 0
        for i in range(m):
            if obstacleGrid[i][0] != 1:
                continue
            else:
                for j in range(i, m):
                    dp[j][0] = 0
                break
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]
