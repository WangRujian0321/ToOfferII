# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = deque([root])
        ans = root.val
        while len(queue):
            size = len(queue)
            ans = queue[0].val
            for i in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return ans