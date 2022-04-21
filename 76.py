from collections import deque


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(root1, root2):
            dummy = ListNode(-1)
            p, p1, p2 = dummy, root1, root2
            while p1 and p2:
                if p1.val <= p2.val:
                    p.next = p1
                    p1 = p1.next
                    p = p.next
                    p.next = None
                else:
                    p.next = p2
                    p2 = p2.next
                    p = p.next
                    p.next = None
            if p1:
                p.next = p1
            elif p2:
                p.next = p2

            return dummy.next

        if not head:
            return None
        p_ = head
        node_list = deque()
        while p_:
            node_list.append(p_)
            temp = p_
            p_ = p_.next
            temp.next = None
        while len(node_list) > 1:
            node0 = node_list.popleft()
            node1 = node_list.popleft()
            node_list.append(merge(node0, node1))
        return node_list[0]