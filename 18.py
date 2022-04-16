class Solution:
    def isPalindrome(self, s: str) -> bool:
        def get_pos(alpha):
            if ord(alpha) > 122 or ord(alpha) < 48 or (ord(alpha) > 90 and ord(alpha) < 97) or (ord(alpha) > 57 and ord(alpha) < 65):
                return -1
            else:
                if ord(alpha)<=90:
                    return ord(alpha) + 32
                else:
                    return ord(alpha)
        n = len(s)
        i = 0
        j = n - 1
        while i < j:
            while get_pos(s[i]) < 0 and i < n - 1:
                i += 1
            while get_pos(s[j]) < 0 and j > 0:
                j -= 1
            if get_pos(s[i]) != get_pos(s[j]):
                return False
            i += 1
            j -= 1
        return True