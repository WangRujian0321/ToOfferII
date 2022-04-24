class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, j, num_sum = 0, 1, 1
        ans = []
        while i < j:
            if num_sum < target:
                j += 1
                num_sum += j
            elif num_sum == target:
                if j > i + 1:
                    ans.append([i, j])
                i += 1
                num_sum -= i
            else:
                i += 1
                num_sum -= i
        return [list(range(item[0]+1, item[1]+1)) for item in ans]