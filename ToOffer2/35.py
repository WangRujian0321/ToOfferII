
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        dummy = Node(-1)
        node_dict, p, p0 = {}, head, dummy
        while p:
            p0.next = Node(p.val)
            p0 = p0.next
            node_dict[p] = p0
            p = p.next
        for item in node_dict:
            node = node_dict[item]
            if item.random:
                node.random = node_dict[item.random]
            else:
                node.random = None
        return dummy.next