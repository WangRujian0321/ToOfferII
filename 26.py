# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while 1:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                break
        stack = []
        p = slow
        while p.next:
            p = p.next
            stack.append(p)

        p0 = head
        dummy = ListNode(-1)
        p = dummy
        while len(stack):
            node0 = p0
            p0 = p0.next
            node1 = stack.pop()
            p.next = node0
            node0.next = node1
            node1.next = None
            p = node1
        if p0 == slow:
            p.next = slow
            slow.next = None