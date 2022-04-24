class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = {}
        pre = None
        for item in nums:
            if num_dict == {}:
                num_dict[item] = 1
                pre = item
            elif item == pre:
                num_dict[item] += 1
            else:
                num_dict[pre] -= 1
                if num_dict[pre] == 0:
                    del num_dict[pre]
        return list(num_dict.keys())[0]