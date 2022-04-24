class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # num_dict = {}
        # for item in nums:
        #     if item not in num_dict:
        #         num_dict[item] = 1
        #     else:
        #         num_dict[item] += 1
        #         if num_dict[item] == 3:
        #             del num_dict[item]
        # return list(num_dict.keys())[0]
        ones, twos = 0, 0
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
