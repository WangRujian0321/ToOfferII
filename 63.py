class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_root = False


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def add_root(self, string):
        p = self.root
        for item in string:
            if not p.children[ord(item) - ord('a')]:
                p.children[ord(item) - ord('a')] = TreeNode()
            p = p.children[ord(item) - ord('a')]
        p.is_root = True

    def search_root(self, string):
        p = self.root
        flag = 0
        for i in range(len(string)):
            if not p.children[ord(string[i]) - ord('a')] or p.is_root:
                flag = 1
                break
            p = p.children[ord(string[i]) - ord('a')]
        if flag:
            if p.is_root:
                return string[:i]
        return string
