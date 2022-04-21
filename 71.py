from collections import OrderedDict
from random import randint


class Solution:

    def __init__(self, w):
        temp = 0
        self.w_list = OrderedDict()
        for i in range(len(w)):
            temp += w[i]
            self.w_list[i] = temp
        self.max = temp

    def pickIndex(self) -> int:
        rand = randint(1, self.max)
        ans = 0
        print('randint:', rand)
        for k in self.w_list:
            if rand > self.w_list[k]:
                continue
            ans = k
        return ans

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

sol = Solution([1,3])
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())
print(sol.pickIndex())


