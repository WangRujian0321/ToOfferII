class Solution:
    def firstUniqChar(self, s: str) -> str:
        s_dict = {}
        for item in s:
            if item in s_dict:
                s_dict[item] += 1
            else:
                s_dict[item] = 1
        for item in s:
            if s_dict[item] == 1:
                return item
        return " "