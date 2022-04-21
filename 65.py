class TreeNode:
    def __init__(self):
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def add_words(self, word):
        p = self.root
        n = len(word)
        for i in range(n):
            index = n - 1 - i
            if not p.children[ord(word[index]) - ord('a')]:
                p.children[ord(word[index]) - ord('a')] = TreeNode()
            p = p.children[ord(word[index]) - ord('a')]

    def get_depth(self, root):
        ans = []
        for item in root.children:
            if item:
                ans_item = self.get_depth(item)
                if ans_item == []:
                    ans.append(1)
                else:
                    ans.extend([item + 1 for item in ans_item])
        return ans


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        t = Trie()
        for word in words:
            t.add_words(word)
        ans = t.get_depth(t.root)
        return sum(ans) + len(ans)

sol = Solution()
print(sol.minimumLengthEncoding(["time","me","bell"]))

