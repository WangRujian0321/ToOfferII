class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Codec:

    def serialize(self, root):
        if not root:
            return ""
        dq = deque([root])
        res = []
        while dq:
            node = dq.popleft()
            if node:
                res.append(str(node.val))
                dq.append(node.left)
                dq.append(node.right)
            else:
                res.append('None')
        return ','.join(res)

    def deserialize(self, data):
        if not data:
            return []
        dataList = data.split(',')
        root = TreeNode(int(dataList[0]))
        dq = deque([root])
        i = 1
        while dq:
            node = dq.popleft()
            if dataList[i] != 'None':
                node.left = TreeNode(int(dataList[i]))
                dq.append(node.left)
            i += 1
            if dataList[i] != 'None':
                node.right = TreeNode(int(dataList[i]))
                dq.append(node.right)
            i += 1
        return root




root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
sol = Codec()

ser = sol.serialize(root)

root_new = sol.deserialize(ser)

print('aaa')
