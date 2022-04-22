# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if not B or not A:
            return False
        def check(A, B):
            if A is None and B is not None:
                return False
            elif B is None:
                return True
            if A.val != B.val:
                return False
            return check(A.left, B.left) and check(A.right, B.right)
        if check(A, B):
            return True
        elif self.isSubStructure(A.left, B):
            return True
        elif self.isSubStructure(A.right, B):
            return True
        return False