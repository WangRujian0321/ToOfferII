class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        for l in range(n):
            if l > 0 and nums[l] == nums[l-1]:
                continue
            r = n - 1
            target = -nums[l]

            for m in range(l+1, n):
                if m > l + 1 and nums[m] == nums[m-1]:
                    continue
                while m < r and nums[m] + nums[r] > target:
                    r -= 1
                if m == r:
                    break
                if nums[m] + nums[r] == target:
                    ans.append([nums[l], nums[m], nums[r]])
        return ans