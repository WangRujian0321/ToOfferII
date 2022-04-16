from copy import deepcopy

# from copy import deepcopy
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        n = len(s)
        j = -1
        max_len = 0
        for i in range(len(s)):
            if (i != 0):
                s_set.remove(s[i - 1])
            while j + 1 < n and s[j+1] not in s_set:
                j += 1
                s_set.add(s[j])
            max_len = max(max_len, j - i + 1)
        return max_len


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
