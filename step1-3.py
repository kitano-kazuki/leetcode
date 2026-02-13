class Solution:
    def _addTwoNumbers(self, l1, l2, carry):
        if l1 is None and l2 is None:
            if carry == 0:
                return None
            return ListNode(carry)
        if l1 is None:
            summed_value = l2.val + carry
            node = ListNode(summed_value % 10)
            carry = summed_value // 10
            node.next = self._addTwoNumbers(None, l2.next, carry)
            return node
        if l2 is None:
            summed_value = l1.val + carry
            node = ListNode(summed_value % 10)
            carry = summed_value // 10
            node.next = self._addTwoNumbers(l1.next, None, carry)
            return node
        summed_value = l1.val + l2.val + carry
        node = ListNode(summed_value % 10)
        carry = summed_value // 10
        node.next = self._addTwoNumbers(l1.next, l2.next, carry)
        return node
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self._addTwoNumbers(l1, l2, 0)
        