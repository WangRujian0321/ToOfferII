# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        p0, p1 = dummy, head
        while p1:
            temp = p1
            p1 = p1.next
            temp.next = dummy.next
            dummy.next = temp
        return dummy.next