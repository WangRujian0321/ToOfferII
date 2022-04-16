# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        p = head
        while p:
            temp = p
            p = p.next
            temp.next = dummy.next
            dummy.next = temp
        return dummy.next