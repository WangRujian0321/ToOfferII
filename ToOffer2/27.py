# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#  递归方法
# class Solution:
#     def mirrorTree(self, root: TreeNode) -> TreeNode:
#         if not root:
#             return
#         root.left, root.right = root.right, root.left
#         root.left = self.mirrorTree(root.left)
#         root.right = self.mirrorTree(root.right)
#         return root

# 迭代方法
from collections import deque
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        # if not root:
        #     return
        # root.left, root.right = root.right, root.left
        # root.left = self.mirrorTree(root.left)
        # root.right = self.mirrorTree(root.right)
        # return root
        if not root:
            return None
        queue = deque([root])
        while len(queue):
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                node.left, node.right = node.right, node.left
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

