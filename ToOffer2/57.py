class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            val = nums[i] + nums[j]
            if val == target:
                return [nums[i], nums[j]]
            elif val < target:
                i += 1
            else:
                j -= 1
        return []
