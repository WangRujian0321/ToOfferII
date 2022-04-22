class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i = 0
        j = 0
        for j in range(len(nums)):
            if nums[j] % 2:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        return nums


sol = Solution()
print(sol.exchange([1,2,3,4]))