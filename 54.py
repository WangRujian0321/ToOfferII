# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        stack = []
        p = root
        ans = 0
        while p or len(stack):
            while p:
                stack.append(p)
                p = p.right
            p = stack.pop()
            ans += p.val
            p.val = ans
            p = p.left
        return root
