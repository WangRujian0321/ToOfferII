from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root) -> bool:
        if not root:
            return True
        if bool(root.left) ^ bool(root.right):
            return False
        if root.left is None:
            return True
        p0, p1 = root.left, root.right
        stack0 = deque([p0])
        stack1 = deque([p1])

        while len(stack0):
            if len(stack0) != len(stack1):
                return False
            size = len(stack0)
            for _ in range(size):
                node0 = stack0.pop()
                node1 = stack1.pop()
                if node0.val != node1.val or (bool(node0.left) ^ bool(node1.right)) or (bool(node1.left) ^ bool(node0.right)):
                    return False
                if node0.left:
                    stack0.append(node0.left)
                    stack1.append(node1.right)
                if node0.right:
                    stack0.append(node0.right)
                    stack1.append(node1.left)
        return True

sol = Solution()
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(3)
root.left = node1
root.right = node2
node1.right = node3
node2.right = node4
print(sol.isSymmetric(root))