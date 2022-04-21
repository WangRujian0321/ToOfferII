class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        def track(first=0):
            if first == n:
                if nums not in res:
                    res.append(nums.copy())
            for i in range(first, n):
                if nums[first] != nums[i] or i == first:
                    nums[first], nums[i] = nums[i], nums[first]
                    track(first+1)
                    nums[first], nums[i] = nums[i], nums[first]
        track()
        return res