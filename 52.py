class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode()
        tail = dummy
        stack = []
        while root or len(stack):
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            tail.right = root
            tail = tail.right
            root.left = None
            root = root.right
        return dummy.right

sol = Solution()
root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6, None, TreeNode(8, TreeNode(7), TreeNode(9))))
print(sol.increasingBST(root))