class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        temp = 0
        for i in range(m):
            temp += grid[i][0]
            grid[i][0] = temp
        temp = 0
        for i in range(n):
            temp += grid[0][i]
            grid[0][i] = temp
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = max(grid[i-1][j], grid[i][j-1]) + grid[i][j]
        return grid[-1][-1]