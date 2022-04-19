class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0
        if root:
            self.get_ans(0, root)
        return self.ans

    def get_ans(self, pre_num, root):
        ans = pre_num * 10 + root.val
        if root.left is None and root.right is None:
            self.ans += ans
        if root.left is not None:
            self.get_ans(ans, root.left)
        if root.right is not None:
            self.get_ans(ans, root.right)


root = TreeNode(1, TreeNode(2), TreeNode(3))
sol = Solution()
print(sol.sumNumbers(root))