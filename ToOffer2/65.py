class Solution:
    def add(self, a: int, b: int) -> int:
        s_a = bin(a)[2:]
        s_b = bin(b)[2:]
        i, j, c = 0, 0, 0
        ans = ""
        while i < len(s_a) or j < len(s_b):
            a_i, b_i = 0, 0
            if i < len(s_a):
                a_i = int(s_a[-i-1])
            if j < len(s_b):
                b_i = int(s_b[-i-1])
            k = str(int(not (not a ^ b) ^ c))
            ans = k + ans
            c = bool((a_i and b_i) or (b_i and c) or (a_i and c))
            i += 1
            j += 1
        if c:
            ans = "1" + ans
        return int(ans, 2)

sol = Solution()
print(sol.add(111, 899))