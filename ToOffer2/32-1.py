# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while len(queue):
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                ans.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans