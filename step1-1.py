# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        bef_node2 = None
        carry = 0
        while node1 is not None and node2 is not None:
            summed_value = node1.val + node2.val + carry
            node2.val = summed_value % 10
            carry = summed_value // 10
            bef_node2 = node2
            node1 = node1.next
            node2 = node2.next
        if node1 is None:
            while node2 is not None:
                summed_value = node2.val + carry
                node2.val = summed_value % 10
                carry = summed_value // 10
                bef_node2 = node2
                node2 = node2.next
            if carry != 0:
                bef_node2.next = ListNode(carry)
            return l2
        bef_node2.next = node1
        bef_node1 = bef_node2
        while node1 is not None:
            summed_value = node1.val + carry
            node1.val = summed_value % 10
            carry = summed_value // 10
            bef_node1 = node1
            node1 = node1.next
        if carry != 0:
            bef_node1.next = ListNode(carry)
        return l2