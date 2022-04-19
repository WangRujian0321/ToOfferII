from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: TreeNode):
        if not root:
            return []
        ans = []
        queue = deque([root])
        while len(queue):
            size = len(queue)
            max_ans = queue[0].val
            for _ in range(size):
                node = queue.popleft()
                max_ans = max(max_ans, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(max_ans)
        return ans


sol = Solution()
root = TreeNode(1, TreeNode(3, TreeNode(5), TreeNode(3)), TreeNode(2, None, TreeNode(9)))
print(sol.largestValues(root))


