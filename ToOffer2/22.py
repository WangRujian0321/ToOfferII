# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        p0, p1 = dummy, dummy
        for _ in range(k):
            p1 = p1.next
        while p1:
            p1 = p1.next
            p0 = p0.next
        return p0