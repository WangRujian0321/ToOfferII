# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        ans = []
        flag = 1
        while len(queue):
            size = len(queue)
            ans_item = []
            for _ in range(size):
                node = queue.popleft()
                if flag:
                    ans_item.append(node.val)
                else:
                    ans_item = [node.val] + ans_item
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(ans_item)
            flag = 1 - flag
        return ans