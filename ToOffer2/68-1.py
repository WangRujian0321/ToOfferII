# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p0 = root
        while 1:
            if (p0.val - p.val) * (p0.val - q.val) <= 0:
                return p0
            if p0.val - p.val > 0:
                p0 = p0.left
            else:
                p0 = p0.right
