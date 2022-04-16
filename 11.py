class Solution:
    def findMaxLength(self, nums) -> int:
        nums_dict = {0: -1}
        temp = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                temp += -1
            else:
                temp += 1
            if temp not in nums_dict:
                nums_dict[temp] = i
            elif temp in nums_dict:
                max_len = max(max_len, i - nums_dict[temp])
        return max_len


sol = Solution()
print(sol.findMaxLength([0,1]))
