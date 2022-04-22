class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        if len(matrix[0]) == 0:
            return []
        ans = []
        m = matrix
        while len(m) > 1 and len(m[0]) > 1:
            for item in m[0]:
                ans.append(item)
            for j in range(1, len(m)):
                ans.append(m[j][-1])
            for j in range(len(m[0])-2, -1, -1):
                ans.append(m[-1][j])
            for j in range(len(m)-2, 0, -1):
                ans.append(m[j][0])
            m = [m[i][1:len(m[i])-1] for i in range(1, len(m)-1)]
        if len(m) == 0:
            return ans
        elif len(m[0]) == 0:
            return ans
        elif len(m) == 1:
            for item in m[0]:
                ans.append(item)
        elif len(m[0]) == 1:
            for i in range(len(m)):
                ans.append(m[i][0])
        return ans
sol = Solution()
print(sol.spiralOrder([[1,2], [3,4]]))
