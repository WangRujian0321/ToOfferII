class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        p = head
        stack = []
        while p or len(stack):
            if p.child:
                if p.next:
                    stack.append(p.next)
                p.next = p.child
                p.child.prev = p
                p.child = None
            if p.next is None and len(stack):
                node = stack.pop()
                p.next = node
                if node:
                    node.prev = p
            p = p.next
        return head


sol = Solution()
node0 = Node(1, None, None, None)
node1 = Node(2, None, None, None)
node2 = Node(3, None, None, None)
node0.child = node1
node1.child = node2

print(sol.flatten(node0))