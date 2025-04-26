from typing import Optional
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        head = ListNode()
        cur = head
        while l1 and l2:
            val = l1.val + l2.val + carry

            carry = val // 10
            val = val % 10

            cur.next = ListNode(val = val, next = None)
            cur = cur.next

            l1 = l1.next
            l2 = l2.next
        rem = None
        if l1 or l2:
            if l1:
                rem = l1
            else:
                rem = l2
        while rem:
            val = rem.val + 0 + carry

            carry = val // 10
            val = val % 10

            cur.next = ListNode(val = val , next = None)
            cur = cur.next

            rem = rem.next
        if carry != 0:
            cur . next = ListNode(val = 1, next= None)
        return head.next
