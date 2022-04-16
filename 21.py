# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        p0, p1 = dummy, dummy
        for _ in range(n):
            p1 = p1.next
        while p1.next:
            p1 = p1.next
            p0 = p0.next

        p0.next = p0.next.next
        return dummy.next