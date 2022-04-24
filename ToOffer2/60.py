class Solution:
    def dicesProbability(self, n: int) -> List[float]:
        if n == 1:
            return [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
        pre_ans = self.dicesProbability(n-1)
        ans = [0] * (len(pre_ans) + 5)
        for i in range(6):
            for j in range(len(pre_ans)):
                ans[i+j] += pre_ans[j] / 6
        return ans