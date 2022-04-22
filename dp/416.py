class Solution:
    def canPartition(self, nums) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2:
            return False
        target = nums_sum // 2
        dp = [False] * (target+1)
        dp[0] = True
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[-1]

sol = Solution()
print(sol.canPartition([1,5,11,5]))
