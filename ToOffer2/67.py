class Solution:
    def strToInt(self, string: str) -> int:
        flag = 1
        ans = 0
        i = 0
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        while i < len(string):
            if string[i] == " ":
                i += 1
                continue
            elif string[i] == "+" or string[i] == "-" or string[i] in nums:
                if string[i] == "+" or string[i] == "-":
                    flag = (-1) ** int(string[i] == "-")
                    i += 1
                break
            else:
                return 0
        if i >= len(string) or string[i] not in nums:
            return 0
        while i < len(string) and string[i] in nums:
            ans *= 10
            ans += int(string[i])
            i += 1
        ans *= flag
        if ans < - 2 ** 31:
            return - 2 ** 31
        if ans > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return ans

sol = Solution()
print(sol.strToInt("-91283472332"))