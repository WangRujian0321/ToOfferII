class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int):
        def dfs(root, val, target, path):
            val += root.val
            path.append(root.val)
            if val == target and root.left is None and root.right is None:
                ans.append(path.copy())
            if root.left:
                dfs(root.left, val, target, path)
            if root.right:
                dfs(root.right, val, target, path)
            val -= root.val
            path.pop()
        ans = []
        dfs(root, 0, target, [])
        return ans

root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
sol = Solution()
print(sol.pathSum(root, 22))

