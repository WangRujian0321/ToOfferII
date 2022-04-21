class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        cur = self.stack.pop()
        node = cur.right
        while node:
            self.stack.append(node)
            node = node.left
        return cur.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))

bst = BSTIterator(root)

print(bst.hasNext())
print(bst.next())
print(bst.hasNext())
print(bst.next())
print(bst.hasNext())
print(bst.next())
print(bst.hasNext())
print(bst.next())
print(bst.hasNext())
