class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        queue = deque([root])
        stack = []
        while len(queue):
            node = queue.popleft()
            stack.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        for _ in range(len(stack)):
            node = stack.pop()
            if node.left:
                if node.left.val == 0 and node.left.left is None and node.left.right is None:
                    node.left = None
            if node.right:
                if node.right.val == 0 and node.right.left is None and node.right.right is None:
                    node.right = None
        if root.val == 0 and root.left is None and root.right is None:
            return None
        else:
            return root
