class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal, None)
            node.next = node
            return node
        p = head
        if head.next != head:
            while 1:
                if p.next.val <= p.val:
                    if p.next.val >= insertVal or p.val <= insertVal:
                        break
                    p = p.next
                else:
                    if p.next.val >= insertVal and p.val <= insertVal:
                        break
                    p = p.next
                # if (p.next.val >= insertVal and p.val <= insertVal):
                #     break
                # p = p.next
        node = Node(insertVal)
        node.next = p.next
        p.next = node
        return head


node0 = Node(3)
node1 = Node(3)
node2 = Node(3)
node0.next = node1
node1.next = node2
node2.next = node0
sol = Solution()
print(sol.insert(node0, 0))