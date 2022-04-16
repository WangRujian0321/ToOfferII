# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack0, stack1, p1, p2 = [], [], l1, l2
        while p1:
            stack0.append(p1)
            p1 = p1.next
        while p2:
            stack1.append(p2)
            p2 = p2.next
        dummy = ListNode()
        c = 0
        while len(stack0) or len(stack1):
            val1, val2 = 0, 0
            if len(stack0):
                val1 = stack0.pop().val
            if len(stack1):
                val2 = stack1.pop().val
            val = (val1 + val2 + c) % 10
            c = (val1 + val2 + c) // 10
            node = ListNode(val)
            node.next = dummy.next
            dummy.next = node
        if c:
            node = ListNode(1)
            node.next = dummy.next
            dummy.next = node
        return dummy.next