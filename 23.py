# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nA, nB = 0, 0
        pA, pB = headA, headB
        while pA:
            nA += 1
            pA = pA.next
        while pB:
            nB += 1
            pB = pB.next
        pA, pB = headA, headB
        if nA > nB:
            for _ in range(nA-nB):
                pA = pA.next
        else:
            for _ in range(nB-nA):
                pB = pB.next
        while pA and pB:
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next
        return None