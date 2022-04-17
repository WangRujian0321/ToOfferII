class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n):
            while stack and stack[-1][1] < temperatures[i]:
                node = stack.pop()
                ans[node[0]] = i - node[0]
            stack.append((i, temperatures[i]))
        return ans
