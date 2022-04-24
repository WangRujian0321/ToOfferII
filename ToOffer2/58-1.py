class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split()
        s_split.reverse()
        return " ".join(s_split)