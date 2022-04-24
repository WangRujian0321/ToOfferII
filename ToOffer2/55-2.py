# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        self.depth(root)

        def judge(root):
            if not root:
                return True
            left, right = 0, 0
            if root.left:
                left = root.left.val
            if root.right:
                right = root.right.val
            if abs(left - right) > 1:
                return False
            return judge(root.left) and judge(root.right)

        return judge(root)

    def depth(self, root):
        val = 1
        if root.left:
            self.depth(root.left)
            val = max(root.left.val + 1, val)
        if root.right:
            self.depth(root.right)
            val = max(root.right.val + 1, val)
        root.val = val