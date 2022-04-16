class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        flag = False
        n = len(nums)
        min_len = n
        i = 0
        j = 0
        num_sum = 0
        while j < n:
            num_sum += nums[j]
            j += 1
            if num_sum >= target:
                flag = True
                min_len = min(min_len, j - i)
                num_sum -= nums[i]
                i += 1
        if flag:
            return min_len
        else:
            return 0

sol = Solution()
print(sol.minSubArrayLen(1))