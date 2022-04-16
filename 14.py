from copy import deepcopy
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for item in s1:
            if item in s1_dict:
                s1_dict[item] += 1
            else:
                s1_dict[item] = 1
        s1_dict0 = deepcopy(s1_dict)
        i = 0
        j = 0
        while j < len(s2):
            if s2[j] not in s1_dict:
                j += 1
                i = j
                s1_dict0 = deepcopy(s1_dict)
            elif s2[j] in s1_dict:
                if s2[j] not in s1_dict0:
                    while s2[i] != s2[j]:
                        if s2[i] in s1_dict0:
                            s1_dict0[s2[i]] += 1
                        else:
                            s1_dict0[s2[i]] = 1
                        i += 1
                    i += 1
                else:
                    s1_dict0[s2[j]] -= 1
                    if s1_dict0[s2[j]] == 0:
                        del s1_dict0[s2[j]]
                    if len(list(s1_dict0.keys())) == 0:
                        return True
                j += 1
        return False


sol = Solution()
print(sol.checkInclusion("adc", "dcda"))

