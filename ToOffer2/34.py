# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
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
        if root is None:
            return []
        ans = []
        dfs(root, 0, target, [])
        return ans      