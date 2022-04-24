class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not len(prices):
            return 0
        max_val = 0
        temp = prices[0]
        pre = [0] * len(prices)
        for i in range(len(prices)):
            temp = min(temp, prices[i])
            pre[i] = temp
        for i in range(len(prices)):
            max_val = max(max_val, prices[i] - pre[i])
        return max_val