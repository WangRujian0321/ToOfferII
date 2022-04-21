class TreeNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_word_end = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root
        for item in word:
            if not p.children[ord(item) - ord('a')]:
                p.children[ord(item) - ord('a')] = TreeNode()
            p = p.children[ord(item) - ord('a')]
        p.is_word_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        p = self.root
        for item in word:
            if not p.children[ord(item) - ord('a')]:
                return False
            p = p.children[ord(item) - ord('a')]
        return p.is_word_end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        p = self.root
        for item in prefix:
            if not p.children[ord(item) - ord('a')]:
                return False
            p = p.children[ord(item) - ord('a')]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)