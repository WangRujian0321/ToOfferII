class Solution:
    def isAlienSorted(self, words, order: str) -> bool:
        alien_dict = {}
        for i in range(len(order)):
            alien_dict[order[i]] = i
        def compare(s, t):
            ns, nt, i, j = len(s), len(t), 0, 0
            while i < ns and j < nt:
                if alien_dict[s[i]] < alien_dict[t[j]]:
                    return True
                if alien_dict[s[i]] > alien_dict[t[j]]:
                    return False
                i += 1
                j += 1
            return ns <= nt
        for i in range(len(words) - 1):
            if not compare(words[i], words[i+1]):
                return False
        return True


sol = Solution()
print(sol.isAlienSorted(["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))

