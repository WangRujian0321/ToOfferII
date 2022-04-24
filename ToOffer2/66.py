class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        left, right = 1, 1
        count = 0
        pos = 0
        for i in range(len(a)):
            if a[i] == 0:
                count += 1
                pos = i
            else:
                right *= a[i]
        if count:
            if count == 1:
                return [0] * pos + [right] + [0] * (len(a)-pos-1)
            else:
                return [0] * len(a)
        ans = []
        for i in range(len(a)):
            right //= a[i]
            ans.append(left * right)
            left *= a[i]
        return ans