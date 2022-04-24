# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = deque([root])
        ans = []
        while queue:
            node = queue.popleft()
            if node:
                ans.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                ans.append('None')
        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        ans = deque(data.split(','))
        val = int(ans.popleft())
        root = TreeNode(val)
        queue = deque([root])
        while queue:
            node = queue.popleft()
            val0 = ans.popleft()
            val1 = ans.popleft()
            if val0 != "None":
                node.left = TreeNode(int(val0))
                queue.append(node.left)
            if val1 != "None":
                node.right = TreeNode(int(val1))
                queue.append(node.right)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))