class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre_sum = [0]
        temp = 0
        for item in nums:
            temp += item
            pre_sum.append(temp)
        min_val = 0
        max_val = nums[0]
        for i in range(1, len(pre_sum)):
            max_val = max(max_val, pre_sum[i] - min_val)
            min_val = min(pre_sum[i], min_val)
        return max_val