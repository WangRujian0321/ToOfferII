class Solution:
    def subsets(self, nums):
        def get_list(string):
            ans = []
            for i in range(len(string)):
                if string[-1-i] == "1":
                    ans.append(nums[i])
            return ans
        ans_lists = []
        for i in range(2 ** len(nums)):
            ans_lists.append(get_list(bin(i)[2:]))
        return ans_lists


sol = Solution()
print(sol.subsets([1,2,3]))