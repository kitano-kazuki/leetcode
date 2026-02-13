class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        carry = 0
        tail = None
        while node2 is not None:
            node1_val = 0
            node1_next = None
            if node1 is not None:
                node1_val = node1.val
                node1_next = node1.next
            summed_value = node1_val + node2.val + carry
            node2.val = summed_value % 10
            carry = summed_value // 10
            if node2.next is None:
                node1 = None
                node2.next = node1_next
                tail = node2
                node2 = node2.next
            else:
                node1 = node1_next
                tail = node2
                node2 = node2.next
        if carry != 0:
            tail.next = ListNode(carry) 
        return l2