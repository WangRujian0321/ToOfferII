# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def get_num(root, targetSum):
            if root is None:
                return 0
            ans = 0
            if root.val == targetSum:
                ans += 1
            ans += get_num(root.left, targetSum-root.val)
            ans += get_num(root.right, targetSum-root.val)
            return ans
        if root is None:
            return 0
        ans = get_num(root, targetSum)
        ans += self.pathSum(root.left, targetSum)
        ans += self.pathSum(root.right, targetSum)
        return ans


