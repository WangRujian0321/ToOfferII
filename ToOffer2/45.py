from functools import cmp_to_key
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            temp0 = int(str(x) + str(y))
            temp1 = int(str(y) + str(x))
            if temp0 > temp1:
                return 1
            else:
                return -1
        nums.sort(key=cmp_to_key(cmp))
        return "".join([str(item) for item in nums])

sol = Solution()
print(sol.minNumber([824,938,1399,5607,6973,5703,9609,4398,8247]))