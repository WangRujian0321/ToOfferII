class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        flag = int(nums[-1] == right)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left