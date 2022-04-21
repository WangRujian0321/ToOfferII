# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from collections import deque
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(node0, node1):
            dummy = ListNode(-1)
            p, p0, p1 = dummy, node0, node1
            while p0 and p1:
                if p0.val <= p1.val:
                    p.next = p0
                    p0 = p0.next
                    p = p.next
                    p.next = None
                else:
                    p.next = p1
                    p1 = p1.next
                    p = p.next
                    p.next = None
            if p0:
                p.next = p0
            elif p1:
                p.next = p1
            return dummy.next
        if len(lists) == 0:
            return None
        node_lists = deque()
        for item in lists:
            if item is not None:
                node_lists.append(item)
        if len(node_lists) == 0:
            return None
        while len(node_lists) > 1:
            node0 = node_lists.popleft()
            node1 = node_lists.popleft()
            node_lists.append(merge(node0, node1))
        return node_lists[0]