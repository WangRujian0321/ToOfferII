class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        num = 0
        for item in nums:
            num ^= item
        mask = 1
        while mask & num == 0:
            mask = mask << 1
        num0, num1 = 0, 0
        for item in nums:
            if item & mask:
                num0 ^= item
            else:
                num1 ^= item
        return [num0, num1]