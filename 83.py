class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []

        def track(first=0):
            if first == n:
                res.append(nums.copy())
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                track(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        track()
        return res