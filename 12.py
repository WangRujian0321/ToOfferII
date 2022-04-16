class Solution:
    def pivotIndex(self, nums) -> int:
        n = len(nums)
        num_sums = [0] * (n + 1)
        temp = 0
        for i in range(n):
            temp += nums[i]
            num_sums[i+1] = temp
        for i in range(0, n):
            # print(temp - nums[i] - num_sums[i])
            # print(num_sums[i])
            if temp - nums[i] - num_sums[i] == num_sums[i]:
                return i
        return -1


sol = Solution()
print(sol.pivotIndex([1,7,3,6,5,6]))