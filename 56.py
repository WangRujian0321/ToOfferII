# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        val_dict = {}
        p = root
        stack = []
        while p or len(stack):
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            val = p.val
            if (k-val) in val_dict:
                return True
            val_dict[val] = True
            p = p.right
        return False