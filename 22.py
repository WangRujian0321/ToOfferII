# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        fast, slow = head, head
        while 1:
            if fast.next is None or fast.next.next is None:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast


node_list = [-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5]
num = 24
def gen_list(nodes_num, num):
    nodes = []
    for item in nodes_num:
        nodes.append(ListNode(item))
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    nodes[-1].next = nodes[num]
    return nodes[0]
sol = Solution()
node = gen_list(node_list, num)
print(sol.detectCycle(node).val)