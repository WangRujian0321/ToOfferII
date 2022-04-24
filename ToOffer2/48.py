class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        ans = 0
        for item in s:
            if item in s[i:j]:
                index = s[i:j].index(item)
                i += index+1
            j += 1
            ans = max(j-i, ans)
        return ans


sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))