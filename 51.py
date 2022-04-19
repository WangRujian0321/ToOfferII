class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -1001
        self.change_tree(root)
        return self.ans

    def change_tree(self, root):
        left, right = 0, 0
        if root.left:
            self.change_tree(root.left)
            left = max(0, root.left.val)
        if root.right:
            self.change_tree(root.right)
            right = max(0, root.right.val)
        if root.val + left + right > self.ans:
            self.ans = root.val + left + right
        root.val = max(left, right) + root.val