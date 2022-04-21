class Solution:
    def combinationSum2(self, candidates, target: int):
        candidates_sort = sorted(candidates)
        ans = []
        def backtracking(nums, total, target, path):
            if total == target:
                ans.append(path.copy())
                return
            if total > target:
                return
            p = [-1] + nums
            for i in range(1, len(p)):
                if p[i] == p[i-1]:
                    continue
                total += p[i]
                path.append(p[i])
                backtracking(nums[i:], total, target, path)
                path.pop()
                total -= p[i]
        backtracking(candidates_sort, 0, target, [])
        return ans

sol = Solution()
print(sol.combinationSum2([10, 1, 2, 7,6,1,5], 8))
