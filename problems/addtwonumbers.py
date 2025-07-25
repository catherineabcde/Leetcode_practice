# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        total = ListNode()
        current = total # serve as pointer
        carry = 0

        while l1 or l2 or carry:

            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0

            S = val_l1 + val_l2 + carry

            current.next = ListNode(S % 10)
            current = current.next

            carry = S // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return total.next
