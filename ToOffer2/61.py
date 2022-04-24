class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        max_val = 0
        min_val = 14
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            if nums[i] in nums[:i]:
                return False
            max_val = max(nums[i], max_val)
            min_val = min(nums[i], min_val)
        if min_val == 14 or min_val == max_val:
            return True
        return max_val - min_val <= 4
