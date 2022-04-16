# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        dummy = ListNode(0, head)
        fast, slow = dummy, dummy
        while 1:
            if fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            else:
                break
        dummy0 = ListNode(0)
        p = slow.next
        while p:
            temp = p
            p = p.next
            temp.next = dummy0.next
            dummy0.next = temp
        p0, p1 = dummy0, dummy
        while p0:
            if p0.val != p1.val:
                return False
            p0 = p0.next
            p1 = p1.next
        return True


sol = Solution()
print(sol.isPalindrome(ListNode(1, ListNode(2))))
