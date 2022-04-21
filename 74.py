class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        merge_ans = [intervals[0]]
        for i in range(1, len(intervals)):
            interval0 = merge_ans[-1]
            interval1 = intervals[i]
            if interval0[1] < interval1[0]:
                merge_ans.append(interval1)
            else:
                merge_ans.pop()
                merge_ans.append([min(interval0[0], interval1[0]), max(interval0[1], interval1[1])])
        return merge_ans

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
