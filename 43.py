from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        if not root:
            self.num = 0
            self.root = None
            return
        self.num = 0
        self.root = root
        queue = deque([root])
        while len(queue):
            node = queue.popleft()
            self.num += 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def insert(self, v: int) -> int:
        if self.root is None:
            node = TreeNode(v)
            self.num = 1
            self.root = node
            return None
        node = TreeNode(v)
        self.num += 1
        bin_sum = bin(self.num)[3:]
        path = list(bin_sum[:-1])
        p = self.root
        while len(path):
            direc = path[0]
            if direc == '1':
                p = p.right
            else:
                p = p.left
            del path[0]
        if bin_sum[-1] == '0':
            p.left = node
        else:
            p.right = node
        return p.val

    def get_root(self) -> TreeNode:
        return self.root


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))
m = CBTInserter(root)
print(m.insert(7))
print(m.insert(8))
print(m.get_root().val)

