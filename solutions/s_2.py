# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode(0)
        p1, p2, cur = l1, l2, ret
        carry = 0
        while p1 or p2:
            x = p1.val if p1 else 0
            y = p2.val if p2 else 0
            s = x + y + carry
            carry = int(s / 10)
            cur.next = ListNode(s % 10)
            cur = cur.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        if carry:
            cur.next = ListNode(carry)
        return ret.next
