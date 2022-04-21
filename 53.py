# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        p0 = root
        ans = None
        while p0:
            if p0.val > p.val:
                ans = p0
                p0 = p0.left
            else:
                p0 = p0.right
        return ans