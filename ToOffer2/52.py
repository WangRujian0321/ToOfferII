# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p0, p1, n0, n1 = headA, headB, 0, 0
        while p0:
            n0 += 1
            p0 = p0.next
        while p1:
            n1 += 1
            p1 = p1.next
        p0, p1 = headA, headB
        if n0 > n1:
            for _ in range(n0-n1):
                p0 = p0.next
        else:
            for _ in range(n1- n0):
                p1 = p1.next

        while p0 and p1:
            if p0 == p1:
                return p0
            p0 = p0.next
            p1 = p1.next
        return None