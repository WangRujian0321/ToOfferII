class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        father_dict = {}
        queue = deque([root])
        while len(queue):
            node = queue.popleft()
            if node.left:
                father_dict[node.left] = node
                queue.append(node.left)
            if node.right:
                father_dict[node.right] = node
                queue.append(node.right)
        father_dict[root] = root
        pathp = []
        pathq = []
        while p != root or q != root:
            if p.val in pathq:
                return p
            if p != root:
                pathp.append(p.val)
                p = father_dict[p]
            if q.val in pathp:
                return q
            if q != root:
                pathq.append(q.val)
                q = father_dict[q]
        return root


m = TreeNode(8)
n = TreeNode(0)
root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))), TreeNode(1, n, m))
sol = Solution()
print(sol.lowestCommonAncestor(root, n, m).val)

