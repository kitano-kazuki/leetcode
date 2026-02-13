# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        carry = 0
        tail = None
        while node2 is not None:
            node1_value = node1.val if node1 is not None else 0
            summed_value = node1_value + node2.val + carry
            node2.val = summed_value % 10
            carry = summed_value // 10
            node1 = node1.next if node1 is not None else None
            if node2.next is None:
                node2.next = node1
                node1 = None
            tail = node2
            node2 = node2.next
        if carry != 0:
            tail.next = ListNode(carry)
        return l2
        