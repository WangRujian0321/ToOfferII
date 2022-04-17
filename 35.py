# class Solution:
#     def findMinDifference(self, timePoints: List[str]) -> int:
#         def sub_to_min(s, t):
#             s_split = [int(item) for item in s.split(':')]
#             t_split = [int(item) for item in t.split(':')]
#             return abs((s_split[0] - t_split[0]) * 60 + (s_split[1] - t_split[1]))
#         min_ans = 1440
#         for i in range(len(timePoints)):
#             s_dict = {timePoints[i]: True}
#             for j in range(i+1, len(timePoints)):
#                 if timePoints[j] not in s_dict:
#                     sub = sub_to_min(timePoints[i], timePoints[j])
#                     min_ans = min(min_ans, sub, 1440-sub)
#                     s_dict[timePoints[j]] = True
#                 elif timePoints[i] == timePoints[j]:
#                     return 0
#         return min_ans

import functools
class Solution:
    def findMinDifference(self, timePoints) -> int:
        def cmp(s, t):
            s_split = [int(item) for item in s.split(':')]
            t_split = [int(item) for item in t.split(':')]
            if s_split[0] < t_split[0]:
                return -1
            elif s_split[0] == t_split[0]:
                if s_split[1] <= t_split[1]:
                    return -1
                else:
                    return 1
            else:
                return 1
        def get_min(s, t):
            s_split = [int(item) for item in s.split(':')]
            t_split = [int(item) for item in t.split(':')]
            return (t_split[0] - s_split[0]) * 60 + (t_split[1] - s_split[1])

        timePoints_sort = sorted(timePoints, key=functools.cmp_to_key(cmp))
        min_ans = 1440
        for i in range(len(timePoints_sort) - 1):
            min_ans = min(min_ans, get_min(timePoints_sort[i], timePoints_sort[i+1]))
        min_ans = min(min_ans, 1440 - get_min(timePoints_sort[0], timePoints_sort[-1]))
        return min_ans


sol = Solution()
print(sol.findMinDifference(["01:01", "02:01", "03:00", "03:01"]))

