class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = deque([root])
        while len(queue):
            ans_item = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                ans_item.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(ans_item)
        return ans