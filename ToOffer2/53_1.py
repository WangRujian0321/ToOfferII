class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not len(nums):
            return 0
        n = len(nums)
        left = 0
        right = n-1
        while right > left:
            mid = (right + left) // 2
            if nums[mid] == target:
                break
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        mid = (left + right) // 2
        if nums[mid] != target:
            return 0
        left, right = mid, mid
        while left - 1 >= 0 and nums[left-1] == target:
            left -= 1
        while right + 1 <= n-1 and nums[right+1] == target:
            right += 1
        return right - left + 1