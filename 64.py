class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()


    def buildDict(self, dictionary) -> None:
        for item in dictionary:
            p = self.root
            for alpha in item:
                if not p.children[ord(alpha)-ord('a')]:
                    p.children[ord(alpha)-ord('a')] = TreeNode()
                p = p.children[ord(alpha)-ord('a')]
            p.is_word = True

    def search_word(self, node, word):
        p = node
        for item in word:
            if not p.children[ord(item)-ord('a')]:
                return False
            p = p.children[ord(item) - ord('a')]
        return p.is_word

    def search(self, searchWord: str) -> bool:
        p = self.root
        for i in range(len(searchWord)):
            for j in range(len(p.children)):
                if j != ord(searchWord[i]) - ord('a') and p.children[j]:
                    if self.search_word(p.children[j], searchWord[i + 1:]):
                        return True
            if p.children[ord(searchWord[i]) - ord('a')]:
                p = p.children[ord(searchWord[i]) - ord('a')]
            else:
                break
        return False


m = MagicDictionary()
m.buildDict(["hello", "hallo",  "leetcode"])
print(m.search("hello"))
print(m.search("hhllo"))
print(m.search("hell"))
print(m.search("leetcoded"))

