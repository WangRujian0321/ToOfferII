class Solution:
    def combinationSum(self, candidates, target: int):
        if target == 0:
            return [[]]
        ans_item = []
        for item in candidates:
            if item <= target:
                ans_item = [[item] + item0 for item0 in self.combinationSum(candidates, target - item)]
        return ans_item


sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))
